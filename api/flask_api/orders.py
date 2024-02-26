from flask import Flask, jsonify
from flask_api.order_controller import OrderController

app = Flask(__name__)

orderController = OrderController("storage/source.csv")

@app.route("/orders")
def get_orders():
    return jsonify(orderController.get_orders())