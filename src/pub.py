class Pub():
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = []

    def drink_sold(self, drink):
        self.cash += drink.price
