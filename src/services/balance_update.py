import flet as ft
from src.services.balance import Balance
from src.components.items_list import ItemsExpansion
from src.components.overview import Exchange

class BalanceUpdate:
    def __init__(self, page: ft.Page):
        balance = Balance()

        page.overview.controls = [
            Exchange([
                "Poloniex:",
                f"{balance.poloniex_btc_value:.08f} BTC",
                f"US$ {balance.poloniex_uss_value:.02f}",
                f"R$ {balance.poloniex_brl_value:.02f}"
            ]),
            Exchange([
                "Binance:",
                f"{balance.binance_btc_value:.08f} BTC",
                f"US$ {balance.binance_uss_value:.02f}",
                f"R$ {balance.binance_brl_value:.02f}"
            ]),
            Exchange([
                "Total:",
                f"{balance.btc_value:.08f} BTC",
                f"US$ {balance.uss_value:.02f}",
                f"R$ {balance.brl_value:.02f}"
            ])
        ]

        page.items_list.controls = [
            ItemsExpansion(asset, count)
            for count, asset in enumerate(balance.coins)
        ]

        page.update()
