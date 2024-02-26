import pandas as pd
from flask_api.models.order import Order

class OrderTransformer():

    def convertFromCsv(csvData):
        orders = []
        for i,row in csvData.iterrows():
            id = str(row['Trace ID'])
            abbreviated_name = str(row['First Name'] + row['Last Name'])
            order = Order(id, abbreviated_name)
            orders.append(order)
        return orders