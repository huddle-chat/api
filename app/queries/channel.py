from app.models.channel import Channel
from app.models.channel_member import ChannelMember
from app.models.user import User
from app.common.schemas import ChannelSchema
from app.common.schemas import UserNoEmail
from app.models.guild_member import GuildMember
from app.models.guild_member_role import GuildMemberRole
from app.models.role import Role
from app.models.channel_allowed_roles import ChannelAllowedRoles
from app.extensions import db
from sqlalchemy import distinct, or_


# Gets a list of channels that the current user has
# access to within the given guild
def get_user_channels_by_guild(user_id: int, guild_id: int):
    results = db.session.query(Channel, ChannelMember.last_seen_message_id)\
            .outerjoin(
                ChannelMember,
                Channel.channel_id == ChannelMember.channel_id
              )\
            .outerjoin(User, ChannelMember.member_id == User.user_id)\
            .filter(Channel.guild_id == guild_id)\
            .filter(ChannelMember.member_id == user_id)\
            .all()

    result_dicts = []
    schema = ChannelSchema()
    print(results)
    for channel, last_seen_message_id in results:
        channel = schema.dump(channel)
        channel['last_seen_message_id'] = last_seen_message_id
        channel['has_unread_message'] = False if last_seen_message_id is None\
            else (last_seen_message_id < channel["last_message_id"])
        result_dicts.append(channel)

    return result_dicts


# Selects all users who have at least one role that is in the allowed_roles for
# the given channel
def get_users_with_channel_access(channel_id):
    result = db.session.query(distinct(User.user_id), User)\
            .join(GuildMember, User.user_id == GuildMember.member_id)\
            .join(
                GuildMemberRole,
                GuildMember.guild_member_id == GuildMemberRole.guild_member_id
              )\
            .join(Role, GuildMemberRole.role_id == Role.role_id)\
            .join(
                ChannelAllowedRoles,
                Role.role_id == ChannelAllowedRoles.role_id
              )\
            .join(
                Channel,
                ChannelAllowedRoles.channel_id == Channel.channel_id
            )\
            .filter(or_(
                ChannelAllowedRoles.channel_id == channel_id,
                Channel.everyone_can_view == True
              )).all()
    result_dicts = []
    schema = UserNoEmail()
    for user_id, user in result:
        user = schema.dump(user)
        result_dicts.append(user)

    print(len(result_dicts))
    return result_dicts
