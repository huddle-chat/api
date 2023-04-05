from app.extensions import db


class GuildMemberRole(db.Model):
    __table_args__ = (
        db.UniqueConstraint('guild_member_id', 'role_id'),
      )
    guild_member_id = db.Column(
        db.BigInteger,
        db.ForeignKey("guild_member.guild_member_id", ondelete="CASCADE"),
        primary_key=True
    )
    role_id = db.Column(
        db.BigInteger,
        db.ForeignKey("role.role_id", ondelete="CASCADE"),
        primary_key=True
    )
    member = db.relationship(
        "GuildMember",
        back_populates="roles",
        cascade="all, delete"
    )
    role = db.relationship(
        "Role",
        back_populates="members",
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<GMRole gm_id={self.guild_member_id} role_id={self.role_id}>"
