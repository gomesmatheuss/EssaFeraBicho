import flet as ft
from src.services.utils import TwoLineText

class Overview(ft.ExpansionTile):
    def __init__(self, balance):
        super().__init__("")
        self.initially_expanded = False
        self.collapsed_text_color = ft.Colors.WHITE
        self.min_tile_height = 1
        self.update_content(balance)

    def update_content(self, balance):
        self.title = ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls = [
                TwoLineText("Total - BTC", f"{balance.btc_value:,.08f}"),
                TwoLineText("Total - USD", f"{balance.uss_value:,.02f}"),
                TwoLineText("Total - R$", f"{balance.brl_value:,.02f}"),
                TwoLineText("Updated", f"{balance.last_update[11:19]}")
            ]
        )
        self.controls = [
            ft.ListTile(
                min_vertical_padding = 5,
                min_height = 1,
                dense = True,
                trailing = ft.Icon(None),
                bgcolor = ft.Colors.ON_SECONDARY,
                title = ft.Row(
                    controls = [
                        TwoLineText("Poloniex - BTC", f"{balance.poloniex_btc_value:,.08f}"),
                        TwoLineText("Poloniex - USD", f"{balance.poloniex_uss_value:,.02f}"),
                        TwoLineText("Poloniex - R$", f"{balance.poloniex_brl_value:,.02f}"),
                        TwoLineText("", "")
                    ]
                )
            ),
            ft.ListTile(
                min_vertical_padding = 5,
                min_height = 1,
                dense = True,
                trailing = ft.Icon(None),
                bgcolor = ft.Colors.ON_SECONDARY,
                title = ft.Row(
                    controls = [
                        TwoLineText("Binance - BTC", f"{balance.binance_btc_value:,.08f}"),
                        TwoLineText("Binance - USD", f"{balance.binance_uss_value:,.02f}"),
                        TwoLineText("Binance - R$", f"{balance.binance_brl_value:,.02f}"),
                        TwoLineText("", "")
                    ]
                )
            ),
            ft.Divider(height=5),
            ft.ListTile(
                min_vertical_padding = 5,
                min_height = 1,
                dense = True,
                trailing = ft.Icon(None),
                bgcolor = ft.Colors.ON_SECONDARY,
                title = ft.Row(
                    controls = [
                        TwoLineText("BTC - USD", f"{balance.btcuss_value:,.02f}"),
                        TwoLineText("USD - BRL", f"{balance.ussbrl_value:,.02f}"),
                        TwoLineText("", ""),
                        TwoLineText("", "")
                    ]
                )
            ),
            ft.Divider(height=4, color=ft.Colors.ON_SECONDARY)
        ]
