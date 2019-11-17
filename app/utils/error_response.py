from flask import jsonify


def database_not_found_error_response():
    message = {
        'status': 500,
        'message': 'A database was required but none was found.',
    }
    resp = message
    try:
        resp = jsonify(message)
        resp.status_code = 500
    except:
        pass
    return resp


def not_allowed_405_error_response(request):
    message = {
        'status': 405,
        'message': 'Request is not allowed: ' + request.url,
    }
    resp = message
    try:
        resp = jsonify(message)
        resp.status_code = 405
    except:
        pass
    return resp


def not_found_404_error_response(request):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = message
    try:
        resp = jsonify(message)
        resp.status_code = 404
    except:
        pass
    return resp


def internal_server_error_response(request):
    message = {
        'status': 500,
        'message': 'Internal server error: ' + request.url,
    }
    resp = message
    try:
        resp = jsonify(message)
        resp.status_code = 500
    except:
        pass
    return resp


def parameter_400_error_response():
    message = {
        'status': 400,
        'message': 'Lookup field must be bigger than 3 characters.',
    }

    resp = message
    try:
        resp = jsonify(message)
        resp.status_code = 400
    except:
        pass
    return resp
