from marshmallow import Schema, fields

class Order(object):
    # food_ordered, started_status, processing_status
    def __init__(self, trace_id, abbreviated_name):
        self.trace_id = trace_id
        self.abbreviated_name = abbreviated_name

    def __repr__(self):
        return f'<Order(trace_id={self.trace_id},name={self.abbreviated_name})>'

    def __eq__(self, __o: object) -> bool:
        return self.trace_id == __o.trace_id and self.abbreviated_name == __o.abbreviated_name

class OrderSchema(Schema):
    trace_id = fields.Str()
    abbreviated_name = fields.Str()