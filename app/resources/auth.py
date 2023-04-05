from flask_restful import Resource
from app.queries.channel import get_user_channels_by_guild


class AuthRegister(Resource):
    def post(self):
        # db.drop_all()
        # db.create_all()
        res = get_user_channels_by_guild(7049386703114534913, 7049387349465169920)
        return {'message': 'success', 'channels': res}


class AuthLogin(Resource):
    def post(self):
        return {"message": "This is the login route"}


class AuthLogout(Resource):
    def post(self):
        return {"message": "This is the logout route"}
