from app.extensions import db
from app.common.util import sf


class User(db.Model):
    user_id = db.Column(
        db.BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
        )
    username = db.Column(
        db.String,
        unique=True,
        nullable=False
        )
    email = db.Column(
        db.String,
        unique=True,
        nullable=False
        )
    password = db.Column(db.String, nullable=False)
    online_status = db.Column(db.Integer, server_default=db.text("1"))
    created_at = db.Column(
            db.DateTime,
            nullable=False,
            server_default=db.func.now()
        )
    avatar = db.Column(db.String, server_default="None")
    guilds = db.relationship(
            "GuildMember",
            back_populates="member",
            cascade="all, delete",
            passive_deletes=True
        )
    channels = db.relationship(
            "ChannelMember",
            back_populates="member",
            cascade="all, delete",
            passive_deletes=True
        )

    def __repr__(self):
        return f"<User id={self.user_id} username={self.username}>"
