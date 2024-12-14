import flet as ft
from src.components.navbar import Navbar
from src.services.balance_update import BalanceUpdate

class LoadButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.text = "Load"
        self.on_click = lambda func: BalanceUpdate(self.page)
        self.style = ft.ButtonStyle(
            bgcolor=ft.colors.BLUE,
            color=ft.colors.WHITE
        )

class InitialPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.center
        self.height = 100
        self.expand = True
        self.content = LoadButton()
