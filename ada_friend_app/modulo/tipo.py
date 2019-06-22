from ada_friend_app.servico.mod_database import Database
from ada_friend_app.modulo.jwt_auth import Token

def set_tipo(token, tipos):
    infos = Token().validar_token(token)
    # VERIFICA EXISTENCIA NO BD