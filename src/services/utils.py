import flet as ft

class Utils:
    @staticmethod
    def format_big_numbers(number, dec_num=2):
        number = float(number.replace(",", "")) if type(number) == str else number

        new_dec_num = dec_num
        if dec_num > 2:
            new_dec_num = 18 - len(f"{number:,.08f}") if len(f"{number:,.08f}") <= 15 else 2

        return f"{number:,.0{new_dec_num}f}"

class CustomTextField(ft.TextField):
    def __init__(self, label, text):
        super().__init__()
        self.label = label
        self.label_style = ft.TextStyle(color=ft.colors.WHITE70, overflow=ft.TextOverflow.ELLIPSIS, size=17)
        self.value = text
        self.disabled = True
        self.border = ft.InputBorder.NONE
        self.color = ft.colors.WHITE
        self.border_color = ft.colors.WHITE
        self.height = 36
        self.content_padding = ft.padding.symmetric(vertical=4, horizontal=1)
        self.expand = True
        self.multiline = False
        self.max_lines = 1
