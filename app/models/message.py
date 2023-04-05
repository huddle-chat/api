from app.extensions import db
from app.common.util import sf


class Message(db.Model):
    message_id = db.Column(
        db.BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    channel_id = db.Column(
        db.BigInteger,
        db.ForeignKey(
                "channel.channel_id",
                ondelete="CASCADE",
                name="fk_channel"
            ),
        nullable=False
    )
    author_id = db.Column(
        db.BigInteger,
        db.ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False
    )
    content = db.Column(
        db.Text,
        nullable=False
    )
    timestamp = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )
    edited_timestamp = db.Column(
        db.DateTime,
        nullable=True,
        onupdate=db.func.now()
    )
    mention_everyone = db.Column(
        db.Boolean,
        server_default=db.text("false")
    )
    author = db.relationship("User")

    def __repr__(self) -> str:
        return f"""<Message message_id={self.message_id},
         author_id={self.author_id}"""
