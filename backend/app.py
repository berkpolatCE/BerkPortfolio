from flask import Flask
from flask_cors import CORS

# Import routes using relative imports
from .routes import home, photo, projects, skills, cv, contact
from .utils.responses import success_response, error_response

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# API version prefix
API_PREFIX = '/api/v1'

# Register blueprints with versioned prefix
app.register_blueprint(home.bp, url_prefix=API_PREFIX)
app.register_blueprint(photo.bp, url_prefix=API_PREFIX)
app.register_blueprint(projects.bp, url_prefix=API_PREFIX)
app.register_blueprint(skills.bp, url_prefix=API_PREFIX)
app.register_blueprint(cv.bp, url_prefix=API_PREFIX)
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
    # Log the error in production
    app.logger.error(f'Unhandled exception: {str(error)}')
    return error_response(
        error='An unexpected error occurred',
        status_code=500
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)