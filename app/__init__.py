from flask import Flask
from config import Config


def create_app(config_class=Config):
    base_url = '/api/v1/'
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize flask extensions here

    # Register blueprints here
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix=base_url + "auth")

    @app.route("/test")
    def test_route():
        return {"success": True}

    return app
