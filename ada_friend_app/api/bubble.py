from flask import request
from bson import ObjectId
from loguru import logger
from flasgger import swag_from
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError

# from ada_friend_app.modulo.tipo import set_tipo
from ada_friend_app.modulo.jwt_auth import Token
from ada_friend_app.api.resposta_api import Resposta
from ada_friend_app.servico.mod_database import Database
from ada_friend_app.servico.utils import converter_objectid



class Bubble(Resource):
    @swag_from('../../docs/api/feed_get.yml')
    def get(self):
        return Resposta.retorno(converter_objectid(Database().get_document('postagens')))
    
    @swag_from('../../docs/api/feed_post.yml')
    def post(self):
        json = request.json

        if json.get('token', False) and json.get('tipo', False) and json.get('interesse', False) \
            and json.get('texto', False):

            try:
                info_token = Token.validar_token(json['token'])

                Database().set_document('postagens', {
                    'usuario': info_token['id_usuario'],
                    'tipo': json['tipo'],
                    'interesse': json['interesse'],
                    'texto': json['texto'],
                    'likes': [],
                    'comentarios': [] 
                })

                return Resposta.sucesso('Postagem enviada')
            except ExpiredSignatureError:
                return Resposta.nao_aceito('Token expirado')
            except Exception as e:
                return Resposta.error(str(e))
        else:
            return Resposta.error('JSON Inválido!')

    #TODO: renovar cookie
    @swag_from('../../docs/api/feed_put.yml')
    def put(self):
        json = request.json

        if json.get('token', False) and json.get('id_post', False) \
            and (json.get('comentario', False) or json.get('like', False)):

            try:
                info_token = Token.validar_token(json['token'])
                json['id_post'] = ObjectId(json['id_post'])

                if json.get('comentario', False):
                    Database().update_document('postagens', {'_id': json['id_post']}, {
                        '$push': {'comentarios': [info_token['id_usuario'], json['comentario']]}
                    })

                    return Resposta.sucesso('Comentário enviado')
                else:
                    Database().update_document('postagens', {'_id': json['id_post']},{
                        '$push': {'likes': info_token['id_usuario']}
                    })

                    return Resposta.sucesso('Curtida enviada')
            except ExpiredSignatureError:
                return Resposta.nao_aceito('Token expirado')
            except Exception as e:
                return Resposta.error(str(e))
        else:
            return Resposta.error('JSON Inválido!')


class FiltrarBubble(Resource):
    @swag_from('../../docs/api/listarfeed_post.yml')
    def post(self):
        json = request.json

        if json.get('token', False) and json.get('interesses', False):

            try:
                info_token = Token.validar_token(json['token'])

                resultado = Database().get_document('postagens', {
                    'interesse': {'$in': json['interesses']},
                })

                return Resposta.retorno(converter_objectid(resultado))
            except ExpiredSignatureError:
                return Resposta.nao_aceito('Token expirado')
            except Exception as e:
                return Resposta.error(str(e))
        else:
            return Resposta.error('JSON Inválido!')

    # #TODO: renovar cookie
    # def put(self):
    #     json = request.json

    #     if json.get('token', False) and json.get('id_post', False) \
    #         and (json.get('comentario', False) or json.get('like', False)):

    #         try:
    #             info_token = Token.validar_token(json['token'])
    #             json['id_post'] = ObjectId(json['id_post'])

    #             if json.get('comentario', False):
    #                 Database().update_document('postagens', {'_id': json['id_post']}, {
    #                     '$push': {'comentarios': [info_token['id_usuario'], json['comentario']]}
    #                 })

    #                 return Resposta.sucesso('Comentário enviado')
    #             else:
    #                 Database().update_document('postagens', {'_id': json['id_post']},{
    #                     '$push': {'likes': info_token['id_usuario']}
    #                 })

    #                 return Resposta.sucesso('Curtida enviada')
    #         except ExpiredSignatureError:
    #             return Resposta.nao_aceito('Token expirado')
    #         except Exception as e:
    #             return Resposta.error(str(e))
    #     else:
    #         return Resposta.error('JSON Inválido!')
