from app.extensions import db
from app.models.user import User
from app.models.guild import Guild
from app.models.channel import Channel
from app.models.channel_member import ChannelMember
from app.models.guild_member import GuildMember
from app.models.role import Role
from app.models.guild_member_role import GuildMemberRole
from app.models.channel_allowed_roles import ChannelAllowedRoles
import random
from math import floor
from app.queries.channel import get_users_with_channel_access


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

        #Assign random users to each guild
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

    new_obj = []
    # Create test roles for each guild:
    for guild in selected_guilds:
        for k in range(4):
            # This gives random permissions for each role for testing purposes
            role = Role(
                name=f"Test Role #{k}",
                can_invite=True if random.randint(1,2) % 2 == 0 else False,
                can_create_channel=True if random.randint(1,2) % 2 == 0 else False,
                can_delete_channel=True if random.randint(1,2) % 2 == 0 else False,
                can_delete_message=True if random.randint(1,2) % 2 == 0 else False,
                can_kick_member=True if random.randint(1,2) % 2 == 0 else False,
              )
            guild.roles.append(role)
            new_obj.append(role)


    db.session.add_all(new_obj)
    db.session.commit()

    new_gmrs = []

    #Assign random guild members to each role
    for guild in selected_guilds:
        # Select all roles within the current guild
        selected_roles = db.session.query(Role).filter_by(guild_id=guild.guild_id).all()
        # select all guild members for the current guild
        selected_gms = db.session.query(GuildMember).filter_by(guild_id=guild.guild_id).all()
        for role in selected_roles:
            rand_start = random.randint(0,floor(len(selected_gms) / 2))
            rand_end = random.randint(floor(len(selected_gms) / 2) + 1,len(selected_gms) -1)
            # Grabbing a random set of users from the guild
            for i in range(rand_start, rand_end +1):
                gmr = GuildMemberRole()
                gmr.member = selected_gms[i]
                role.members.append(gmr)
                new_gmrs.append(gmr)

    db.session.add_all(new_gmrs)
    db.session.commit()

    new_cars = []

    # Assign 1 allowed role per channel
    for guild in selected_guilds:
        # grab all channels for the given guild
        gcs = db.session.query(Channel).filter_by(guild_id=guild.guild_id).all()
        # grab all roles for the given guild
        grs = db.session.query(Role).filter_by(guild_id=guild.guild_id).all()

        #loop over each channel and choose a random role to allow
        for channel in gcs:
            rand_index = random.randint(0, len(grs)-1)
            car = ChannelAllowedRoles()
            car.role = grs[rand_index]
            channel.allowed_roles.append(car)
            new_cars.append(car)

    db.session.add_all(new_cars)
    db.session.commit()

    # Loop through all the users that have access to a given channel and
    # create channel_member rows for them

    new_cms = []

    for guild in selected_guilds:
        # grab all channels for the given guild
        gcs = db.session.query(Channel).filter_by(guild_id=guild.guild_id).all()

        for channel in gcs:
            users = get_users_with_channel_access(channel.channel_id)
            print("did we even get here?", users)
            for user_id, user in users:
                cm = ChannelMember()
                user.channels.append(cm)
                cm.channel = channel
                new_cms.append(cm)

    db.session.add_all(new_cms)
    db.session.commit()


def small_seed_db():
    db.drop_all()
    db.create_all()
    user = User(
        username="matt-yard",
        email="mattyard11@gmail.com",
        password="pass1234"
    )
    guild = Guild(name="Matt's Server")
    gm = GuildMember()
    gm.member = user
    guild.members.append(gm)

    channel1 = Channel(
        type=1,
        position=1,
        name="general"
    )
    channel2 = Channel(
        type=1,
        position=2,
        name="admin-channel"
    )

    guild.channels.append(channel1)
    guild.channels.append(channel2)

    role = Role(name="Admin")

    guild.roles.append(role)

    gmr = GuildMemberRole()
    gmr.member = gm
    role.members.append(gmr)

    db.session.add_all([user, guild, gm, channel1, channel2, role])
    db.session.commit()


