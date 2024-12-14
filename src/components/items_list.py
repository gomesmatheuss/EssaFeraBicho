import flet as ft
from src.services.balance.coin import Coin

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

class ItemsExpansion(ft.ExpansionTile):
    def __init__(self, asset: Coin, count: int):
        super().__init__("")
        _asset = f'{count:02d} - {asset.asset}'
        _amount = f'{asset.amount:.08f}'
        _uss_value = f'{asset.uss_value:.02f}' if asset.uss_value > 0 else "-"
        _variation = asset.get_variation_uss() if asset.uss_value > 0 else "-"
        _color = ft.colors.LIGHT_GREEN_ACCENT_700 if asset.get_variation_uss() != "-" and float(asset.get_variation_uss().replace(" %", "")) >= 0 else ft.colors.RED_500

        self.trailing = ft.Icon(ft.icons.ARROW_DROP_DOWN)
        self.initially_expanded = False
        self.collapsed_text_color = ft.colors.WHITE
        self.text_color = ft.colors.BLUE
        self.bgcolor = ft.colors.PRIMARY_CONTAINER
        self.min_tile_height = 2
        self.show_trailing_icon = False
        self.title = ft.Row(
            controls = [
                ItemsText(_asset),
                ItemsText(_amount),
                ItemsText(_uss_value),
                ItemsText(_variation, _color)
            ]
        )
        self.controls = [
            ft.ListTile(title=ft.Text("Sub - Item 1"))
        ]

        del _asset, _amount, _uss_value, _variation, _color

class ItemsList(ft.Column):
    def __init__(self, coins):
        super().__init__()
        self.spacing = 0
        self.controls = [
            ItemsExpansion(asset, count)
            for count, asset in enumerate(coins, start = 1)
        ]
