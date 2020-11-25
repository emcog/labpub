class Customer():

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, drink):
        # 1. reduce the drink amount from customers wallet
        # 2. increase shop cash by same amount
        self.wallet -= drink.price
        pub.cash += drink.price