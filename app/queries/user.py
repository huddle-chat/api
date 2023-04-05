from app.extensions import db
from app.models.user import User
from app.common.schemas import UserSchema
import bcrypt


def create_user(username: str, email: str, password: str):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = User(
        username=username,
        email=email,
        password=hashed_pw.decode()
    )

    db.session.add(new_user)
    db.session.commit()

    # Refreshing the user to get the ID that was generated
    db.session.refresh(new_user)
    # Serializing to JSON so it can be sent back via HTTP
    schema = UserSchema()
    json = schema.dump(new_user)

    return json
