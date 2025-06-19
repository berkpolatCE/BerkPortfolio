"""
Error handling utilities for safe error responses
"""
import logging
import os
from functools import wraps
from .responses import error_response

# Configure logging
logger = logging.getLogger(__name__)


def safe_error_handler(func):
    """
    Decorator to handle exceptions safely without exposing sensitive information
    
    Args:
        func: The route function to decorate
    
    Returns:
        Wrapped function with safe error handling
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log the actual error for debugging
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            
            # Return generic error message to client
            return error_response(
                error='An internal server error occurred',
                message='Please try again later or contact support if the issue persists',
                status_code=500
            )
    
    return wrapper


def log_error(error, context=None):
    """
    Log an error with optional context
    
    Args:
        error: The exception or error message
        context: Optional context information
    """
    if context:
        logger.error(f"{context}: {str(error)}", exc_info=isinstance(error, Exception))
    else:
        logger.error(str(error), exc_info=isinstance(error, Exception))


def get_safe_error_message(error):
    """
    Get a safe error message based on the error type
    
    Args:
        error: The exception
    
    Returns:
        A safe error message string
    """
    # In development mode, we might want to see more details
    if os.getenv('FLASK_ENV') == 'development' and os.getenv('FLASK_DEBUG', 'False').lower() == 'true':
        return f"Development error: {type(error).__name__}"
    
    # Map specific exceptions to safe messages
    error_map = {
        FileNotFoundError: 'The requested resource could not be found',
        ValueError: 'Invalid input provided',
        KeyError: 'Required data is missing',
        TypeError: 'Invalid data type provided',
        ConnectionError: 'Service temporarily unavailable',
        TimeoutError: 'Request timed out',
    }
    
    # Return mapped message or generic message
    for error_type, message in error_map.items():
        if isinstance(error, error_type):
            return message
    
    return 'An internal server error occurred'