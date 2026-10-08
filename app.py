import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]

@app.route("/")
def home():
    return '<h1>Payer POC</h1><a href="/login">Connect my Medicare data</a>'

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)