from datetime import datetime, timedelta

import jwt
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.config import JWT_PWD, JWT_EXP


class Token:
    def __init__(self, senha='', id_usuario=''):
        self.token = self.__token(senha, id_usuario)

    def __token(self, senha, id_usuario):
        return jwt.encode({'pwd': senha, 'id_usuario': id_usuario, 'exp': datetime.utcnow() + timedelta(hours=JWT_EXP)}, JWT_PWD, algorithm='HS256')

    def validar_token(self, token):
        return self.__token(jwt.decode(bytes(token, 'utf-8'), JWT_PWD, algorithms='HS256'))

