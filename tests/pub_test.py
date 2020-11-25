import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub('The Dancing Otter', 100)

    def test_pub_has_name(self):
        self.assertEqual('The Dancing Otter', self.pub.name)
