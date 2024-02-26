from flask_api.models.order import Order

class OrderTransformer:

    def convertFromCsv(self, csvData):
        orders = {}
        for i,row in csvData.iterrows():
            id = str(row['Trace ID'])
            abbreviated_name = str(row['First Name'] + row['Last Name'])
            food = str(row['Order'])
            status_type = str(row['Status'])
            status_result = str(row['Success'])

            if (id in orders.keys()):
                order = orders[id]
            else:
                order = Order(id, abbreviated_name, food)
            
            order = self.__processStatuses(order, status_type, status_result)
            orders[id] = order
        listOfOrders = list(orders.values())
        return listOfOrders

    def __processStatuses(self, order, status_type, status_result):
        if status_type == 'Started':
            order.set_started_status(status_result)
        if status_type == 'Processing':
            order.set_processing_status(status_result)

        return order