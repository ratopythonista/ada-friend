from datetime import datetime, timedelta

import jwt
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.config import JWT_PWD, JWT_EXP


class Token:
    # TODO: ALTERAR PARA HORAS A VALIDAÇÃO DO TOKEN
    def __init__(self, senha, id_usuario):
        self.token = self.__token(senha, id_usuario)

    def __token(self, senha, id_usuario):
        return jwt.encode({'pwd': senha, 'id_usuario': id_usuario, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP)}, JWT_PWD, algorithm='HS256')

    def validar_token(self):
        try:
            self.token = self.__token(jwt.decode(self.token, JWT_PWD, algorithms='HS256'))
        except ExpiredSignatureError:
            return None
        
        return self.token

