import flet as ft

class ExchangeText(ft.Text):
    def __init__(self, text):
        super().__init__()
        self.value = text
        self.expand = 1 if text in ["Poloniex:", "Binance:", "Total:"] else 2
        self.color = ft.colors.WHITE
        self.no_wrap = True
        self.size = 15

class Exchange(ft.Row):
    def __init__(self, texts=[]):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.START
        self.controls = [
            ExchangeText(text)
            for text in texts
        ]

class Overview(ft.Column):
    def __init__(self, balance):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.horizontal_alignment = ft.CrossAxisAlignment.START
        self.controls = [
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
