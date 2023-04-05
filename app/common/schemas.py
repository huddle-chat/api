from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    avatar = fields.Str()
    online_status = fields.Int()
    created_at = fields.DateTime()

class UserNoEmail(Schema):
    user_id = fields.Int()
    username = fields.Str()
    avatar = fields.Str()
    online_status = fields.Int()
    created_at = fields.DateTime()

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


class ChannelMemberSchema(Schema):
    member = fields.Nested(UserSchema)
    last_seen_message_id = fields.Int()

class ChannelSchema(Schema):
    channel_id = fields.Int()
    name = fields.Str()
    type = fields.Int()
    date_created = fields.DateTime()
    position = fields.Int()
    everyone_can_view = fields.Bool()
    everyone_can_chat = fields.Bool()
    guild_id = fields.Int()
    last_message_id = fields.Int()
