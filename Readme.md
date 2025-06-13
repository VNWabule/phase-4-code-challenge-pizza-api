# 🍕 Pizza Restaurant API

This is a RESTful API for a pizza restaurant, built with Flask and SQLAlchemy. It allows users to view pizzas, restaurants, and create restaurant-pizza associations with pricing.

---

## 🔧 Technologies Used

- Python 3.8+
- Flask
- SQLAlchemy
- SQLite (default database)

---

## 🚀 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone git@github.com:VNWabule/phase-4-code-challenge-pizza-api.git
   cd phase-4-code-challenge-pizza-api

2. **Create and activate a virtual environment**
    ```bash
    pipenv install
    pipenv shell

3. **Install dependencies**
    ```bash
    pipenv install flask flask_sqlalchemy flask_migrate

4. **Set up the database**
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

5. **Run the flask app**
    ```bash
    flask run

---

## 📚 API Endpoints

1. **GET /pizzas**
    Returns a list of all pizzas
    Response:
    ```json
    [
        {
            "id": 1,
            "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni",
            "name": "Pepperoni"
        },
        {
            "id": 2,
            "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil",
            "name": "Margherita"
        }
    ]

2. **GET /restaurants**
    Returns a list of restaurants
    Response:
    ```json
    [
        {
            "address": "123 Main St",
            "id": 1,
            "name": "Mario's Pizza"
        },
        {
            "address": "456 Elm St",
            "id": 2,
            "name": "Luigi's Pizza"
        }
    ]

3. **GET /restaurants/<int:id>**
    Returns a single restaurant and the pizzas it offers.
    Response:
    ```json
    {
        "address": "123 Main St",
        "id": 1,
        "name": "Mario's Pizza",
        "pizzas": [
            {
                "id": 1,
                "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni",
                "name": "Pepperoni"
            },
            {
                "id": 2,
                "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil",
                "name": "Margherita"
            }
        ]
    }

4. **POST /restaurant_pizzas**
    Creates a new-pizza association with a price
    Request body:
    ```json
    {
     "price": 15,
     "pizza_id": 1,
     "restaurant_id": 2
    }

5. **Validations:**
- price must be between 1 and 30
- pizza_id and restaurant_id must be valid

6. **Successful Response (201):**
    ```json
    {
     "id": 1,
     "name": "Margherita",
     "ingredients": "Cheese, Tomato"
    }

7. **Error Response (400):**
    ```json
    {
    "errors": ["Price must be between 1 and 30"]
    }

---

## 🧪 Testing the API
You can test endpoints using:
- Postman for POST requests
- Your browser or Postman for GET requests



