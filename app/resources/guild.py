from flask_restful import Resource
from app.rpc.guilds_rpc import get_guilds_by_user_id
from flask_jwt_extended import jwt_required, get_jwt_identity


class Guilds(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            guilds = get_guilds_by_user_id(int(current_user_id))
            return {
                "success": True,
                "message": f"Successsfully fetched guilds for the user {current_user_id}",
                "data": guilds
            }

        except Exception as e:
            print(e)
            code = 500
            message = "something went wrong"
            return {
                "success": False,
                "message": message,
                "data": None
            }, code

    def post(self):
        return {"message": "Creating a new guild"}


class GuildsByUser(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            guilds = get_guilds_by_user_id(current_user_id)
            return {
                "success": True,
                "message": f"Successsfully fetched guilds for the user {current_user_id}",
                "data": guilds
            }

        except Exception as e:
            code = 500
            message = "something went wrong"
            return {
                "success": False,
                "message": message,
                "data": None
            }, code


class GuildById(Resource):
    def get(self, guild_id):
        return {"message": f"Getting guild with ID: {guild_id}"}

    def delete(self, guild_id):
        return {"message": f"Deleting guild with ID: {guild_id}"}

    def patch(self, guild_id):
        return {"message": f"Updating guild with ID: {guild_id}"}
