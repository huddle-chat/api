from app.extensions import db
from app.common.util import sf


class Channel(db.Model):
    channel_id = db.Column(
        db.BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    type = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    position = db.Column(db.Integer)
    everyone_can_view = db.Column(db.Boolean, server_default=db.text('false'))
    everyone_can_chat = db.Column(db.Boolean, server_default=db.text('false'))
    guild_id = db.Column(
          db.BigInteger,
          db.ForeignKey("guild.guild_id", ondelete="CASCADE"),
          nullable=True
        )
    members = db.relationship(
          "ChannelMember",
          back_populates="channel",
          cascade="all, delete",
          passive_deletes=True
        )
    messages = db.relationship(
        "Message",
        cascade="all, delete",
        passive_deletes=True
    )
    # last message ID

    def __repr__(self):
        return f"<Channel id={self.channel_id}>"
