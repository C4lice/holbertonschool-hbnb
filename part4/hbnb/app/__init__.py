from flask import Flask
import config

from app.extensions import bcrypt, restx_api
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    restx_api.init_app(app)
    jwt.init_app(app)

    from app.api.v1.users import api as users_ns
    from app.api.v1.admin import admin_api
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as reviews_ns
    from app.api.v1.auth import api as auth_ns
    

    restx_api.add_namespace(users_ns, path='/api/v1/users')
    restx_api.add_namespace(places_ns, path='/api/v1/places')
    restx_api.add_namespace(amenities_ns, path='/api/v1/amenities')
    restx_api.add_namespace(reviews_ns, path='/api/v1/reviews')
    restx_api.add_namespace(auth_ns, path='/api/v1/auth')
    restx_api.add_namespace(admin_api, path='/api/v1/admin')

    return app

def create_app(config_class=config['development']):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    restx_api.init_app(app)

    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as reviews_ns

    restx_api.add_namespace(users_ns, path='/api/v1/users')
    restx_api.add_namespace(places_ns, path='/api/v1/places')
    restx_api.add_namespace(amenities_ns, path='/api/v1/amenities')
    restx_api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
