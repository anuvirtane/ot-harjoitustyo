import unittest
from recipereader import recipereader


class TestRecipeReader(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_recipereader_reads_bad_recipe_file(self):
        r_r = recipereader.RecipeReader("files/dingdong.txt")
        r_r.read()
        self.assertEqual(r_r.recipe, "ding\ndong\nbom")
