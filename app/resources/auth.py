from flask_restful import Resource
from app.common.seed import seed_db


class AuthRegister(Resource):
    def post(self):
        seed_db()
        return {'message': 'success'}


class AuthLogin(Resource):
    def post(self):
        return {"message": "This is the login route"}


class AuthLogout(Resource):
    def post(self):
        return {"message": "This is the logout route"}
