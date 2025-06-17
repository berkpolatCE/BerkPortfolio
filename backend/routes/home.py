from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response

bp = Blueprint('home', __name__)

@bp.route('/home', methods=['GET'])
def get_home():
    """Get home/about me information"""
    try:
        return success_response(data=PORTFOLIO_DATA["home"])
    except KeyError:
        return error_response(
            error='Home data not found',
            status_code=404
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )