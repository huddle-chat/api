from flask_restful import Resource, reqparse
from app.rpc.guilds_rpc import get_guilds_by_user_id, create_guild
from flask_jwt_extended import jwt_required, get_jwt_identity


guild_post_args = reqparse.RequestParser()
guild_post_args.add_argument(
    "name",
    type=str,
    help="Please enter a valid guild name.",
    required=True
)
guild_post_args.add_argument(
    "description",
    type=str,
    help="Description optional.",
    required=False
)
guild_post_args.add_argument(
    "icon",
    type=str,
    help="Icon optional.",
    required=False
)


class Guilds(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            guilds = get_guilds_by_user_id(int(current_user_id))
            return {
                "success": True,
                "message": f"""Successsfully fetched guilds
                for the user {current_user_id}""",
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

    @jwt_required()
    def post(self):
        try:
            current_user_id = get_jwt_identity()

            args = guild_post_args.parse_args()

            new_guild = create_guild(
                int(current_user_id),
                args['name'],
                args['description'] if 'description' in args else None,
                args['icon'] if 'icon' in args else "None",
            )

            return {
                "success": True,
                "message": "Successfully created guild.",
                "data": new_guild
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


class GuildsByUser(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user_id = get_jwt_identity()
            guilds = get_guilds_by_user_id(current_user_id)
            return {
                "success": True,
                "message": f"""Successsfully fetched guilds
                for the user {current_user_id}""",
                "data": guilds
            }

        except Exception:
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
