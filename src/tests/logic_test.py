import unittest
from logic import logic
from os.path import expanduser
from os import path
from datetime import datetime


class TestLogic(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_logic_for_one_creates_folderpath_and_order_files(self):
        logic1 = logic.Logic(1)
        homepath = expanduser("~")
        creation_time = datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
        folderpath = f'{homepath}/order{creation_time}'
        logic1.generate_order_based_on_recipes()
        self.assertTrue(path.exists(folderpath+'/asia_order.txt'))
        self.assertTrue(path.exists(folderpath+'/lidl_order.txt'))
        self.assertTrue(path.exists(folderpath+'/wholesaler_order.txt'))
        

        
        
