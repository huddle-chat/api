from app.extensions import db
from app.models.guild import Guild
from app.models.user import User


db.drop_all()
db.create_all()
