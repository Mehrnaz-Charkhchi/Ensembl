from flask import Blueprint
from flask_restplus import Api

genes_blueprint = Blueprint('genes', __name__, url_prefix='/api', )
genes_blueprint_api = Api(genes_blueprint, version='1.0', title='Ensembl Search API',
                          description='Simple Ensemble Genes Search API')

from app.resources.gene import GeneSearchAPI

genes_blueprint_api.add_resource(GeneSearchAPI, '/genes')
