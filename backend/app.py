import os
import logging
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Import routes using relative imports
from .routes import home, photo, projects, skills, contact
from .utils.responses import success_response, error_response
from .utils.error_handling import log_error

# Load environment variables from backend/.env
# Handle both cases: running from backend/ or project root
backend_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(backend_dir, '.env')
load_dotenv(dotenv_path)

# Configure logging
logging.basicConfig(
    level=logging.INFO if os.getenv('FLASK_ENV') == 'production' else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create Flask app
app = Flask(__name__)

# Configure Flask app
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configure CORS with environment variables
# Default to localhost for development, restrict in production
default_origins = 'http://localhost:3000,http://127.0.0.1:3000'
if os.getenv('FLASK_ENV') == 'production':
    # In production, CORS_ORIGINS must be explicitly set - no wildcard
    cors_origins_str = os.getenv('CORS_ORIGINS')
    if not cors_origins_str:
        raise ValueError("CORS_ORIGINS must be set in production environment")
    cors_origins = [origin.strip() for origin in cors_origins_str.split(',')]
else:
    # Development: allow localhost origins
    cors_origins = [origin.strip() for origin in os.getenv('CORS_ORIGINS', default_origins).split(',')]

CORS(app, origins=cors_origins)

# API version prefix
API_PREFIX = '/api/v1'

# Register blueprints with versioned prefix
app.register_blueprint(home.bp, url_prefix=API_PREFIX)
app.register_blueprint(photo.bp, url_prefix=API_PREFIX)
app.register_blueprint(projects.bp, url_prefix=API_PREFIX)
app.register_blueprint(skills.bp, url_prefix=API_PREFIX)
app.register_blueprint(contact.bp, url_prefix=API_PREFIX)

# Health check endpoint (keeping at /api/health for backward compatibility)
@app.route('/api/health')
def health():
    return success_response(
        data={'status': 'healthy'},
        message='Portfolio API is running'
    )

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return error_response(
        error='The requested resource was not found',
        status_code=404
    )

@app.errorhandler(500)
def internal_error(error):
    return error_response(
        error='Internal server error',
        message='An unexpected error occurred',
        status_code=500
    )

@app.errorhandler(Exception)
def handle_exception(error):
    # Log the error with full details
    log_error(error, context='Unhandled exception')
    return error_response(
        error='An unexpected error occurred',
        message='Please try again later or contact support if the issue persists',
        status_code=500
    )

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(debug=debug, host=host, port=port)
