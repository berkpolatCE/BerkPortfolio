from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response

bp = Blueprint('photo', __name__)

@bp.route('/photo', methods=['GET'])
def get_photos():
    """Get photo gallery data"""
    try:
        return success_response(data=PORTFOLIO_DATA["photo"])
    except KeyError:
        return error_response(
            error='Photo data not found',
            status_code=404
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )
