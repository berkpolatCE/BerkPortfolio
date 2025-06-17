# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a portfolio website with a Flask backend (Python) and Nuxt.js frontend. The backend provides REST API endpoints with hardcoded portfolio data, while the frontend will consume these APIs to display the portfolio content.

## Commands

### Backend Development
```bash
# Navigate to backend directory
cd backend

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run Flask development server
python app.py

# The API will be available at http://localhost:5000
```

### API Testing
```bash
# Test endpoints (from project root)
curl http://localhost:5000/api/health
curl http://localhost:5000/api/home
curl http://localhost:5000/api/projects
curl http://localhost:5000/api/skills
```

## Architecture

### Backend Structure
- `app.py`: Main Flask application entry point with CORS configuration
- `routes/`: Modular API endpoints organized by feature
  - Each route module uses Flask Blueprints for clean separation
  - All routes prefixed with `/api`
- `data/portfolio_data.py`: Centralized hardcoded data store
  - All portfolio content is maintained here for easy updates

### API Endpoints
- `GET /api/health` - Health check
- `GET /api/home` - About me information
- `GET /api/photo` - Photo gallery data  
- `GET /api/projects` - All projects (supports ?featured=true filter)
- `GET /api/projects/<id>` - Specific project details
- `GET /api/skills` - All skills
- `GET /api/skills/<category>` - Skills by category (technical/soft)
- `GET /api/cv` - CV information
- `GET /api/cv/download` - Download CV file
- `GET /api/contact` - Contact information and social links

### Key Design Decisions
1. **Blueprint Architecture**: Each feature has its own route module using Flask Blueprints for modularity
2. **CORS Enabled**: Flask-CORS configured globally to allow frontend communication
3. **Consistent Response Format**: All endpoints return JSON with `success` flag and `data`/`error` fields
4. **Hardcoded Data**: All content in `portfolio_data.py` for easy customization without database setup

## Development Notes

- The backend runs on port 5000 by default
- Debug mode is enabled in development
- Static files (images, CV) should be placed in `backend/static/` directory when added
- Update data in `data/portfolio_data.py` to customize portfolio content