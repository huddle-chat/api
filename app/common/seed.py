from app.extensions import db
from app.models.user import User
from app.models.guild import Guild
from app.models.channel import Channel
from app.models.guild_member import GuildMember
from app.models.role import Role
from app.models.guild_member_role import GuildMemberRole
from app.models.channel_allowed_roles import ChannelAllowedRoles
import random


def seed_db():
    # drop all tables and recreate them
    db.drop_all()
    db.create_all()

    new_users = []

    # create 20 new test users
    for x in range(20):
        user = User(
            username=f"test-user{x}",
            email=f"test-email{x}@mail.com",
            password="pass1234"
        )
        new_users.append(user)

    db.session.add_all(new_users)
    db.session.commit()

    # Select all users to be used later
    selected_users = db.session.query(User).all()

    new_guilds = []

    # create 5 test guilds

    for x in range(5):
        guild = Guild(name=f"Test-Guild #{x}")
        new_guilds.append(guild)

    db.session.add_all(new_guilds)
    db.session.commit()

    # Assign each guild members
    selected_guilds = db.session.query(Guild).all()

    new_obj = []

    for guild in selected_guilds:
        rand_start = random.randint(0,9)
        rand_end = random.randint(10,19)
        for i in range(rand_start, rand_end +1):
            gm = GuildMember()
            gm.member = selected_users[i]
            guild.members.append(gm)
            new_obj.append(gm)
        # also create 3 new channels for each guild
        for j in range(3):
            channel = Channel(
                type=1,
                position=j+1,
                name=f"Test-Channel #{j}"
            )
            guild.channels.append(channel)
            new_obj.append(channel)

    db.session.add_all(new_obj)
    db.session.commit()







