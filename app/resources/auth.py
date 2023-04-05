from flask_restful import Resource
from app.queries.user import create_user


class AuthRegister(Resource):
    def post(self):
        result = create_user("matt-2", "test@mail.com", "something")
        return {'message': 'success', 'channels': result}


class AuthLogin(Resource):
    def post(self):
        return {"message": "This is the login route"}


class AuthLogout(Resource):
    def post(self):
        return {"message": "This is the logout route"}
