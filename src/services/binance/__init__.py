import urllib.request
import json
import requests
import hmac
import urllib.parse
import hashlib
from time import time
from dotenv import dotenv_values

class Binance:
    def __init__(self):
        api_key = dotenv_values(".env", ).get("BINANCE_API_KEY")
        secret_key = dotenv_values(".env").get("BINANCE_SECRET_KEY")

        if not api_key or api_key == "api_key":
            raise Exception("Binance Api Key not found! Please verify .env file.")
        
        if not secret_key or api_key == "secret_key":
            raise Exception("Binance Secret Key not found! Please verify .env file.")

        self.headers = {
            'content-type': "application/json",
            'x-mbx-apikey': api_key,
            'cache-control': "no-cache"
        }
        self.secret_key = secret_key
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
        temp_file_path = "src/files/temp_binance_balance.json"
        
        new_balances = self.load_temp_arq(temp_file_path)

        if new_balances:
            return new_balances, self.last_update

        url = "https://api.binance.com/api/v3/account"
        timestamp = int(round((time()-10) * 1000))
        query = {"timestamp":timestamp, "recvWindow":60000}
        encoded_param = urllib.parse.urlencode(query)
        signature = hmac.new(self.secret_key.encode(), msg=encoded_param.encode(), digestmod=hashlib.sha256).hexdigest()
        querystring = {"timestamp":timestamp, "recvWindow":60000, "signature":signature}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        balances = json.loads(response.content)
        new_balances = [
            {
                "asset": asset.get("asset"),
                "amount": float(asset.get("free")) + float(asset.get("locked"))
            } for asset in balances.get("balances", {}) if float(asset.get("free")) != 0.0 or float(asset.get("locked")) != 0.0
        ]

        self.create_temp_arq(temp_file_path, new_balances)

        del balances
        return new_balances, self.last_update

    def get_prices(self):
        temp_file_path = "src/files/temp_binance_prices.json"
        
        new_prices = self.load_temp_arq(temp_file_path)

        if new_prices:
            return new_prices

        url = "https://api.binance.com/api/v3/ticker/price"
        querystring = {}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        prices = json.loads(response.content)
        new_prices = {price.get("symbol"): price.get("price") for price in prices}

        self.create_temp_arq(temp_file_path, new_prices)

        del prices
        return new_prices
