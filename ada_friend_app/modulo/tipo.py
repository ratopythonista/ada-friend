from ada_friend_app.servico.mod_database import Database
from ada_friend_app.modulo.jwt_auth import Token

def set_tipo(token, tipos):
    __db = Database()
    infos = Token.validar_token(token)
    usuario = __db.get_document('usuarios', filter=
    {'$and':[{'_id':infos['email']}, {'senha':infos['senha']}]})
    if usuario:
        __db.update_document('usuarios', filter={'_id':usuario[0]['_id']}, 
        value={'tipo':tipos})
    return "Sucesso!"