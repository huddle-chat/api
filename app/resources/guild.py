from flask_restful import Resource


class Guilds(Resource):
    def post(self):
        return {"message": "Creating a new guild"}


class GuildsByUser(Resource):
    def get(self, user_id):
        return {"message": f"Getting guilds for user: {user_id}"}


class GuildById(Resource):
    def get(self, guild_id):
        return {"message": f"Getting guild with ID: {guild_id}"}

    def delete(self, guild_id):
        return {"message": f"Deleting guild with ID: {guild_id}"}

    def patch(self, guild_id):
        return {"message": f"Updating guild with ID: {guild_id}"}
