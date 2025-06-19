from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response

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
        return error_response(
            error=str(e),
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
        return error_response(
            error=str(e),
            status_code=500
        )
