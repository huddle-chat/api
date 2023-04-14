from datetime import timedelta
from flask_restful import Resource, reqparse
from flask import make_response
from app.rpc.users_rpc import register_user, get_user_for_login,\
    get_user_verification_code, verify_user, get_current_user_by_id
from grpc import RpcError
import grpc
import bcrypt
import redis
from app.extensions import jwt
from flask_jwt_extended import create_access_token,\
    get_jwt, jwt_required,\
    get_jwt_identity
from app.common.email import send_verification_email
import os

ACCESS_EXPIRES = timedelta(hours=1)

REDIS_HOST = os.getenv("REDIS_HOST")

jwt_redis_blocklist = redis.StrictRedis(
    host=REDIS_HOST, port=6379, db=0, decode_responses=True
)


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


auth_register_post_args = reqparse.RequestParser()
auth_register_post_args.add_argument(
    "username",
    type=str,
    help="Username is required",
    required=True
)
auth_register_post_args.add_argument(
    "email",
    type=str,
    help="Email is required",
    required=True
)
auth_register_post_args.add_argument(
    "password", type=str,
    help="Password required. Must be between 8 and 20 characters",
    required=True
)


class AuthRegister(Resource):
    def post(self):
        args = auth_register_post_args.parse_args()
        try:
            email, verification_code = register_user(
                args['username'], args['password'], args['email']
            )

            send_verification_email(email, verification_code)

            return {
                'success': True,
                'message': """Thanks for signing up! We've sent a
                    verification code to your email.""",
                'data': None
            }
        except RpcError as e:
            code = 500
            message = "Something went wrong. Please try again."
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                message = e.details()
                code = 409
            return {
                'success': False,
                'message': message,
                'data': None
            }, code


auth_verify_post_args = reqparse.RequestParser()
auth_verify_post_args.add_argument(
    "email",
    type=str,
    help="Please provide a valid email address.",
    required=True
)
auth_verify_post_args.add_argument(
    "verificationCode",
    type=int,
    help="Pleas provide the verification code sent to your email.",
    required=True
)


class AuthVerify(Resource):
    def post(self):
        args = auth_verify_post_args.parse_args()
        try:
            res = get_user_verification_code(args['email'])
            if "isVerified" in res and res["isVerified"] is True:
                return {
                    "success": False,
                    "message": "User is already verified.",
                    "data": None
                }
            else:
                valid = res["verificationCode"] == args["verificationCode"]
                if valid is True:
                    user = verify_user(args["email"])
                    if "isVerified" in user and user["isVerified"] is True:
                        return {
                            "success": True,
                            "message": "Thank you for verifying your email!",
                            "data": None
                        }
                    else:
                        return {
                            "success": False,
                            "message": "Something went wrong.\
                                Please try again later.",
                            "data": None
                        }
                else:
                    return {
                        "success": False,
                        "message": "Incorrect verification code.",
                        "data": None
                    }
        except RpcError as e:
            code = 500
            message = "Something went wrong."
            if e.code() == grpc.StatusCode.NOT_FOUND:
                code = 404
                message = e.details()
            return {
                'success': False,
                'message': message,
                'data': None
            }, code


auth_login_post_args = reqparse.RequestParser()
auth_login_post_args.add_argument(
    "email",
    type=str,
    help="Please enter a valid email.",
    required=True
)
auth_login_post_args.add_argument(
    "password",
    type=str,
    help="Password required.",
    required=True
)


class AuthLogin(Resource):
    def post(self):
        try:
            args = auth_login_post_args.parse_args()
            user = get_user_for_login(args['email'])

            valid_password = bcrypt.checkpw(
                args['password'].encode(),
                user['password'].encode()
            )

            if valid_password:
                del user['password']
                if "isVerified" not in user:
                    user["isVerified"] = False
                access_token = create_access_token(identity=user['userId'])
                resp = make_response({
                    'success': True,
                    'message': "Welcome back!",
                    'data': {
                        'user': user,
                        'token': access_token
                    }
                })

                return resp
            else:
                return {
                    'success': False,
                    'message': "Incorrect password.",
                    'data': None
                }

        except RpcError as e:
            print(e)
            code = 500
            message = "Something went wrong."
            if e.code() == grpc.StatusCode.NOT_FOUND:
                code = 404
                message = e.details()
            return {
                'success': False,
                'message': message,
                'data': None
            }, code


class AuthLogout(Resource):
    @jwt_required()
    def delete(self):
        jti = get_jwt()['jti']
        jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
        return {
            "success": True,
            "message": "Successfully logged out.",
            "data": None
        }


class AuthMe(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            current_user = get_current_user_by_id(int(current_user_id))

            del current_user['password']

            return {
                "success": True,
                "message": "Welcome back!",
                "data": {
                    "user": current_user
                }
            }
        except RpcError as e:
            code = 500
            message = "Something went wrong."
            if e.code() == grpc.StatusCode.NOT_FOUND:
                code = 404
                message = e.details()
            resp = make_response({
                    'success': False,
                    'message': message,
                    "data": None
                })
            # Clear the malformed token, prompt user for login again

            return resp, code
        # Some error that wasn't thrown by rpc
        except Exception as e:
            print("error here", e)
            message = "Something went wrong"
            code = 500
            return {
                "success": False,
                "message": message,
                "data": None
            }, code
