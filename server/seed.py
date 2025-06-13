from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Elm St")

    p1 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p2 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
