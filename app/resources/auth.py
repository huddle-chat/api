from flask_restful import Resource
# from app.extensions import db
from marshmallow import Schema, fields
# from app.models.user import User
from app.models.guild import Guild


class UserSchema(Schema):
    user_id = fields.Int()
    username = fields.Str()
    email = fields.Str()


class GuildMemberSchema(Schema):
    member = fields.Nested(UserSchema)
    joined_at = fields.DateTime()


class GuildSchema(Schema):
    guild_id = fields.Int()
    name = fields.Str()
    created_at = fields.DateTime()
    icon = fields.Str()
    description = fields.String()
    members = fields.List(fields.Nested(GuildMemberSchema))


class AuthRegister(Resource):
    def post(self):
        guild = Guild.query.get(7049155216561733632)
        schema = GuildSchema()
        json = schema.dump(guild)

        return {'message': 'success', 'guild': json}


class AuthLogin(Resource):
    def post(self):
        return {"message": "This is the login route"}


class AuthLogout(Resource):
    def post(self):
        return {"message": "This is the logout route"}
