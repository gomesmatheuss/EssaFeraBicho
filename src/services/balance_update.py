import flet as ft
from src.services.balance import Balance
from src.components.items_list import ItemsListContent
from src.components.overview import OverviewContent

class BalanceUpdate:
    def __init__(self, page: ft.Page):
        balance = Balance()

        page.overview.controls = OverviewContent.content(balance)
        page.items_list.controls = ItemsListContent.content(balance.coins)

        page.update()
