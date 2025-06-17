from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response

bp = Blueprint('contact', __name__)

@bp.route('/contact', methods=['GET'])
def get_contact():
    """Get contact information"""
    try:
        # You might want to hide sensitive info like phone/email in production
        # and only show social links
        return success_response(data=PORTFOLIO_DATA["contact"])
    except KeyError:
        return error_response(
            error='Contact data not found',
            status_code=404
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )