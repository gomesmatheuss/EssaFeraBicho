import flet as ft
from src.services.balance import Balance

class BalanceUpdate:
    def __init__(self, page: ft.Page):
        balance = Balance()

        page.overview.update_content(balance)
        page.customtabs.update_tabs(balance.coins)

        page.update()
