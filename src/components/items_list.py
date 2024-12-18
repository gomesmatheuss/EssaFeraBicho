import flet as ft
from src.services.balance.coin import Coin
from src.services.utils import Utils

class ItemsText(ft.Text):
    def __init__(self, text, color=None):
        super().__init__()
        self.value = text
        self.expand = 1
        self.no_wrap = True
        self.overflow = ft.TextOverflow.ELLIPSIS
        self.size = 14
        if color:
            self.color = color

class ItemsTextField(ft.TextField):
    def __init__(self, label, text):
        super().__init__()
        self.label = label
        self.label_style = ft.TextStyle(color=ft.colors.WHITE70, overflow=ft.TextOverflow.ELLIPSIS, size=17)
        self.value = text
        self.disabled = True
        self.border = ft.InputBorder.NONE
        self.color = ft.colors.WHITE
        self.border_color = ft.colors.WHITE
        self.height = 27
        self.content_padding = ft.padding.all(1)
        self.expand = True
        self.multiline = False
        self.max_lines = 1

class ItemsExpansion(ft.ExpansionTile):
    def __init__(self, asset: Coin, count: int):
        super().__init__("")
        _asset = f'{count:02d} - {asset.asset}'
        _amount = f'{asset.amount:,.08f}'
        _uss_value = f'{asset.uss_value:,.02f}' if asset.uss_value > 0 else "-"
        _variation = asset.get_variation_uss() if asset.uss_value > 0 else "-"
        _color = ft.colors.LIGHT_GREEN_ACCENT_700 if asset.get_variation_uss() != "-" and float(asset.get_variation_uss().replace(" %", "")) >= 0 else ft.colors.RED_500

        self.trailing = ft.Icon(ft.icons.ARROW_DROP_DOWN)
        self.initially_expanded = False
        self.collapsed_text_color = ft.colors.WHITE
        self.text_color = ft.colors.BLUE_200
        self.bgcolor = ft.colors.PRIMARY_CONTAINER
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

        return [
            ft.ListTile(
                min_vertical_padding=1,
                min_height=1,
                title=ft.Row(
                    controls = [
                        ItemsTextField("Poloniex", _pol_amount),
                        ItemsTextField("Initial Amount", _init_amount),
                        ItemsTextField("Initial USS", _init_uss),
                        ItemsTextField("Initial BTC", _init_btc)
                    ]
                )
            ),
            ft.ListTile(
                title=ft.Row(
                    controls = [
                        ItemsTextField("Binance", _bin_amount),
                        ItemsTextField("Price", _price),
                        ItemsTextField("R$", _brl_value),
                        ItemsTextField("", "")
                    ]
                )
            )
        ]

class ItemsListContent:
    @staticmethod
    def content(coins):
        return [
            ItemsExpansion(asset, count)
            for count, asset in enumerate(coins, start = 1)
        ]

class ItemsList(ft.Column):
    def __init__(self, coins):
        super().__init__()
        self.spacing = 0
        self.controls = ItemsListContent.content(coins)
