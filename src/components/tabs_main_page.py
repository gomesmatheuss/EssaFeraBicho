import flet as ft
from src.components.items_list import ItemsList

class CustomTabs(ft.Tabs):
    def __init__(self, coins):
        super().__init__()
        self.selected_index = 0
        self.animation_duration = 300
        self.expand = 1
        self.label_padding = ft.padding.only(top=-5, left=35, right=35)
        self.update_tabs(coins)

    def update_tabs(self, coins):
        self.tabs = self.load_content(coins)

    def load_content(self, coins):
        return [
            ft.Tab(
                text="All",
                icon=ft.icons.ATTACH_MONEY_OUTLINED,
                content=ItemsList(coins)
            ),
            ft.Tab(
                text="Binance",
                icon=ft.icons.ACCOUNT_BALANCE,
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Poloniex",
                icon=ft.icons.ACCOUNT_BALANCE,
                content=ft.Text("This is Tab 3"),
            ),
        ]
