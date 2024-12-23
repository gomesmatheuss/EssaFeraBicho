import flet as ft
from src.components.items_list import ItemsList

class CustomTabs(ft.Tabs):
    def __init__(self, balance):
        super().__init__()
        self.selected_index = 0
        self.animation_duration = 300
        self.expand = 1
        self.label_padding = ft.padding.only(top=-5, left=35, right=35)
        self.update_tabs(balance)

    def update_tabs(self, balance):
        self.tabs = self.load_content(balance)

    def load_content(self, balance):
        return [
            ft.Tab(
                text="All",
                icon=ft.icons.ATTACH_MONEY_OUTLINED,
                content=ItemsList(balance.coins)
            ),
            ft.Tab(
                text="Binance",
                icon=ft.icons.ACCOUNT_BALANCE,
                content=ItemsList(balance.binance_coins)
            ),
            ft.Tab(
                text="Poloniex",
                icon=ft.icons.ACCOUNT_BALANCE,
                content=ItemsList(balance.poloniex_coins)
            )
        ]
