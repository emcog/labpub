class Customer():

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def spend(self, drink):
        self.wallet -= drink.price

    def buy_drink(self, drink, pub):
        self.spend(drink)
        pub.drink_sold(drink)
