from app.extensions import db


class ChannelMember(db.Model):
    channel_id = db.Column(
          db.BigInteger,
          db.ForeignKey("channel.channel_id", ondelete="CASCADE"),
          primary_key=True
        )
    member_id = db.Column(
          db.BigInteger,
          db.ForeignKey("user.user_id", ondelete="CASCADE"),
          primary_key=True
        )
    channel = db.relationship("Channel", back_populates="members")
    member = db.relationship("User", back_populates="guilds")
    # last seen message id
