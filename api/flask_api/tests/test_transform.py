from flask_api.models.order import Order
from flask_api.order_transformer import OrderTransformer
from flask_api.csv_wrapper import CSVWrapper

import pandas as pd


def test_parse_with_one_log():
    orderOne = Order('53192','JohnWatson','Pizza','False','')
    orders = [orderOne]

    readCSV = CSVWrapper().readCSV("tests/mockdata/one_log_per_order.csv")
    assert orders == OrderTransformer().convertFromCsv(readCSV)