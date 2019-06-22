import os

from loguru import logger
from flask_restful import Resource

from ada_friend_app.servico.mod_database import ModDatabase


class Status(Resource):
    def get(self):
        logger.debug("[STATUS - Requisição recebida]")
        __db = ModDatabase('ada-friend',
                           user='admin', password=os.environ.get('PASSAF'),
                           host='ds117540.mlab.com', port='17540')
        logger.debug("[STATUS - Conexão com o banco está ok!]")
        return {'code': 400, 'message': f'{__db}'}
