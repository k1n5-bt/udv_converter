# udv_converter
Необходимо разработать back-end, реализующий следующее REST API:
GET /convert?from=RUR&to=USD&amount=42
Перевести amount из валюты from в валюту to
Ответ в Json
POST /database?merge=1

Установить данные по валютам
Если merge == 0, то старые данные инвалидируются
Если merge == 1, то новые данные перетирают старые, но старые все еще акутальны, если не
перетерты
Ответ в Json

Оформление решения:
• Решение необходимо предоставить в виде git репозитория.
• Язык реализации Python 3.7 или выше.
• Фреймворк для реализации - aiohttp 3.6.0 и выше.
• Хранилище данных - Redis.
• Использование дополнительных библиотек на усмотрение разработчика.
• Реализация неописанных явно форматов и протоколов на усмотрение разработчика.
• Плюсом будет наличие тестов и запуск через docker-compose.
