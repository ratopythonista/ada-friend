from ada_friend_app.api.status import Status
from ada_friend_app.api.cadastro import Cadastro


def add_resources(api):
    api.add_resource(Status, '/api/status')
    api.add_resource(Cadastro, '/api/cadastrar')
