from flask_api.models.order import OrderSchema
from flask_api.csv_wrapper import CSVWrapper
from flask_api.order_transformer import OrderTransformer

class OrderController:
    def __init__(self, dbLocation) -> None:
        self.db = CSVWrapper().readCSV(dbLocation)

    def get_orders(self):
        csv = self.db
        orders = OrderTransformer().convertFromCsv(csv)
        schema = OrderSchema(many=True)
        ordersTransformed = schema.dump(orders)
        return ordersTransformed