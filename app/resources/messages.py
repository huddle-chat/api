from flask_restful import Resource


class MessagesByChannel(Resource):
    def get(self, channel_id):
        return {"message": f"Getting messages for channel: {channel_id}"}

    def post(self, channel_id):
        return {"message": f"Posting message to channel: {channel_id}"}
