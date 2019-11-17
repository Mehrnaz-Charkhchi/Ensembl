from peewee import Model, CharField, OperationalError
from app.utils.db_connection import mysql_db_connection
from app.utils.error_response import database_not_found_error_response, parameter_400_error_response
from app.utils.result_templates import gene_result_template


class BaseModel(Model):
    class Meta:
        database = mysql_db_connection


class GeneAutoComplete(BaseModel):
    stable_id = CharField(max_length=128, primary_key=True)
    display_label = CharField(max_length=128)
    species = CharField(max_length=255)
    location = CharField(max_length=60)

    @staticmethod
    def search(lookup, species=None):
        if len(lookup) < 3:
            return parameter_400_error_response()
        try:
            gene_results_model = GeneAutoComplete \
                .select() \
                .where(
                GeneAutoComplete.display_label.contains(lookup))
            if species:
                gene_results_model = gene_results_model.where(
                    GeneAutoComplete.species == species
                )
            gene_results_model = gene_results_model.execute()
            gene_results_dict = gene_result_template(gene_results_model)
        except OperationalError:
            gene_results_dict = database_not_found_error_response()
        return gene_results_dict

    class Meta:
        table_name = 'gene_autocomplete'
