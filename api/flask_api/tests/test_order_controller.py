import json
from flask_api.order_controller import OrderController

def test_order_controller():
    orderController = OrderController("tests/mockdata/multiple_logs_per_order.csv")
    jsonOrders = orderController.get_orders()

    f = open('tests/mockdata/output/result.json')
    mockJson = json.load(f)
    
    assert mockJson == jsonOrders
    assert False