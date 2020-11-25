class Customer():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.apparent_intoxication = 0

    def spend(self, drink):
        self.wallet -= drink.price

    def buy_drink(self, drink, pub):
        if self.age >= 18 and self.apparent_intoxication < 3:
            self.spend(drink)
            self.apparent_intoxication += drink.alcohol_units
            pub.drink_sold(drink)
