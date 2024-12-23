import flet as ft
from src.services.utils import CustomTextField

class Overview(ft.ExpansionTile):
    def __init__(self, balance):
        super().__init__("")
        self.initially_expanded = False
        self.collapsed_text_color = ft.colors.WHITE
        self.text_color = ft.colors.BLUE_200
        self.min_tile_height = 1
        self.update_content(balance)

    def update_content(self, balance):
        self.title = ft.Row(
            alignment = ft.MainAxisAlignment.START,
            controls = [
                CustomTextField("Total - BTC", f"{balance.btc_value:,.08f}"),
                CustomTextField("Total - USD", f"{balance.uss_value:,.02f}"),
                CustomTextField("Total - R$", f"{balance.brl_value:,.02f}"),
                CustomTextField("Updated", f"{balance.last_update[11:19]}")
            ]
        )
        self.controls = [
            ft.ListTile(
                min_vertical_padding=1,
                min_height=1,
                trailing=ft.Icon(None),
                title=ft.Row(
                    controls = [
                        CustomTextField("Poloniex - BTC", f"{balance.poloniex_btc_value:,.08f}"),
                        CustomTextField("Poloniex - USD", f"{balance.poloniex_uss_value:,.02f}"),
                        CustomTextField("Poloniex - R$", f"{balance.poloniex_brl_value:,.02f}"),
                        CustomTextField("", "")
                    ]
                )
            ),
            ft.ListTile(
                # min_vertical_padding=1,
                # min_height=1,
                trailing=ft.Icon(None),
                title=ft.Row(
                    controls = [
                        CustomTextField("Binance - BTC", f"{balance.binance_btc_value:,.08f}"),
                        CustomTextField("Binance - USD", f"{balance.binance_uss_value:,.02f}"),
                        CustomTextField("Binance - R$", f"{balance.binance_brl_value:,.02f}"),
                        CustomTextField("", "")
                    ]
                )
            ),
            ft.ListTile(
                # min_vertical_padding=1,
                # min_height=1,
                trailing=ft.Icon(None),
                title=ft.Row(
                    controls = [
                        CustomTextField("BTC - USD", f"{balance.binance_btc_value:,.08f}"),
                        CustomTextField("Binance - USD", f"{balance.binance_uss_value:,.02f}"),
                        CustomTextField("Binance - R$", f"{balance.binance_brl_value:,.02f}"),
                        CustomTextField("", "")
                    ]
                )
            )
        ]
