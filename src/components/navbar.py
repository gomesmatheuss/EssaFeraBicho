import flet as ft
from src.services.balance_update import BalanceUpdate

class NavbarTitle(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Container(
                content = ft.Text(
                    "Wallet",
                    size = 22,
                    weight = ft.FontWeight.BOLD,
                    no_wrap = True,
                    color = ft.Colors.WHITE,
                ),
                alignment = ft.alignment.center,
                padding = ft.padding.symmetric(vertical=5)
            )
        ]


class Navbar(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.title = NavbarTitle()
        self.bgcolor = ft.Colors.INVERSE_PRIMARY
        self.actions = [
            ft.IconButton(
                icon = ft.Icons.REFRESH,
                tooltip = "Recarregar dados",
                on_click = lambda func: BalanceUpdate(self.page),
                padding = ft.padding.symmetric(horizontal=20),
                alignment = ft.alignment.center,
                visible = False
            )
        ]
