import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Robin', 50)
        self.drink = Drink('hibster beer', 3)

    def test_customer_has_name(self):
        self.assertEqual('Robin', self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(50, self.customer.wallet)

    def test_spend(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(47, self.customer.wallet)

    # def test_wallet_amount_changed():
        # test the wallet amount has changed

    def test_buy_drink(self):
        pass
        # test the wallet has been decreased by drink ammount
        # and the till has increased by the drink amount