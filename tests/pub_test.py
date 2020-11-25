import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub('The Dancing Otter', 100)
        self.drink = Drink('hibster beer', 3)
        self.customer = Customer('Robin', 50, 19)

    def test_pub_has_name(self):
        self.assertEqual('The Dancing Otter', self.pub.name)

    def test_drink_sold(self):
        self.pub.drink_sold(self.drink)
        self.assertEqual(103, self.pub.cash)

