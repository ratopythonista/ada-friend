from loguru import logger
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.modulo.jwt_auth import Token
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.servico.mod_database import Database


class Informacao(Resource):
    @swag_from('../../docs/api/informacao_post.yml')
    def post(self):
        json = request.json

        if json.get('token', False):
            try:
                info_token = Token.validar_token(json['token'])

                usr = Database().get_document('usuarios', {'_id': info_token['id_usuario']}, {'senha': 0})[0]
                usr['email'] = usr['_id']
                del usr['_id']

                return Resposta.retorno([usr])
            except ExpiredSignatureError:
                return Resposta.nao_aceito('Token expirado')
            except Exception as e:
                return Resposta.error(str(e))
        else:
            return Resposta.error('JSON Inválido!')
