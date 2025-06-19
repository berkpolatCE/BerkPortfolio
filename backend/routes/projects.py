from flask import Blueprint, request
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response, not_found_response
from ..utils.error_handling import log_error, get_safe_error_message

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
        log_error(e, context='Error retrieving projects list')
        return error_response(
            error=get_safe_error_message(e),
            message='Unable to load projects',
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
        log_error(e, context='Error retrieving specific project')
        return error_response(
            error=get_safe_error_message(e),
            message='Unable to load project details',
            status_code=500
        )
