from ada_friend_app.api.login import Login
from ada_friend_app.api.status import Status


def add_resources(api):
    api.add_resource(Status, '/api/status')
    api.add_resource(Login, '/api/login')
