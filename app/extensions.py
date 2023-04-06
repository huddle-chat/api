from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail

api = Api()
jwt = JWTManager()
mail = Mail()
