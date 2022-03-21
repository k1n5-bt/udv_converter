from aiohttp import web
import json
from app.storage.repository import Repository


async def database_handler(request: web.Request):
    body: bytes = await request.content.read()
    data = json.loads(body)
    if 'merge' not in request.query.keys():
        return web.json_response(text='The merge parameter is missing', status=400)
    await Repository().connect()
    await Repository().update(data=data, merge=bool(int(request.query['merge'])))
    return web.json_response(text='The currency exchange rate has been updated')
