import flet as ft
from src.services.balance.coin import Coin
from src.services.utils import Utils, TwoLineText

class ItemsText(ft.Text):
    def __init__(self, text, color=None):
        super().__init__()
        self.value = text
        self.expand = 1
        self.no_wrap = True
        self.overflow = ft.TextOverflow.ELLIPSIS
        self.size = 16
        if color:
            self.color = color


class ItemsExpansion(ft.ExpansionTile):
    def __init__(self, asset: Coin, count: int):
        super().__init__("")
        _asset = f'{count:02d} - {asset.asset}'
        _amount = f'{asset.amount:,.08f}'
        _uss_value = f'{asset.uss_value:,.02f}' if asset.uss_value > 0 else "-"
        _variation = asset.get_variation_uss() if asset.uss_value > 0 else "-"
        _color = ft.Colors.LIGHT_GREEN_ACCENT_700 if asset.get_variation_uss() != "-" and float(asset.get_variation_uss().replace(" %", "")) >= 0 else ft.Colors.RED_500

        self.initially_expanded = False
        self.collapsed_text_color = ft.Colors.WHITE
        self.text_color = ft.Colors.BLUE_200
        self.bgcolor = ft.Colors.PRIMARY_CONTAINER
        self.min_tile_height = 1
        self.show_trailing_icon = False
        self.title = ft.Row(
            controls = [
                ItemsText(_asset),
                ItemsText(Utils.format_big_numbers(_amount, 8)),
                ItemsText(_uss_value),
                ItemsText(_variation, _color)
            ]
        )
        self.controls = self.ItemsListTile(asset)

        del _asset, _amount, _uss_value, _variation, _color

    def ItemsListTile(self, asset: Coin):
        _pol_amount = Utils.format_big_numbers(asset.pol_amount, 8)
        _bin_amount = Utils.format_big_numbers(asset.bin_amount, 8)
        _init_amount = Utils.format_big_numbers(asset.initial_amount, 8)
        _init_uss = f'{asset.initial_uss_value:,.02f}'
        _init_btc = f'{asset.initial_btc_value:,.08f}'
        _brl_value = f'{asset.brl_value:,.02f}'
        _price = f'{asset.price:,.02f}'
        _btc_variation = asset.get_variation_btc()

        return [
            ft.ListTile(
                min_vertical_padding = 5,
                min_height = 1,
                dense = True,
                bgcolor = ft.Colors.PRIMARY_CONTAINER,
                title = ft.Row(
                    controls = [
                        TwoLineText("Poloniex", _pol_amount),
                        TwoLineText("Initial Amount", _init_amount),
                        TwoLineText("Initial USS", _init_uss),
                        TwoLineText("Initial BTC", _init_btc)
                    ]
                )
            ),
            ft.ListTile(
                min_vertical_padding = 5,
                min_height = 1,
                dense = True,
                bgcolor = ft.Colors.PRIMARY_CONTAINER,
                title = ft.Row(
                    controls = [
                        TwoLineText("Binance", _bin_amount),
                        TwoLineText("Price", _price),
                        TwoLineText("R$", _brl_value),
                        TwoLineText("BTC Value Variation", _btc_variation)
                    ]
                )
            ),
            ft.Divider(height=6, color=ft.Colors.PRIMARY_CONTAINER)
            # ft.ListTile(
            #     title=ft.Row(
            #         controls = [
            #             ItemsTextField("What if BTC", -),
            #             ItemsTextField("BTC Value", -),
            #         ]
            #     )
            # )
        ]


class ItemsList(ft.Column):
    def __init__(self, coins):
        super().__init__()
        self.spacing = 0
        self.controls = self.update_list(coins)

    def update_list(self, coins):
        return [
            ft.ListView(
                expand = 1,
                controls = [
                    ItemsExpansion(asset, count)
                    for count, asset in enumerate(coins, start = 1)
                ]
            )
        ]
