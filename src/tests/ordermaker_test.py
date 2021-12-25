import unittest
from ordermaker import ordermaker
from os.path import expanduser
from os import path
from datetime import datetime


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
    
    def test_ordermaker_generates_order_folder(self):
        o_m = ordermaker.OrderMaker(1)
        homepath = expanduser("~")
        creation_time = datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
        folderpath = f'{homepath}/order{creation_time}'
        o_m.generate_order_folder()
        self.assertTrue(path.exists(folderpath))
    
