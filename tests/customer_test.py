import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def SetUp(self):
        self.customer = Customer('Robin', 50)

    def test_buy_drink(self):
        pass
