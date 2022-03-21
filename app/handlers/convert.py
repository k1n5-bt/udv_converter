from aiohttp import web
from app.storage.repository import Repository
from app.models.models import CurrencySchema
from marshmallow import ValidationError
from decimal import Decimal, ROUND_HALF_DOWN


async def convert_handler(request: web.Request):
    params = dict(request.query)
    await Repository().connect()

    try:
        conv_schema = CurrencySchema().load(params)
    except ValidationError as e:
        return web.json_response(e.messages, status=400)

    try:
        cur_from = await Repository().get_cur(conv_schema.cur_from)
        cur_to = await Repository().get_cur(conv_schema.cur_to)
    except Exception as e:
        return web.json_response(text=str(e), status=400)
    result = Decimal(conv_schema.amount * cur_from / cur_to).quantize(Decimal("1.00"), ROUND_HALF_DOWN)

    return web.json_response({"Conversion result": f'{result}'}, status=200)
