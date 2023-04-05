from app.extensions import db
from app.common.util import sf


class Role(db.Model):
    role_id = db.Column(
        db.BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    guild_id = db.Column(
        db.BigInteger,
        db.ForeignKey("guild.guild_id", ondelete="CASCADE"),
        nullable=False
    )
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, server_default=db.text("'#ffffff'"))
    can_invite = db.Column(db.Boolean, server_default=db.text("false"))
    can_create_channel = db.Column(db.Boolean, server_default=db.text("false"))
    can_delete_channel = db.Column(db.Boolean, server_default=db.text("false"))
    can_delete_message = db.Column(db.Boolean, server_default=db.text("false"))
    can_kick_member = db.Column(db.Boolean, server_default=db.text("false"))
    members = db.relationship(
          "GuildMemberRole",
          cascade="all, delete",
          passive_deletes=True,
          back_populates="role"
    )

    def __repr__(self):
        return f"<Role name={self.name} guild_id={self.guild_id} >"
