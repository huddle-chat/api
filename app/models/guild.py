from app.extensions import db
from app.common.util import sf


class Guild(db.Model):
    guild_id = db.Column(
        db.BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    icon = db.Column(db.String, server_default="None")
    description = db.Column(db.String)
    members = db.relationship("GuildMember", back_populates="guild")

    def __repr__(self):
        return f"<Guild id={self.guild_id}, name={self.name}>"
