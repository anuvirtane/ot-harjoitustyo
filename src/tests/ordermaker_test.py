import unittest
from ordermaker import ordermaker


class TestOrderMaker(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_ordermaker_converts_amounts(self):
        o_m = ordermaker.OrderMaker(100)
        o_m.ingredients = [
            {'ingredient': 'cake', 'amount': 10.0, 'unit': 'kg'}]
        o_m.add_ingredients([{'ingredient': 'cake', 'amount': 1.0, 'unit': 'kg'}, {
                            'ingredient': 'chocolate', 'amount': 11.0, 'unit': 'kg'}])
        self.assertEqual(o_m.ingredients, [{'ingredient': 'cake', 'amount': 20.0, 'unit': 'kg'}, {
                         'ingredient': 'chocolate', 'amount': 110.0, 'unit': 'kg'}])
