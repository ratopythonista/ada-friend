from datetime import datetime, timedelta

import jwt

from ada_friend_app.config import JWT_PWD, JWT_EXP


class Token:
    @staticmethod
    def gerar(senha, id_usuario):
        print(id_usuario) 
        return jwt.encode({'pwd': senha, 'id_usuario': id_usuario, 'exp': datetime.utcnow() + timedelta(days=JWT_EXP)}, 
            JWT_PWD, algorithm='HS256')

    @staticmethod
    def validar_token(token):
        print(token)   
        return jwt.decode(bytes(token, encoding='utf-8'), JWT_PWD, algorithms='HS256')
