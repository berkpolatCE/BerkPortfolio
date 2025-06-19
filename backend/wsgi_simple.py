"""
Simple WSGI entry point for running from backend directory
"""
import os
import sys

# Get the current directory (backend)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add both current and parent directories to Python path
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.dirname(current_dir))

# Try to import the app - this should work with the fixed imports
try:
    from app import app
except ImportError:
    # Fallback to absolute import
    from backend.app import app

if __name__ == "__main__":
    app.run()