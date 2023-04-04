from flask_restful import Resource


class ChannelById(Resource):
    def get(self, channel_id):
        return {"message": f"Getting channel info for channel: {channel_id}"}

    def delete(self, channel_id):
        return {"message": f"Deleting channel: {channel_id}"}

    def patch(self, channel_id):
        return {"message": f"Updating channel: {channel_id}"}


class ChannelsByGuild(Resource):
    # This will need to only select the channels that the current user has
    # access to within the guild
    def get(self, guild_id):
        return {"message": f"Getting channels for guild: {guild_id}"}

    def post(self, guild_id):
        return {"message": f"Creating channel for guild: {guild_id}"}
