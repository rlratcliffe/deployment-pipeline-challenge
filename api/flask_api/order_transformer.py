import pandas as pd
from flask_api.models.order import Order

class OrderTransformer:

    def convertFromCsv(self, csvData):
        orders = []
        for i,row in csvData.iterrows():
            id = str(row['Trace ID'])
            abbreviated_name = str(row['First Name'] + row['Last Name'])
            food = str(row['Order'])
            started_status, processing_status = self.__processStatus(str(row['Status']), str(row['Success']))
            order = Order(id, abbreviated_name, food, started_status, processing_status)
            orders.append(order)
        return orders

    def __processStatus(self, status_type, status):
        started_status = ''
        processing_status = ''
        if status_type == 'Started':
            started_status = status
        
        return started_status, processing_status