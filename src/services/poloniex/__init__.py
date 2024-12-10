import json
from time import time
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
        self.last_update = time()

    def create_temp_arq(self, name, content):
        with open(name, "w") as arq:
            arq.write(json.dumps({
                "time": time(),
                "content": content
            }))

    def load_temp_arq(self, name):
        try:
            with open(name, "r") as arq:
                temp_content = json.loads(arq.read())

            if temp_content and float(temp_content.get("time", 0)) + 300 >= time():
                if self.last_update and float(self.last_update) > float(temp_content.get("time", 0)):
                    self.last_update = float(temp_content.get("time"))

                return temp_content.get("content", [])
        except:
            pass 

        return None

    def get_balance(self):
        temp_file_path = "src/files/temp_poloniex_balance.json"
        
        new_balances = self.load_temp_arq(temp_file_path)

        if new_balances:
            return new_balances, self.last_update

        balances = self.polo.accounts().get_balances()

        new_balances = [
            {
                "asset": asset.get("currency"),
                "amount": float(asset.get("available")) + float(asset.get("hold"))
            } for asset in balances[0].get("balances", [])
        ]

        self.create_temp_arq(temp_file_path, new_balances)

        del balances
        return new_balances, self.last_update       
    
    def get_prices(self):
        temp_file_path = "src/files/temp_poloniex_prices.json"
        
        new_prices = self.load_temp_arq(temp_file_path)

        if new_prices:
            return new_prices

        prices = self.polo.markets().get_prices()
        new_prices = {price.get("symbol"): price.get("price") for price in prices}

        self.create_temp_arq(temp_file_path, new_prices)

        del prices
        return new_prices
