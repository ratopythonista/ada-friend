from ada_friend_app.servico.mod_database import Database
from ada_friend_app.modulo.jwt_auth import Token

def set_tipo(token, tipos):
    infos = Token.validar_token(token)
    usuario = Database().get_document('usuarios', filter=
    {'$and':[{'_id':infos['email']}, {'senha':infos['senha']}]})
    if usuario:
        pass


    return infos