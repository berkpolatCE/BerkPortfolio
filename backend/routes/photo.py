from flask import Blueprint, jsonify
from data.portfolio_data import PHOTO_DATA

bp = Blueprint('photo', __name__, url_prefix='/api')

@bp.route('/photo', methods=['GET'])
def get_photos():
    """Get photo gallery data"""
    return jsonify({
        'success': True,
        'data': PHOTO_DATA
    })