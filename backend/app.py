from flask import Flask
from flask_cors import CORS

# Import routes
from routes import home, photo, projects, skills, cv, contact

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Register blueprints
app.register_blueprint(home.bp)
app.register_blueprint(photo.bp)
app.register_blueprint(projects.bp)
app.register_blueprint(skills.bp)
app.register_blueprint(cv.bp)
app.register_blueprint(contact.bp)

# Health check endpoint
@app.route('/api/health')
def health():
    return {'status': 'healthy', 'message': 'Portfolio API is running'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)