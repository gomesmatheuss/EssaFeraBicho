import flet as ft
from src.services.balance import Balance
from src.components.overview import Overview
from src.components.navbar import Navbar
from src.components.tabs_main_page import CustomTabs

class MainPage:
    def __init__(self, page: ft.Page):
        page.controls.clear()
        page.update()
        
        balance = Balance()
        navbar = Navbar()
        page.overview = Overview(balance)
        page.customtabs = CustomTabs(balance)
        
        page.add(
            navbar,
            page.overview,
            page.customtabs
        )

        navbar.actions[0].visible = True

        page.update()
