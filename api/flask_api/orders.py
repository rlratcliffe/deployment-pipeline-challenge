from flask import Flask, jsonify
from .order import Order, OrderSchema

app = Flask(__name__)

orders = []

@app.route("/")
def get_orders():
    schema = OrderSchema(many=True)
    ordersTransformed = schema.dump(orders)
    return jsonify(ordersTransformed)