from flask import request
from peewee import OperationalError

from app import app, app_blueprint
from app.routes import genes_blueprint
from app.utils.error_response import not_found_404_error_response, internal_server_error_response, \
    not_allowed_405_error_response, parameter_400_error_response

app.register_blueprint(genes_blueprint)

app.register_blueprint(app_blueprint)


@app.errorhandler(400)
def parameter_400_error_handler():
    return parameter_400_error_response()


@app.errorhandler(404)
def not_found_404_error_handler(e):
    return not_found_404_error_response(request)


@app.errorhandler(405)
def not_allowed_405_error_handler():
    return not_allowed_405_error_response(request)


@app.errorhandler(500)
def internal_server_error_handler():
    return internal_server_error_response(request)


@app.errorhandler(OperationalError)
def database_not_found_error_handler():
    return database_not_found_error_handler()


if __name__ == "__main__":
    app.run()
