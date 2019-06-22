from datetime import datetime, timedelta

import jwt
from jwt.exceptions import ExpiredSignatureError

from ada_friend_app.config import JWT_PWD, JWT_EXP


class Token:
    # TODO: ALTERAR PARA HORAS A VALIDAÇÃO DO TOKEN
    def __init__(self, senha):
        self.token = self.__token(senha)

    def __token(self, senha):
        return jwt.encode({'pwd': senha, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP)}, JWT_PWD, algorithm='HS256')

    def validar_token(self):
        try:
            self.token = self.__token(jwt.decode(self.token, JWT_PWD, algorithms='HS256'))
        except ExpiredSignatureError:
            return None
        
        return self.token

