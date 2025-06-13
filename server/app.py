from server import create_app

app = create_app()

@app.route('/')
def home():
    return { "message": "Pizza API is running!" }


if __name__ == "__main__":
    app.run(debug=True)
