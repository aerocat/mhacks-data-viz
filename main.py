from flask import Flask, render_template, request, jsonify
import get_vols
import time
import json

app = Flask(__name__)

@app.route('/get-vols')
def get_volumes():
    volumes = get_vols.get_volumes()
    dictionary = {
        "name": "init",
        "value": 42,
        "children": [
        {
          "name": "ETH-EUR",
          "value": volumes["ETH-EUR"]
        },
        {
          "name": "BTC-EUR",
          "value": volumes["BTC-EUR"]
        },
        {
          "name": "ETH-BTC",
          "value": volumes["ETH-BTC"]
        },
        {
          "name": "BTC-USD",
          "value": volumes["BTC-USD"]
        },
        {
          "name": "LTC-EUR",
          "value": volumes["LTC-EUR"]
        },
        {
          "name": "ETH-USD",
          "value": volumes["ETH-USD"]
         },
         {
           "name": "LTC-USD",
           "value": volumes["LTC-USD"]
           }
         ]
        }
    data = json.dumps(dictionary)
    return jsonify(data)

@app.route('/')
def index():
    #data = get_volumes()
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
