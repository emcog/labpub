from src.drink import Drink

class Pub():
    
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.drinks = [Drink('hibster beer', 3)]