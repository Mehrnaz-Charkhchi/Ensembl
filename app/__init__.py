import os

from flask import Flask, Blueprint
from flask_restplus import Api

from app.config import app_config

basedir = os.path.abspath(os.path.dirname(__file__))
app_blueprint = Blueprint('api', __name__, url_prefix='/api', )
app_blueprint_api = Api(app_blueprint, version='1.0', title='Ensembl Search API',
                        description='Simple Ensemble Search API')


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)

    return app


env = os.getenv("ENV", 'development')
app = create_app(env.lower())
