from flask import request
from loguru import logger
from flask_restful import Resource

from ada_friend_app.modulo.tipo import set_tipo

class Tipo(Resource):

    def get(self):
        return ['evento', 'palestra', 'ideia', 'profissão', 'discussão']
    
    def post(self):
        response = request.json
        return set_tipo(**response)
