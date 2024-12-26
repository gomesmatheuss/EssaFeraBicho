import flet as ft
from src.components.main_page import MainPage

class LoadButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.text = "Load"
        self.on_click = lambda f: MainPage(self.page)
        self.style = ft.ButtonStyle(
            bgcolor = ft.Colors.BLUE,
            color = ft.Colors.WHITE
        )

class InitialPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.alignment.top_center
        self.padding = ft.padding.only(top=50)
        self.expand = True
        self.content = LoadButton()
