import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Robin', 50)

    def test_customer_has_name(self):
        self.assertEqual('Robin', self.customer.name)

    def test_buy_drink(self):
        pass
