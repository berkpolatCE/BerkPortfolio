"""
WSGI entry point for Gunicorn production server
"""
import os
import sys

# Add the parent directory to Python path to handle imports correctly
backend_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(backend_dir)
sys.path.insert(0, parent_dir)

from backend.app import app

if __name__ == "__main__":
    app.run()