from flask import Blueprint, jsonify, request
from server import db
from server.models.restaurant_pizza import RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        rp = RestaurantPizza(
            price=data['price'],
            restaurant_id=data['restaurant_id'],
            pizza_id=data['pizza_id']
        )
        db.session.add(rp)
        db.session.commit()
        return jsonify(rp.to_dict(include_relations=True)), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
