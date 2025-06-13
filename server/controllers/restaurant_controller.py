from flask import Blueprint, jsonify, request
from server import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    return jsonify([r.to_dict() for r in Restaurant.query.all()])

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(r.to_dict(include_pizzas=True))

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    r = Restaurant.query.get(id)
    if not r:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(r)
    db.session.commit()
    return '', 204
