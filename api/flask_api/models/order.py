from marshmallow import Schema, fields

class Order(object):
    def __init__(self, trace_id, abbreviated_name, food_ordered):
        self.trace_id = trace_id
        self.abbreviated_name = abbreviated_name
        self.food_ordered = food_ordered
        self.started_status = ''
        self.processing_status = ''

    def __repr__(self):
        return f'<Order(trace_id={self.trace_id},name={self.abbreviated_name},food={self.food_ordered},started_status={self.started_status},processing_status={self.processing_status})>'

    def __eq__(self, __o: object) -> bool:
        return self.trace_id == __o.trace_id and \
            self.abbreviated_name == __o.abbreviated_name and \
            self.food_ordered == __o.food_ordered and \
            self.started_status == __o.started_status and \
            self.processing_status == __o.processing_status

    def set_started_status(self, started_status):
        self.started_status = started_status
    
    def set_processing_status(self, processing_status):
        self.processing_status = processing_status

class OrderSchema(Schema):
    trace_id = fields.Str()
    abbreviated_name = fields.Str()