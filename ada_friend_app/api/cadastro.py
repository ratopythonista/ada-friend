from flask import request
from loguru import logger
from flask_restful import Resource
from pymongo.errors import DuplicateKeyError

from ada_friend_app.modulo.cadastro import cadastrar
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.modulo.jwt_auth import Token

class Cadastro(Resource):
    def post(self):
        try:
            response = request.json
            cadastro = cadastrar(response)
            if not cadastro:
                Resposta.error("Não foi possivel cadastrar!")
            token = Token(cadastro['senha'], cadastro['_id']).token
            if not token:
                Resposta.error("Não foi possivel gerar token!")
            return Resposta.token_validado(token.decode('utf-8'))
        except DuplicateKeyError:
            return Resposta.nao_aceito("Usuário já existe!")
        except Exception as e:
            return Resposta.error(str(e))