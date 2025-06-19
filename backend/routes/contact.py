from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response
from ..utils.error_handling import log_error, get_safe_error_message

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
        log_error(e, context='Error fetching contact information')
        return error_response(
            error=get_safe_error_message(e),
            message='Unable to retrieve contact information at this time',
            status_code=500
        )
