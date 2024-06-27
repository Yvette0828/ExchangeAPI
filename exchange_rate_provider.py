from abc import ABC, abstractmethod

# Define an abstract base class for exchange rate providers
class ExchangeRateProvider(ABC):
    @abstractmethod
    def get_exchange_rate(self, source: str, target: str) -> float:
        """
        Abstract method to get the exchange rate between two currencies.
        """
        pass

# Define static exchange rates
EXCHANGE_RATES = {
    "currencies": {
        "TWD": {
            "TWD": 1,
            "JPY": 3.669,
            "USD": 0.03281
        },
        "JPY": {
            "TWD": 0.26956,
            "JPY": 1,
            "USD": 0.00885
        },
        "USD": {
            "TWD": 30.444,
            "JPY": 111.801,
            "USD": 1
        }
    }
}

# Define a static exchange rate provider that implements the ExchangeRateProvider interface
class StaticExchangeRateProvider(ExchangeRateProvider):
    def __init__(self, rates):
        """
        Initialize the provider with predefined exchange rates.
        """
        self.rates = rates

    def get_exchange_rate(self, source: str, target: str) -> float:
        """
        Get the exchange rate between two specified currencies.
        """
        return self.rates["currencies"][source][target]

    def get_exchange_rate_keys(self) -> list:
        """
        Get a list of available currency codes.
        """
        return list(self.rates["currencies"].keys())
