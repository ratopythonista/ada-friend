from flask import request
from loguru import logger
from flask_restful import Resource

from ada_friend_app.modulo.tipo import set_tipo
from ada_friend_app.api.resposta_api import Resposta

class Tipo(Resource):

    def get(self):
        return ['evento', 'palestra', 'ideia', 'profissão', 'discussão']
    
    def post(self):
        try:
            response = request.json
            return Resposta.sucesso(set_tipo(**response))
        except Exception as e:
            return Resposta.error(str(e))
