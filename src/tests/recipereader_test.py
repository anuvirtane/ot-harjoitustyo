import unittest
from recipereader import recipereader

class TestRecipeReader(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_recipereader_reads_bad_recipe_file(self):
        rr = recipereader.RecipeReader("files/dingdong.txt")
        rr.read()
        self.assertEqual(rr.recipe, "ding\ndong\nbom")