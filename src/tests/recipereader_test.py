import unittest
from recipereader import recipereader


class TestRecipeReader(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_recipereader_reads_recipe_file(self):
        r_r = recipereader.RecipeReader(f'files/Day 0 ENG Jan 20.docx')
        r_r.read()
        self.assertEqual(len(r_r.ingredients_list), 10)
