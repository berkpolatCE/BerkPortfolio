from flask import Blueprint, jsonify
from data.portfolio_data import SKILLS_DATA

bp = Blueprint('skills', __name__, url_prefix='/api')

@bp.route('/skills', methods=['GET'])
def get_skills():
    """Get all skills data"""
    return jsonify({
        'success': True,
        'data': SKILLS_DATA
    })

@bp.route('/skills/<category>', methods=['GET'])
def get_skills_by_category(category):
    """Get skills by category (technical or soft)"""
    if category in ['technical', 'soft']:
        return jsonify({
            'success': True,
            'data': SKILLS_DATA.get(category, [])
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Invalid category. Use "technical" or "soft"'
        }), 400