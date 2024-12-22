class Coin:
    def __init__(self, asset: str, amount: float, uss_value: float, btc_value: float, 
                 brl_value: float, pol_amount: float, bin_amount: float, initial_amount: float, 
                 initial_uss_value: float, initial_btc_value: float, price: float):
        self.asset = asset
        self.amount = amount
        self.uss_value = uss_value
        self.btc_value = btc_value
        self.brl_value = brl_value
        self.pol_amount = pol_amount
        self.bin_amount = bin_amount
        self.initial_amount = initial_amount
        self.initial_uss_value = initial_uss_value
        self.initial_btc_value = initial_btc_value
        self.price = price

    def update_values(self, coin):
        self.amount += coin.amount
        self.uss_value += coin.uss_value
        self.btc_value += coin.btc_value
        self.brl_value += coin.brl_value
        self.pol_amount += coin.pol_amount
        self.bin_amount += coin.bin_amount

    def get_variation_uss(self):
        if self.initial_uss_value:
            return f"{(self.uss_value / self.initial_uss_value) * 100:.02f} %"
        return "-"
    
    def get_variation_btc(self):
        if self.initial_btc_value:
            return f"{(self.btc_value / self.initial_btc_value) * 100:.02f} %"
        return "-"

    def __str__(self):
        return (
            "asset: " + self.asset + "\n" +
            "amount: " + str(self.amount) + "\n" +
            "uss_value: " + str(self.uss_value) + "\n" +
            "btc_value: " + str(self.btc_value) + "\n" +
            "brl_value: " + str(self.brl_value) + "\n" +
            "pol_amount: " + str(self.pol_amount) + "\n" +
            "bin_amount: " + str(self.bin_amount) + "\n" +
            "initial_amount: " + str(self.initial_amount) + "\n" +
            "initial_uss_value: " + str(self.initial_uss_value) + "\n" +
            "initial_btc_value: " + str(self.initial_btc_value) + "\n" +
            "price" + str(self.price)
        )
        