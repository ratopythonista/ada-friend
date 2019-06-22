from ada_friend_app.api.tipo import Tipo
from ada_friend_app.api.login import Login
from ada_friend_app.api.status import Status
from ada_friend_app.api.bubble import Bubble
from ada_friend_app.api.cadastro import Cadastro
from ada_friend_app.api.interesses import Interesses
from ada_friend_app.api.informacao import Informacao

def add_resources(api):
    api.add_resource(Status, '/api/status')
    api.add_resource(Cadastro, '/api/cadastrar')
    api.add_resource(Login, '/api/login')
    api.add_resource(Tipo, '/api/tipo')
    api.add_resource(Interesses, '/api/interesses')
    api.add_resource(Informacao, '/api/informacao')
    api.add_resource(Bubble, '/api/feed')

