from flask_restful import Resource, reqparse
from flask import make_response
from app.rpc.users_rpc import register_user, get_user_for_login
from grpc import RpcError
import grpc
import bcrypt
from flask_jwt_extended import create_access_token,\
    set_access_cookies, unset_access_cookies, jwt_required
from app.common.email import send_verification_email

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
                    }
                })
                set_access_cookies(resp, access_token)
                return resp
            else:
                return {
                    'success': False,
                    'message': "Incorrect password.",
                    'data': None
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


class AuthLogout(Resource):
    def get(self):
        resp = make_response({
            'success': True,
            'message': "Successfully logged out!",
            "data": None
        })
        unset_access_cookies(resp)
        return resp

    @jwt_required()
    def post(self):
        return {"message": "protected route"}
