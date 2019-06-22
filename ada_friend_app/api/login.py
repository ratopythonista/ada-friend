from loguru import logger
from flask import request
from flasgger import swag_from
from flask_restful import Resource

from ada_friend_app.modulo.cripto import Sha256
from ada_friend_app.modulo.jwt_auth import Token
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.servico.mod_database import Database


class Login(Resource):
    @swag_from('../../docs/api/login_post.yml')
    def post(self):
        json = request.json

        if json.get('email', False) and json.get('senha', False):
            senha = Sha256(json['senha']).hash
            usuario = Database().get_document('usuarios', {'email': json['email'], 'senha': senha})

            if usuario:
                usuario = usuario[0]
                logger.debug(f"{json['email']} - CONECTADO")
                return Resposta.token_validado(Token(usuario['senha'], usuario['email']).token)
            else:
                logger.debug(f"{json['email']} - ERRO DE ACESSO")                
                return Resposta.nao_aceito('Usuário ou senha inválido!')
        else:
            return Resposta.error('JSON Inválido!')
