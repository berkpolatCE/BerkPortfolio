from flask import Blueprint, jsonify
from data.portfolio_data import HOME_DATA

bp = Blueprint('home', __name__, url_prefix='/api')

@bp.route('/home', methods=['GET'])
def get_home():
    """Get home/about me information"""
    return jsonify({
        'success': True,
        'data': HOME_DATA
    })