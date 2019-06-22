from loguru import logger
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.modulo.cripto import Sha256
from ada_friend_app.modulo.jwt_auth import Token
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.servico.mod_database import Database


class Interesses(Resource):
    @swag_from('../../docs/api/interesses_get.yml')
    def get(self):
        return Resposta.retorno(Database().get_document('interesses')[0]['interesses'])

    @swag_from('../../docs/api/interesses_post.yml')
    def post(self):
        json = request.json

        if json.get('token', False) and json.get('interesses', False):
            try:
                info_token = Token.validar_token(json['token'])

                Database().update_document('usuarios', {'_id': info_token['id_usuario']}, {'interesses': json['interesses']})

                return Resposta.sucesso('Interesses cadastrados!')
            except ExpiredSignatureError:
                return Resposta.nao_aceito('Token expirado')
            except Exception as e:
                return Resposta.error(str(e))
        else:
            return Resposta.error('JSON Inválido!')
