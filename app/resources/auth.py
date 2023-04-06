from flask_restful import Resource, reqparse
from app.rpc.users_rpc import register_user, get_user_for_login
from grpc import RpcError
import grpc
import bcrypt

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
        print(args)
        try:
            register_user(args['username'], args['password'],args['email'])
            return {
                'success': True,
                'message': "Thanks for signing up!",
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
                return {
                    'success': True,
                    'message': "Welcome back!",
                    'data': {
                        'user': user
                    }
                }
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
    def post(self):
        return {"message": "This is the logout route"}
