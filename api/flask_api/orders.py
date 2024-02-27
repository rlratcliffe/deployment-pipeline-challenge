from flask import Flask, jsonify, make_response
from flask_api.order_controller import OrderController

app = Flask(__name__)

orderController = OrderController("storage/source.csv")

@app.route("/orders")
def get_orders():
        response = make_response(
            jsonify(orderController.get_orders())
        )
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response