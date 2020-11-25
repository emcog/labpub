import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Robin', 50, 19)
        self.drink = Drink('hibster beer', 3)
        self.pub = Pub('The Dancing Otter', 100)

    def test_customer_has_name(self):
        self.assertEqual('Robin', self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(50, self.customer.wallet)

    def test_spend(self):
        self.customer.spend(self.drink)
        self.assertEqual(47, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(47, self.customer.wallet)
    
    # def test_sell_buy_drink(self):
    #     self.customer.buy_drink(self.drink, self.pub)
    #     self.assertEqual(103, self.pub.cash)
