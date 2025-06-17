"""
Response helper functions for consistent API responses
"""
from flask import jsonify


def success_response(data=None, message=None, status_code=200):
    """
    Create a standardized success response
    
    Args:
        data: The response data
        message: Optional success message
        status_code: HTTP status code (default 200)
    
    Returns:
        Flask response object
    """
    response = {
        'success': True,
        'data': data
    }
    
    if message:
        response['message'] = message
    
    return jsonify(response), status_code


def error_response(error=None, message=None, status_code=400):
    """
    Create a standardized error response
    
    Args:
        error: Error details
        message: Error message
        status_code: HTTP status code (default 400)
    
    Returns:
        Flask response object
    """
    response = {
        'success': False,
        'error': error or 'An error occurred'
    }
    
    if message:
        response['message'] = message
    
    return jsonify(response), status_code


def not_found_response(resource='Resource'):
    """
    Create a standardized 404 not found response
    
    Args:
        resource: Name of the resource that wasn't found
    
    Returns:
        Flask response object
    """
    return error_response(
        error=f'{resource} not found',
        status_code=404
    )