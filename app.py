# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    config_value = os.getenv("CONFIG_VALUE", "Default Config")
    return f"<h1>Flask App with Config: {config_value}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)