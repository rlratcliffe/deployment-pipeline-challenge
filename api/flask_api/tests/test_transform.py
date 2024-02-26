from flask_api.models.order import Order
from flask_api.order_transformer import OrderTransformer
from flask_api.csv_wrapper import CSVWrapper

def test_parse_with_one_log():
    mockOrder = Order('53192','JohnWatson','Pizza')
    mockOrder.set_started_status('False')
    orders = [mockOrder]

    readCSV = CSVWrapper().readCSV("tests/mockdata/one_log_per_order.csv")
    assert orders == OrderTransformer().convertFromCsv(readCSV)

def test_parse_with_multiple_logs():
    mockOrder = Order('23404','SherlockHolmes', 'Pie')
    mockOrder.set_started_status('True')
    mockOrder.set_processing_status('False')
    orders = [mockOrder]

    readCSV = CSVWrapper().readCSV("tests/mockdata/multiple_logs_per_order.csv")
    assert orders == OrderTransformer().convertFromCsv(readCSV)