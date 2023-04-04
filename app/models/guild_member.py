from app.extensions import db
from app.common.util import sf


class GuildMember(db.Model):
    guild_member_id = db.Column(
          db.BigInteger,
          primary_key=True,
          default=lambda: int(next(sf))
        )
    user_id = db.Column(
          db.BigInteger,
          db.ForeignKey('user.user_id', ondelete="CASCADE"),
          nullable=False
        )
    guild_id = db.Column(
          db.BigInteger,
          db.ForeignKey('guild.guild_id', ondelete="CASCADE"),
          nullable=False
        )
    joined_at = db.Column(db.DateTime, server_default=db.func.now())
    is_owner = db.Column(db.Boolean, server_default=db.text("false"))
    guild = db.relationship("Guild", back_populates="members")
    member = db.relationship("User", back_populates="guilds")
