import flet as ft
from src.components.items_list import ItemsList
from src.services.balance import Balance

class CustomTabs(ft.Tabs):
    def __init__(self, balance):
        super().__init__()
        self.selected_index = 0
        self.animation_duration = 300
        self.expand = 1
        self.label_padding = ft.padding.only(top=-5, left=55, right=55)
        self.update_tabs(balance)

    def update_tabs(self, balance: Balance):
        self.tabs = [
            ft.Tab(
                tab_content = self.custom_tab_text("All", ft.Icons.ATTACH_MONEY_OUTLINED),
                content = ItemsList(balance.coins),
                height = 40
            ),
            ft.Tab(
                tab_content = self.custom_tab_text("Binance", ft.Icons.ACCOUNT_BALANCE),
                content = ItemsList(balance.binance_coins),
                height = 40
            ),
            ft.Tab(
                tab_content = self.custom_tab_text("Poloniex", ft.Icons.ACCOUNT_BALANCE),
                content = ItemsList(balance.poloniex_coins),
                height = 40
            )
        ]

    def custom_tab_text(self, text: str, icon: ft.Icons):
        return ft.Row(
            controls = [
                ft.Icon(icon),
                ft.Text(text, size=16)
            ]
        )
