import flet as ft
from src.services.balance import Balance
from src.components.overview import Overview
from src.components.navbar import Navbar
from src.components.items_list import ItemsList

class BalanceUpdate:
    def __init__(self, page: ft.Page):
        page.controls.clear()
        page.update()
        
        balance = Balance()
        navbar = Navbar()
        overview = Overview(balance)
        items_list = ItemsList(balance.coins)
        
        page.add(
            navbar,
            overview,
            items_list
        )
        page.update()
