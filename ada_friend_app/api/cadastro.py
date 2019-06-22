from flask import request
from loguru import logger
from flasgger import swag_from
from flask_restful import Resource
from pymongo.errors import DuplicateKeyError
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.modulo.cadastro import cadastrar
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.modulo.jwt_auth import Token

class Cadastro(Resource):
    @swag_from('../../docs/api/cadastrar_post.yml')
    def post(self):
        logger.debug("[CADASTRO] Requisição recebida")
        try:
            response = request.json
            cadastro = cadastrar(response)
            if not cadastro:
                Resposta.error("Não foi possivel cadastrar!")
            token = Token.gerar(cadastro['senha'], cadastro['_id'])
            return Resposta.token_validado(token)
        except ExpiredSignatureError:
            return Resposta.nao_aceito('Não foi possivel criar token')
        except DuplicateKeyError:
            return Resposta.nao_aceito("Usuário já existe!")
        except Exception as e:
            return Resposta.error(str(e))