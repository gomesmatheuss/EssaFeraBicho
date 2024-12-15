import flet as ft
from src.services.balance import Balance
from src.components.overview import Overview
from src.components.navbar import Navbar
from src.components.items_list import ItemsList

class MainPage:
    def __init__(self, page: ft.Page):
        page.controls.clear()
        page.update()
        
        balance = Balance()
        navbar = Navbar()
        page.overview = Overview(balance)
        page.items_list = ItemsList(balance.coins)
        
        page.add(
            navbar,
            page.overview,
            page.items_list
        )

        navbar.actions[0].visible = True

        page.update()
