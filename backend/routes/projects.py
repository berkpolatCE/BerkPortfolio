from flask import Blueprint, jsonify, request
from data.portfolio_data import PROJECTS_DATA

bp = Blueprint('projects', __name__, url_prefix='/api')

@bp.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects or filter by featured"""
    featured_only = request.args.get('featured', 'false').lower() == 'true'
    
    if featured_only:
        projects = [p for p in PROJECTS_DATA if p.get('featured', False)]
    else:
        projects = PROJECTS_DATA
    
    return jsonify({
        'success': True,
        'data': projects,
        'count': len(projects)
    })

@bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get a specific project by ID"""
    project = next((p for p in PROJECTS_DATA if p['id'] == project_id), None)
    
    if project:
        return jsonify({
            'success': True,
            'data': project
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Project not found'
        }), 404