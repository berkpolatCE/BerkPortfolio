from flask import Blueprint, jsonify
from data.portfolio_data import CONTACT_DATA

bp = Blueprint('contact', __name__, url_prefix='/api')

@bp.route('/contact', methods=['GET'])
def get_contact():
    """Get contact information"""
    # You might want to hide sensitive info like phone/email in production
    # and only show social links
    return jsonify({
        'success': True,
        'data': CONTACT_DATA
    })