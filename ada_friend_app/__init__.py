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

template = {
    "swagger": "2.0",
    "info": {
        "title": "HACKATON - TEMPO DE MUDANÇAS",
        "description": "",
        "version": "0.0.2"
    },
    # "basePath": "/api",
    # "host": "localhost:5000",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

app = Flask(__name__)
CORS(app)
api = Api(app)
swagger = Swagger(app, template=template)

add_resources(api)
