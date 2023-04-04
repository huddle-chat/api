from flask import Flask
from config import Config
from app.extensions import db, api
from app.resources.auth import AuthLogin, AuthRegister, AuthLogout
from app.resources.guild import GuildsByUser, GuildById, Guilds
from app.resources.channel import ChannelsByGuild, ChannelById
from app.resources.messages import MessagesByChannel


def create_app(config_class=Config):
    base_url = '/api/v1/'
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register api routes here
    # routes for authentication
    api.add_resource(AuthLogin, base_url + "auth/login")
    api.add_resource(AuthRegister, base_url + "auth/register")
    api.add_resource(AuthLogout, base_url + "auth/logout")

    #routes for guilds
    api.add_resource(GuildsByUser, base_url + "user/<int:user_id>/guilds")
    api.add_resource(GuildById, base_url + "guilds/<int:guild_id>")
    api.add_resource(Guilds, base_url + "guilds")

    # routes for channels
    api.add_resource(ChannelsByGuild, base_url + "guilds/<int:guild_id>/channels")
    api.add_resource(ChannelById, base_url + "channels/<int:channel_id>")

    # routes for messages
    api.add_resource(MessagesByChannel, base_url + "channels/<int:channel_id>/messages")

    # Initialize flask extensions here
    db.init_app(app)
    api.init_app(app)

    return app
