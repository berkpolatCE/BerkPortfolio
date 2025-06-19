from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response
from ..utils.error_handling import log_error, get_safe_error_message

bp = Blueprint('skills', __name__)

@bp.route('/skills', methods=['GET'])
def get_skills():
    """Get all skills data"""
    try:
        return success_response(data=PORTFOLIO_DATA["skills"])
    except KeyError:
        return error_response(
            error='Skills data not found',
            status_code=404
        )
    except Exception as e:
        log_error(e, context='Error retrieving skills data')
        return error_response(
            error=get_safe_error_message(e),
            message='Unable to load skills information',
            status_code=500
        )

@bp.route('/skills/<category>', methods=['GET'])
def get_skills_by_category(category):
    """Get skills by category (technical or soft)"""
    try:
        skills = PORTFOLIO_DATA["skills"]
        
        if category in ['technical', 'soft']:
            return success_response(data=skills.get(category, []))
        else:
            return error_response(
                error='Invalid category. Use "technical" or "soft"',
                status_code=400
            )
    except KeyError:
        return error_response(
            error='Skills data not found',
            status_code=404
        )
    except Exception as e:
        log_error(e, context='Error retrieving skills by category')
        return error_response(
            error=get_safe_error_message(e),
            message='Unable to load skills for the requested category',
            status_code=500
        )
