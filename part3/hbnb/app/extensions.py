from flask_bcrypt import Bcrypt
from flask_restx import Api

bcrypt = Bcrypt()
restx_api = Api(version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
