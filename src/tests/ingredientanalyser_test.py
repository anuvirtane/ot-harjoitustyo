import unittest
from ingredientanalyser import ingredientanalyser


class TestIngredientAnalyser(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_ingredientanalyser_saves_ingredients_in_ingr_dict(self):
        ia = ingredientanalyser.IngredientAnalyser()
        ia.ingredients = [{'ingredient': 'Onion', 'amount': 0.25, 'unit': 'kg'},
                          {'ingredient': 'Carrot', 'amount': 0.2, 'unit': 'kg'},
                          {'ingredient': 'Lentils', 'amount': 1.7, 'unit': 'kg'},
                          {'ingredient': 'Turmeric', 'amount': 10, 'unit': 'g'},
                          {'ingredient': 'Basil', 'amount': 100, 'unit': 'g'},
                          {'ingredient': 'Salt', 'amount': 10, 'unit': 'g'},
                          {'ingredient': 'Black pepper',
                              'amount': 10, 'unit': 'ml'},
                          {'ingredient': 'Chili/cayenne',
                              'amount': 1, 'unit': 'tbsp'},
                          {'ingredient': 'Soy sauce', 'amount': 1.1, 'unit': 'dl'},
                          {'ingredient': 'Vegetable broth', 'amount': 10.0, 'unit': 'ml'}]
        ia.convert_units()
        expected_result = [{'ingredient': 'Onion', 'amount': 0.25, 'unit': 'kg'},
                           {'ingredient': 'Carrot', 'amount': 0.2, 'unit': 'kg'},
                           {'ingredient': 'Lentils', 'amount': 1.7, 'unit': 'kg'},
                           {'ingredient': 'Turmeric', 'amount': 100, 'unit': 'g'},
                           {'ingredient': 'Basil', 'amount': 100, 'unit': 'g'},
                           {'ingredient': 'Salt', 'amount': 1, 'unit': 'kg'},
                           {'ingredient': 'Black pepper',
                               'amount': 100, 'unit': 'g'},
                           {'ingredient': 'Chili/cayenne',
                               'amount': 100, 'unit': 'g'},
                           {'ingredient': 'Soy sauce', 'amount': 3, 'unit': 'l'},
                           {'ingredient': 'Vegetable broth', 'amount': 10.0, 'unit': 'ml'}]
        self.assertEqual(ia.ingredients, expected_result)
