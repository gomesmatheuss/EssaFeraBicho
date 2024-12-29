import flet as ft

class Utils:
    @staticmethod
    def format_big_numbers(number, dec_num=2):
        number = float(number.replace(",", "")) if type(number) == str else number

        new_dec_num = dec_num
        if dec_num > 2:
            new_dec_num = 18 - len(f"{number:,.08f}") if len(f"{number:,.08f}") <= 15 else 2

        return f"{number:,.0{new_dec_num}f}"


class TwoLineText(ft.Column):
    def __init__(self, label, text):
        super().__init__()
        self.spacing = 0
        self.expand = 1
        self.controls = [
            ft.Row(
                height = 13,
                expand = 1,
                controls = [
                    ft.Container(
                        padding = ft.padding.only(top=-6),
                        expand = 1,
                        content = ft.Text(
                            value = label,
                            color = ft.Colors.WHITE60,
                            max_lines = 1,
                            overflow = ft.TextOverflow.ELLIPSIS,
                            no_wrap = True,
                            size = 12
                        )
                    )
                ]
            ),
            ft.Row(
                height = 15,
                expand = 1,
                controls = [
                    ft.Container(
                        padding = ft.padding.only(top=-6),
                        expand = 1,
                        content = ft.Text(
                            value = text,
                            max_lines = 1,
                            overflow = ft.TextOverflow.ELLIPSIS,
                            no_wrap = True,
                            size = 16
                        )
                    )
                ]
            )
        ]


class CustomText(ft.Text):
    def __init__(self, text, color=None, text_align=ft.TextAlign.RIGHT):
        super().__init__()
        self.value = text
        self.expand = 1
        self.no_wrap = True
        self.overflow = ft.TextOverflow.ELLIPSIS
        self.size = 16
        self.text_align = text_align
        if color:
            self.color = color
