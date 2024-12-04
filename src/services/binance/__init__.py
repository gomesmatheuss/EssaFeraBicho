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

    def get_balance(self):
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

        del balances
        return new_balances

    def get_prices(self):
        url = "https://api.binance.com/api/v3/ticker/price"
        querystring = {}
        response = requests.request("GET", url, headers=self.headers, params=querystring)

        prices = json.loads(response.content)
        new_prices = {price.get("symbol"): price.get("price") for price in prices}

        del prices
        return new_prices
