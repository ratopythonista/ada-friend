from ada_friend_app.servico.mod_database import Database
from ada_friend_app.modulo.jwt_auth import Token

def set_bubble(token, dados, pai):
    __db = Database()
    infos = Token.validar_token(token)
    usuario = __db.get_document('usuarios', filter=
    {'$and':[{'_id':infos['id_usuario']}, {'senha':infos['pwd']}]})
    if usuario:
        __db.set_document('bubbles', dados)
    return "Sucesso!"

def get_bubble(bubble_id):
    __db = Database()
    return __db.get_document('bubbles', filter={'_id':bubble_id})