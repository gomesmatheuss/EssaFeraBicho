import json
from src.services.binance import Binance
from src.services.poloniex import Poloniex
from src.services.balance.coin import Coin
from datetime import datetime

class Balance:
    def __init__(self):
        self.btc_value = 0
        self.uss_value = 0
        self.brl_value = 0
        self.poloniex_btc_value = 0
        self.poloniex_uss_value = 0
        self.poloniex_brl_value = 0
        self.binance_btc_value = 0
        self.binance_uss_value = 0
        self.binance_brl_value = 0
        self.btcuss_value = 0
        self.ussbrl_value = 0
        self.last_update = str(datetime.now())
        self.coins = []

        self.get_all_balance()

    def get_initial_values(self):
        try:
            with open("src/files/initial_amount.json", "r") as arq:
                values = json.loads(arq.read())
            
            new_values = {}
            for asset in values:
                if asset.get("operation") == "deposit":
                    new_values[asset.get("asset")] = {
                        "balance": asset.get("balance") + new_values.get(asset.get("asset"), {}).get("balance") if new_values.get(asset.get("asset")) else asset.get("balance"),
                        "btc_value": asset.get("btc_value") + new_values.get(asset.get("asset"), {}).get("btc_value") if new_values.get(asset.get("asset")) else asset.get("btc_value"),
                        "uss_value": asset.get("uss_value") + new_values.get(asset.get("asset"), {}).get("uss_value") if new_values.get(asset.get("asset")) else asset.get("uss_value"),
                    }
                else:
                    new_values[asset.get("asset")] = {
                        "balance": new_values.get(asset.get("asset"), {}).get("balance") - asset.get("balance") if new_values.get(asset.get("asset")) else asset.get("balance"),
                        "btc_value": new_values.get(asset.get("asset"), {}).get("btc_value") - asset.get("btc_value") if new_values.get(asset.get("asset")) else asset.get("btc_value"),
                        "uss_value": new_values.get(asset.get("asset"), {}).get("uss_value") - asset.get("uss_value") if new_values.get(asset.get("asset")) else asset.get("uss_value"),
                    }
            return new_values
        except:
            return {}

    def set_btc_value(self, coin, amount, prices):
        symbol = coin + "_USDT"
        symbol2 = coin + "_BTC"

        if price := (prices.get(symbol) or prices.get(symbol.replace("_", ""))):
            uss_value = amount * float(price)
            btc_value = uss_value / self.btcuss_value
            brl_value = uss_value * self.ussbrl_value
            return uss_value, btc_value, brl_value, float(price)

        if price := (prices.get(symbol2) or prices.get(symbol2.replace("_", ""))):
            btc_value = amount * float(price)
            uss_value = btc_value * self.btcuss_value
            brl_value = uss_value * self.ussbrl_value
            return uss_value, btc_value, brl_value, float(price)
        
        if coin == "USDT":
            price = prices.get("TUSDUSDT") if prices.get("TUSDUSDT") else prices.get("TUSD_USDT")
            btc_value = amount * float(price)
            uss_value = amount
            brl_value = uss_value * self.ussbrl_value
            return uss_value, btc_value, brl_value, float(price)
        
        return -1, -1, -1, -1

    def set_values(self, values, prices, exchange, initial_values):
        for asset in values:
            uss_value, btc_value, brl_value, price = self.set_btc_value(asset.get("asset"), asset.get("amount"), prices)

            self.uss_value += uss_value if uss_value > 0 else 0
            self.btc_value += btc_value if btc_value > 0 else 0
            self.brl_value += brl_value if brl_value > 0 else 0
            self.binance_uss_value += uss_value if uss_value > 0 and exchange.lower() == "binance" else 0
            self.binance_btc_value += btc_value if btc_value > 0 and exchange.lower() == "binance" else 0
            self.binance_brl_value += brl_value if brl_value > 0 and exchange.lower() == "binance" else 0
            self.poloniex_uss_value += uss_value if uss_value > 0 and exchange.lower() == "poloniex" else 0
            self.poloniex_btc_value += btc_value if btc_value > 0 and exchange.lower() == "poloniex" else 0
            self.poloniex_brl_value += brl_value if brl_value > 0 and exchange.lower() == "poloniex" else 0

            coin_info = Coin(
                asset = asset.get("asset"),
                amount = asset.get("amount"),
                uss_value = uss_value,
                btc_value = btc_value,
                brl_value = brl_value,
                pol_amount = asset.get("amount") if exchange.lower() == "poloniex" else 0,
                bin_amount = asset.get("amount") if exchange.lower() == "binance" else 0,
                initial_uss_value = initial_values.get(asset.get("asset"), {}).get("uss_value", 0),
                initial_btc_value = initial_values.get(asset.get("asset"), {}).get("btc_value", 0),
                initial_amount = initial_values.get(asset.get("asset"), {}).get("balance", 0),
                price = price
            )
            coin_old = [coin for coin in self.coins if coin.asset == asset.get("asset")]
            if coin_old:
                coin_info.update_values(coin_old[0])
                self.coins.remove(coin_old[0])

            self.coins.append(coin_info)

    def get_all_balance(self):
        binance_balance, bin_last_update = Binance().get_balance()
        binance_prices = Binance().get_prices()
        poloniex_balance, pol_last_update = Poloniex().get_balance()
        poloniex_prices = Poloniex().get_prices()

        initial_values = self.get_initial_values()

        self.btcuss_value = float(binance_prices.get("BTCUSDT"))
        self.ussbrl_value = float(binance_prices.get("USDTBRL"))

        self.last_update = str(datetime.fromtimestamp(bin_last_update)) if bin_last_update < pol_last_update else str(datetime.fromtimestamp(pol_last_update))

        self.set_values(binance_balance, binance_prices, "Binance", initial_values)
        self.set_values(poloniex_balance, poloniex_prices, "Poloniex", initial_values)

        sorted_coins = sorted(self.coins, key=lambda coin: coin.uss_value, reverse=True)
        del self.coins
        self.coins = sorted_coins
        del sorted_coins
