import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink('hibster beer', 3, 1)

    def test_drink_has_name(self):
        self.assertEqual('hibster beer', self.drink.name)