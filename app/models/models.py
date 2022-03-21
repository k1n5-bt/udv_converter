from marshmallow import Schema, fields, validate, post_load


class CurrencyData:
    def __init__(self, cur_from, cur_to, amount):
        self.cur_from = cur_from
        self.cur_to = cur_to
        self.amount = amount


class CurrencySchema(Schema):
    cur_from = fields.String(required=True, data_key='from', validate=validate.Regexp(regex=r'[a-zA-Z]'), attribute='cur_from')
    cur_to = fields.String(required=True, data_key='to', validate=validate.Regexp(regex=r'[a-zA-Z]'), attribute='cur_to')
    amount = fields.Decimal(required=True, data_key='amount', attribute='amount')

    @post_load
    def make_obj(self, data, **kwargs):
        return CurrencyData(**data)
