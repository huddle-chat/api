from app.extensions import db


class ChannelAllowedRoles(db.Model):
    __table_args__ = (
        db.UniqueConstraint('channel_id', 'role_id'),
      )
    channel_id = db.Column(
        db.BigInteger,
        db.ForeignKey("channel.channel_id", ondelete="CASCADE"),
        primary_key=True
    )
    role_id = db.Column(
        db.BigInteger,
        db.ForeignKey("role.role_id", ondelete="CASCADE"),
        primary_key=True
    )
    can_message = db.Column(db.Boolean, server_default=db.text("true"))
    role = db.relationship("Role", cascade="all, delete")

    def __repr__(self) -> str:
        return f"""
            <ChannelAllowedRole channel_id={self.channel_id},
            role_id={self.role_id}>
            """
