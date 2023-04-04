from flask_restful import Resource


class UserById(Resource):
    def get(self, user_id):
        return {"message": f"Getting user info for user with ID: {user_id}"}

    def patch(self, user_id):
        return {"message": f"Updating user info for user with id: {user_id}"}

    def delete(self, user_id):
        return {"message": f"Deleting user with id: {user_id}"}
