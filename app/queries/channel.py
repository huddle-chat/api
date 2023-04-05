from app.models.channel import Channel
from app.models.channel_member import ChannelMember
from app.models.user import User
from app.common.schemas import ChannelSchema
from app.extensions import db


def get_user_channels_by_guild(user_id: int, guild_id: int):
    results = db.session.query(Channel, ChannelMember.last_seen_message_id)\
            .outerjoin(
                ChannelMember,
                Channel.channel_id == ChannelMember.channel_id
              )\
            .outerjoin(User, ChannelMember.member_id == User.user_id)\
            .filter(Channel.guild_id == 7049387349465169920)\
            .filter(ChannelMember.member_id == 7049386703114534912)\
            .all()
    print(type(results[0][0]))
    result_dicts = []
    schema = ChannelSchema()
    for channel, last_seen_message_id in results:
        channel = schema.dump(channel)
        channel['last_seen_message_id'] = last_seen_message_id
        result_dicts.append(channel)

    return result_dicts
