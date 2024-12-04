import flet as ft
from balance import Balance

def main(page: ft.Page):
    page.title = "Essa Fera Bicho - Mobile"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.GREEN)
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.ON_SECONDARY
    page.scroll = ft.ScrollMode.HIDDEN

    page.window.width = 480
    page.window.height = 720
    page.window.min_width = 480 #720

    balance = Balance()

    # Navbar
    navbar = ft.AppBar(
        title=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "Estimated Values:",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        no_wrap=True,
                        color=ft.colors.WHITE,
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=5),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                f"BTC {balance.btcuss_value:.02f} US$ |",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                no_wrap=True,
                                color=ft.colors.WHITE,
                            ),
                            ft.Text(
                                f"Dólar R$ {balance.ussbrl_value:.02f}",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                no_wrap=True,
                                color=ft.colors.WHITE,
                            ),
                            ft.Text(
                                f"| Last update: {balance.last_update[:16]}",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                no_wrap=True,
                                color=ft.colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.symmetric(vertical=5),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Poloniex:",
                                expand=1,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"{balance.poloniex_btc_value:.08f} BTC",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"US$ {balance.poloniex_uss_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"R$ {balance.poloniex_brl_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=0,
                    ),
                    alignment=ft.alignment.center_left,
                    padding=ft.padding.symmetric(vertical=2),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Binance:",
                                expand=1,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"{balance.binance_btc_value:.08f} BTC",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"US$ {balance.binance_uss_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"R$ {balance.binance_brl_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=0,
                    ),
                    alignment=ft.alignment.center_left,
                    padding=ft.padding.symmetric(vertical=2),
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "Total:",
                                expand=1,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"{balance.btc_value:.08f} BTC",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"US$ {balance.uss_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                            ft.Text(
                                f"R$ {balance.brl_value:.02f}",
                                expand=2,
                                color=ft.colors.WHITE,
                                no_wrap=True,
                                size=16,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=0,
                    ),
                    alignment=ft.alignment.center_left,
                    padding=ft.padding.symmetric(vertical=2),
                )
            ],
            spacing=0,
        ),
        bgcolor=ft.colors.INVERSE_PRIMARY,
        toolbar_height=170,
    )

    # Cabeçalho acima da lista
    header = ft.Container(
        content=ft.Text(
            "Cabeçalho - Informações Importantes",
            size=18,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.WHITE
        ),
        bgcolor=ft.colors.BLUE_GREY_600,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center_left
    )

    # Lista de painéis expansíveis
    expansion_items = ft.Column(
        spacing=0,
        controls=[
            ft.Container(
                ft.ExpansionTile(
                    title=ft.Row(
                        controls=[
                            ft.Text(
                                f'{i:02d} - {asset.asset}',
                                expand=1,
                                no_wrap=True,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                size=14
                            ),
                            ft.Text(
                                f'{asset.amount:.08f}',
                                expand=1,
                                no_wrap=True,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                text_align=ft.TextAlign.RIGHT,
                                size=14
                            ),
                            # ft.Text(
                            #     f'{asset.btc_value:.08f}' if asset.btc_value > 0 else "-",
                            #     expand=1,
                            #     no_wrap=True,
                            #     overflow=ft.TextOverflow.ELLIPSIS,
                            #     text_align=ft.TextAlign.RIGHT,
                            #     size=14
                            # ),
                            ft.Text(
                                f'{asset.uss_value:.02f}' if asset.uss_value > 0 else "-",
                                expand=1,
                                no_wrap=True,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                text_align=ft.TextAlign.RIGHT,
                                size=14
                            ),
                            ft.Text(
                                asset.get_variation_uss() if asset.uss_value > 0 else "-",
                                expand=1,
                                color=ft.colors.LIGHT_GREEN_ACCENT_700 if asset.get_variation_uss() != "- %" and float(asset.get_variation_uss().replace(" %", "")) >= 0 else ft.colors.RED_500,
                                no_wrap=True,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                text_align=ft.TextAlign.RIGHT,
                                size=14
                            )
                        ],
                        alignment="spaceBetween"
                    ),
                    trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
                    initially_expanded=False,
                    collapsed_text_color=ft.colors.WHITE,
                    text_color=ft.colors.BLUE,
                    controls=[
                        ft.ListTile(title=ft.Text("Sub - Item 1"))
                    ]
                ),
                margin=ft.margin.symmetric(vertical=-10)
            ) for i, asset in enumerate(balance.coins, start=1)
        ]
    )

    # Layout final
    page.add(
        navbar,
        # header,  # Cabeçalho acima da lista
        expansion_items
    )

if __name__ == "__main__":
    ft.app(target=main)
