from app.__init__ import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
