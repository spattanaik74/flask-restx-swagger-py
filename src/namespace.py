from src.instance.flask_app import api

user_api = api.namespace('users', description='user operations')