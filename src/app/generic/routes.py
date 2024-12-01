from flask import jsonify
from . import blueprint


@blueprint.app_errorhandler(404)
def error404(error):
    '''Handle 404 errors by returning a JSON response.

    This function is triggered when a requested URL is not found.
    
    Args:
        error: The error object containing details about the 404 error.

    Returns:
        tuple: A JSON response with error details and a 404 status code.
    '''
    response = {
        'error': 'Not Found 404', 
        'message': 'The requested URL was not found on the server.'
    }
    return jsonify(response), 404