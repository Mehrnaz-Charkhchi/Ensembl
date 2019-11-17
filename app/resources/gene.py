from flask_restplus import Resource, abort
from flask import request

from app import app_blueprint_api
from app.models.gene import GeneAutoComplete


class GeneSearchAPI(Resource):

    @app_blueprint_api.doc(
        responses={200: 'OK',
                   400: 'Invalid Argument',
                   500: 'Mapping Key Error',
                   405: 'Method Not Allowed'},
        params={'lookup': 'Specify lookup parameter bigger that 3 characters.',
                'species': 'Specify the species.'})
    def get(self):
        """Returns list of genes based on query lookup and species parameters."""
        lookup = request.args.get('lookup', '')

        species = request.args.get('species', None)
        result_dict = GeneAutoComplete.search(lookup, species)
        return result_dict
