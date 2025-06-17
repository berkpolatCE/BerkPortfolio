# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a portfolio website with a Flask backend (Python). The backend provides REST API endpoints with hardcoded portfolio data. The frontend is pending redesign and implementation.

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
python run.py

# The API will be available at http://localhost:5000
```

### Frontend Development
```bash
# Frontend is pending redesign and implementation
# Commands will be added once the new frontend framework is chosen
```

### API Testing
```bash
# Test endpoints (from project root)
curl http://localhost:5000/api/health
curl http://localhost:5000/api/v1/home
curl http://localhost:5000/api/v1/projects
curl http://localhost:5000/api/v1/skills
```

## Architecture

### Backend Structure
- `run.py`: Entry point script to run the Flask application
- `app.py`: Main Flask application with CORS configuration and error handlers
- `routes/`: Modular API endpoints organized by feature
  - Each route module uses Flask Blueprints for clean separation
  - All routes versioned under `/api/v1`
- `data/portfolio_data.py`: Centralized hardcoded data store (single source of truth)
  - All portfolio content is maintained in one `PORTFOLIO_DATA` dictionary
- `utils/`: Helper functions and utilities
  - `responses.py`: Standardized API response functions

### Frontend Structure
- **Pending redesign**: Frontend framework and architecture to be determined
- Will consume the Flask backend REST APIs
- Expected to include:
  - Homepage with hero section and about information
  - Projects gallery/grid with detail pages
  - Skills visualization
  - Contact information
  - Responsive design for all devices

### API Endpoints
All API endpoints (except health check) are now versioned under `/api/v1`:

- `GET /api/health` - Health check (kept at /api for backward compatibility)
- `GET /api/v1/home` - About me information
- `GET /api/v1/photo` - Photo gallery data  
- `GET /api/v1/projects` - All projects (supports ?featured=true filter)
- `GET /api/v1/projects/<id>` - Specific project details
- `GET /api/v1/skills` - All skills
- `GET /api/v1/skills/<category>` - Skills by category (technical/soft)
- `GET /api/v1/cv` - CV information
- `GET /api/v1/cv/download` - Download CV file
- `GET /api/v1/contact` - Contact information and social links

### Key Design Decisions
1. **Blueprint Architecture**: Each feature has its own route module using Flask Blueprints for modularity
2. **CORS Enabled**: Flask-CORS configured globally to allow frontend communication
3. **Consistent Response Format**: All endpoints use standardized response functions for consistency
4. **Error Handling**: Global error handlers and try-catch blocks in all routes
5. **API Versioning**: All endpoints versioned under `/api/v1` for future compatibility
6. **Single Data Source**: All content in one `PORTFOLIO_DATA` dictionary for easy management
7. **Proper Package Structure**: Backend is a proper Python package with `__init__.py` files
8. **Frontend Pending**: New frontend architecture to be designed and implemented

## Development Notes

- The backend runs on port 5000 by default
- Frontend port configuration pending (typically 3000 or 5173)
- Debug mode is enabled in development
- Static files (images, CV) should be placed in `backend/static/` directory when added
- Update data in `data/portfolio_data.py` to customize portfolio content
- Frontend will connect to backend API at `http://localhost:5000/api/v1`

## Important File References

- Backend entry: `backend/run.py`
- Portfolio data: `backend/data/portfolio_data.py`
- Frontend entry: `frontend/pages/index.vue`
- Frontend configuration: `frontend/nuxt.config.ts`

## Frontend Features

- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Smooth Animations**: GSAP integration for page transitions and scroll effects
- **API Integration**: Seamless connection to Flask backend via composables
- **Dynamic Routing**: Auto-generated routes for project detail pages
- **SEO Ready**: Server-side rendering with Nuxt 3
- **Modern Typography**: Google Fonts (Inter & Space Grotesk)
- **Component-Based**: Reusable Vue components for maintainability