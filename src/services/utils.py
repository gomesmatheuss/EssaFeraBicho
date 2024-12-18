class Utils:
    @staticmethod
    def format_big_numbers(number, dec_num=2):
        number = float(number.replace(",", ""))

        new_dec_num = dec_num
        if dec_num > 2:
            new_dec_num = 18 - len(f"{number:,.08f}") if len(f"{number:,.08f}") <= 15 else 2

        return f"{number:,.0{new_dec_num}f}"