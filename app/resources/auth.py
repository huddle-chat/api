from flask_restful import Resource


class AuthRegister(Resource):
    def post(self):
        return {"message": "This is the register route"}


class AuthLogin(Resource):
    def post(self):
        return {"message": "This is the login route"}


class AuthLogout(Resource):
    def post(self):
        return {"message": "This is the logout route"}
