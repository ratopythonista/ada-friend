__version__ = '0.0.1'

import sys

from flask import Flask
from loguru import logger
from flask_cors import CORS
from flasgger import Swagger
from flask_restful import Api

from ada_friend_app.api import add_resources


logger.add("file_1.log", rotation="500 MB")
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

app = Flask(__name__)
CORS(app)
api = Api(app)
swagger = Swagger(app)

add_resources(api)
