class Customer():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def spend(self, drink):
        self.wallet -= drink.price

    def buy_drink(self, drink, pub):
        if self.age >= 18:
            self.spend(drink)
            pub.drink_sold(drink)
