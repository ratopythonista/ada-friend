import os

from Crypto.Hash import SHA256
from pymongo.errors import DuplicateKeyError

from ada_friend_app.servico.mod_database import ModDatabase

def cadastrar(infos):
    __db = ModDatabase('ada-friend',
        user='admin', password=os.environ.get('PASSAF'),
        host='ds117540.mlab.com', port='17540')
    if __db.get_document('usuarios', {'nick':infos['nick']}):
        raise DuplicateKeyError('Nick já existe!')

    hash = SHA256.new()
    hash.update(infos['senha'].encode('utf-8'))
    infos = {
        '_id':infos['email'], 
        'nick':infos['nick'], 
        'senha':hash.hexdigest()
    }

    __db.set_document('usuarios', infos)
    return infos