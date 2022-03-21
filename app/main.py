from aiohttp.web import Application
from aiohttp import web
from app.routes import setup_routes
import config as cfg
import logging


def init_app():
    logging.log(cfg.LOGGER_LEVEL, f"App: {cfg.HOST=}, {cfg.PORT=}")
    logging.log(cfg.LOGGER_LEVEL, "Running...")
    app = Application()
    setup_routes(app)
    return app


def main():
    logging.basicConfig(level=cfg.LOGGER_LEVEL)
    app = init_app()
    web.run_app(app, host=cfg.HOST, port=cfg.PORT)


if __name__ == "__main__":
    main()
