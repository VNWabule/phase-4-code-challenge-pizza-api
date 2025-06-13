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

## 🧪 Testing the API
You can test endpoints using:
- Postman for POST requests
- Your browser or Postman for GET requests



