class CurrencyConverterService:
    def __init__(self, rate_provider):
        self.rate_provider = rate_provider

    def convert(self, source: str, target: str, amount: float) -> float:
        rate = self.rate_provider.get_exchange_rate(source, target)
        return amount * rate
    def exchange_rate_keys(self) -> list:
        keys = self.rate_provider.get_exchange_rate_keys()
        return keys
