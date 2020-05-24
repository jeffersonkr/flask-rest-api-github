from flask_restplus import Api
from .user import api as ns1
from .repository import api as ns2

api = Api(
    title='REST API for GITHUB',
    version='1.0',
    description='A simple REST API for access info from github.',
)

api.add_namespace(ns1, path='/users')
api.add_namespace(ns2, path='/repos')
