from flask import Blueprint
from ..data.portfolio_data import PORTFOLIO_DATA
from ..utils.responses import success_response, error_response, not_found_response

bp = Blueprint('cv', __name__)

@bp.route('/cv', methods=['GET'])
def get_cv_info():
    """Get CV information"""
    try:
        return success_response(data=PORTFOLIO_DATA["cv"])
    except KeyError:
        return error_response(
            error='CV data not found',
            status_code=500
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )

@bp.route('/cv/download', methods=['GET'])
def download_cv():
    """Download CV file"""
    try:
        # In a real application, you would have the actual CV file
        # For now, we'll return a mock response
        cv_data = PORTFOLIO_DATA["cv"]
        return error_response(
            error='CV file not yet available',
            message=f'Please add your CV file to the static/files directory. Expected path: {cv_data["url"]}',
            status_code=404
        )
        
        # When you have the actual file, use this code:
        # from flask import send_file
        # import os
        # cv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), cv_data['url'].lstrip('/'))
        # if os.path.exists(cv_path):
        #     return send_file(cv_path, as_attachment=True, download_name=cv_data['filename'])
        # else:
        #     return not_found_response('CV file')
    except KeyError:
        return error_response(
            error='CV data not found',
            status_code=500
        )
    except Exception as e:
        return error_response(
            error=str(e),
            status_code=500
        )