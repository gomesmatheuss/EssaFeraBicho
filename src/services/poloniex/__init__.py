from src.services.poloniex.polosdk import RestClient
from dotenv import dotenv_values

class Poloniex:
    def __init__(self):
        api_key = dotenv_values(".env").get("POLONIEX_API_KEY")
        secret_key = dotenv_values(".env").get("POLONIEX_SECRET_KEY")

        if not api_key or api_key == "api_key":
            raise Exception("Poloniex Api Key not found! Please verify .env file.")
        
        if not secret_key or api_key == "secret_key":
            raise Exception("Poloniex Secret Key not found! Please verify .env file.")
        
        self.polo = RestClient(api_key, secret_key)

    def get_balance(self):
        balances = self.polo.accounts().get_balances()

        new_balances = [
            {
                "asset": asset.get("currency"),
                "amount": float(asset.get("available")) + float(asset.get("hold"))
            } for asset in balances[0].get("balances", [])
        ]

        del balances
        return new_balances
        
    
    def get_prices(self):
        prices = self.polo.markets().get_prices()
        new_prices = {price.get("symbol"): price.get("price") for price in prices}

        del prices
        return new_prices
