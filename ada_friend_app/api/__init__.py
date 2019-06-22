from ada_friend_app.api.login import Login
from ada_friend_app.api.status import Status
from ada_friend_app.api.cadastro import Cadastro
from ada_friend_app.api.tipo import Tipo

def add_resources(api):
    api.add_resource(Status, '/api/status')
    api.add_resource(Cadastro, '/api/cadastrar')
    api.add_resource(Login, '/api/login')
    api.add_resource(Tipo, '/api/tipo')
