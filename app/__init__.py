from flask import Flask
from config import Config
from app.extensions import api, jwt, mail
from app.resources.auth import AuthLogin, AuthRegister, AuthLogout, AuthVerify
from app.resources.guild import GuildsByUser, GuildById, Guilds
from app.resources.channel import ChannelsByGuild, ChannelById
from app.resources.messages import MessagesByChannel
from app.resources.user import UserById


def create_app(config_class=Config):
    base_url = '/api/v1/'
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register api routes here
    # routes for authentication
    api.add_resource(AuthLogin, base_url + "auth/login")
    api.add_resource(AuthRegister, base_url + "auth/register")
    api.add_resource(AuthLogout, base_url + "auth/logout")
    api.add_resource(AuthVerify, base_url + "auth/verify")

    # routes for guilds
    api.add_resource(GuildsByUser, base_url + "user/<int:user_id>/guilds")
    api.add_resource(GuildById, base_url + "guilds/<int:guild_id>")
    api.add_resource(Guilds, base_url + "guilds")

    # routes for channels
    api.add_resource(
            ChannelsByGuild,
            base_url + "guilds/<int:guild_id>/channels"
        )
    api.add_resource(ChannelById, base_url + "channels/<int:channel_id>")

    # routes for messages
    api.add_resource(
            MessagesByChannel,
            base_url + "channels/<int:channel_id>/messages"
        )

    # routes for users
    api.add_resource(UserById, base_url + "users/<int:user_id>")

    # Initialize flask extensions here
    api.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    return app
