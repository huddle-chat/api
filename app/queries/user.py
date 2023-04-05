from app.extensions import db
from app.models.user import User
from app.common.schemas import UserSchema
import bcrypt


def create_user(username: str, email: str, password: str):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = User(username=username, email=email, password=hashed_pw.decode())
    db.session.add(new_user)
    db.session.commit()
    new_user = db.session.query(User).filter_by(username=username).first()
    schema = UserSchema()
    json = schema.dump(new_user)
    return json
