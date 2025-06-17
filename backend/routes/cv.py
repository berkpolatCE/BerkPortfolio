from flask import Blueprint, jsonify, send_file
from data.portfolio_data import CV_DATA
import os

bp = Blueprint('cv', __name__, url_prefix='/api')

@bp.route('/cv', methods=['GET'])
def get_cv_info():
    """Get CV information"""
    return jsonify({
        'success': True,
        'data': CV_DATA
    })

@bp.route('/cv/download', methods=['GET'])
def download_cv():
    """Download CV file"""
    # In a real application, you would have the actual CV file
    # For now, we'll return a mock response
    return jsonify({
        'success': False,
        'error': 'CV file not yet available. Please add your CV file to the static/files directory.',
        'expected_path': CV_DATA['path']
    }), 404
    
    # When you have the actual file, use this code:
    # cv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), CV_DATA['path'].lstrip('/'))
    # if os.path.exists(cv_path):
    #     return send_file(cv_path, as_attachment=True, download_name=CV_DATA['filename'])
    # else:
    #     return jsonify({
    #         'success': False,
    #         'error': 'CV file not found'
    #     }), 404