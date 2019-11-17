from flask_restplus import fields
# from rest_api_demo.api.restplus import api
from app import app_blueprint_api

gene = app_blueprint_api.model('Gene', {
    'stable_id': fields.String(read_only=True, required=True, min_length=3, max_length=128,
                               description='Article title'),
    'display_label': fields.String(read_only=True, description='Article content'),
    'species': fields.String(read_only=True, description='Article content'),
    'location': fields.String(read_only=True, description='Article content'),
})

pagination = app_blueprint_api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_genes = app_blueprint_api.inherit('Page of blog posts', {
    'items': fields.List(fields.Nested(gene))
})
