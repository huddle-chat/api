from app.auth import bp

@bp.route("/")
def index():
    return {"message": "This is the auth blueprint"}


@bp.route("/login")
def login():
    return {"message": "This is the login route"}
