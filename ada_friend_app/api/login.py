from loguru import logger
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError

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
            usuario = Database().get_document('usuarios', {'_id': json['email'], 'senha': senha})

            if usuario:
                usuario = usuario[0]
                logger.debug(f"{json['email']} - CONECTADO")

                try:
                    token = Token.gerar(usuario['senha'], usuario['_id'])
                    return Resposta.token_validado(token)
                except ExpiredSignatureError:
                    return Resposta.nao_aceito('Token expirado')
                except Exception as e:
                    return Resposta.error(str(e))          
            else:
                logger.debug(f"{json['email']} - ERRO DE ACESSO")                
                return Resposta.nao_aceito('Usuário ou senha inválido!')
        else:
            return Resposta.error('JSON Inválido!')
