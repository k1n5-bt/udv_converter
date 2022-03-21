from aiohttp import web
from app.handlers.convert import convert_handler
from app.handlers.database import database_handler


def setup_routes(app: web.Application):
    routes = [web.get('/convert', convert_handler),
              web.post('/database', database_handler)]
    app.add_routes(routes=routes)
