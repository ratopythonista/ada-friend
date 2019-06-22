import os

from Crypto.Hash import SHA256
from pymongo.errors import DuplicateKeyError

from ada_friend_app.servico.mod_database import Database
from ada_friend_app.modulo.cripto import Sha256

def cadastrar(infos):
    __db = Database()
    if __db.get_document('usuarios', {'nick':infos['nick']}):
        raise DuplicateKeyError('Nick já existe!')
    infos = {
        '_id':infos['email'], 
        'nick':infos['nick'], 
        'senha':Sha256(infos['senha']).hash,
        'interesses':list(),
        'tipo':list()
    }

    __db.set_document('usuarios', infos)
    return infos