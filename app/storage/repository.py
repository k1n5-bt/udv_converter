import aioredis
import config
from decimal import Decimal
from app.exceptions import *


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Repository(metaclass=MetaSingleton):
    connection: aioredis.Redis = None

    async def connect(self):
        if not self.connection:
            self.connection = await aioredis.from_url(f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}")
        return self.connection

    async def get_cur(self, cur_name: str):
        if cur_name.upper() == 'RUR':
            return Decimal(1)
        rate: bytes = await self.connection.lindex(cur_name.upper(), -1)
        if rate is not None:
            return Decimal(rate.decode())
        raise CurrencyNotFound

    async def update(self, data: dict, merge: bool):
        if not merge:
            await self.flush()
        for currency, rate in data.items():
            await self.connection.rpush(str(currency).upper(), Decimal(rate))

    async def flush(self):
        await self.connection.flushdb()
