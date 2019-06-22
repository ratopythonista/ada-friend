from datetime import datetime, timedelta

import jwt

from ada_friend_app.config import JWT_PWD, JWT_EXP


class Token:
    # TODO: ALTERAR PARA HORAS A VALIDAÇÃO DO TOKEN
    def __init__(self, senha, id_usuario):
        self.token = self.__token(senha, id_usuario)
        self.info_token = None

    def __token(self, senha, id_usuario):
        return jwt.encode({'pwd': senha, 'id_usuario': id_usuario, 'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP)}, JWT_PWD, algorithm='HS256')

    def validar_token(self, token):      
        self.info_token = jwt.decode(bytes(token, encoding='utf-8'), JWT_PWD, algorithms='HS256')
        self.__token(self.info_token)

        return self.info_token
