from flask import Flask, jsonify
from flask_api.models.order import OrderSchema
from flask_api.csv_wrapper import CSVWrapper
from flask_api.order_transformer import OrderTransformer

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    # csv = CSVWrapper.readCSV("tests/mockdata/source.csv")
    csv = CSVWrapper.readCSV("storage/source.csv")
    orders = OrderTransformer.convertFromCsv(csv)
    schema = OrderSchema(many=True)
    ordersTransformed = schema.dump(orders)
    return jsonify(ordersTransformed)