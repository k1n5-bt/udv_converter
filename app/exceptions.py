class CurrencyNotFound(Exception):
    def __str__(self):
        return 'Currency not found'
