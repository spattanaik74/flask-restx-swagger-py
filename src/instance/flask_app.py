from flask import Flask
from flask_restx import Api


app = Flask(__name__)

api = Api(app, version='1.1', title='Flask-reastx-swagger', prefix='/api/v1',
          description='swagger api check')