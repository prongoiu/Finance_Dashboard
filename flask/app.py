from flask import Flask
from flask import request
from flask import jsonify
import yfinance as yf

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello world!"

@app.route("/api/<name>", methods=['GET'])
def api(name:str):
    ticker = yf.Ticker("name")
    return jsonify(ticker.info)

