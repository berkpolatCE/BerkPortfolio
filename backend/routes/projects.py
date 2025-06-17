from flask import Blueprint, request
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response, not_found_response

bp = Blueprint('projects', __name__)

@bp.route('/projects', methods=['GET'])
def get_projects():
    """Get all projects or filter by featured"""
    try:
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        projects = PORTFOLIO_DATA["projects"]
        
        if featured_only:
            projects = [p for p in projects if p.get('featured', False)]
        
        return success_response(
            data={
                'projects': projects,
                'count': len(projects)
            }
        )
    except KeyError:
        return error_response(
            error='Projects data not found',
            status_code=404
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )

@bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get a specific project by ID"""
    try:
        project = next((p for p in PORTFOLIO_DATA["projects"] if p['id'] == project_id), None)
        
        if project:
            return success_response(data=project)
        else:
            return not_found_response('Project')
    except KeyError:
        return error_response(
            error='Projects data not found',
            status_code=404
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )