import flet as ft
from src.components.navbar import Navbar
from src.components.initial_page import InitialPage

def main(page: ft.Page):
    page.title = "Essa Fera Bicho"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.ON_SECONDARY

    page.window.width = 1080 #480
    page.window.height = 900 #720
    page.window.min_width = 400 #720    

    navbar = Navbar()
    button = InitialPage()

    page.add(navbar, button)

if __name__ == "__main__":
    ft.app(target=main)
