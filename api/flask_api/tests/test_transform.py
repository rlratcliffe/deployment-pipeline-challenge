from flask_api.models.order import Order
from flask_api.order_transformer import OrderTransformer
from flask_api.csv_wrapper import CSVWrapper

import pandas as pd


def test_parsecsv():
    orderOne = Order('53192','JohnWatson')
    orders = [orderOne]

    readCSV = CSVWrapper.readCSV("tests/mockdata/source.csv")
    assert orders == OrderTransformer.convertFromCsv(readCSV)