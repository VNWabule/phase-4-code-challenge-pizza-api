from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    return jsonify([p.to_dict() for p in Pizza.query.all()])
