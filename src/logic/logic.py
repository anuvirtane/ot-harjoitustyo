from ordermaker.ordermaker import OrderMaker
from recipereader.recipereader import RecipeReader


class Logic:
    """Knows how many eaters order files have to be generated for and
    orchestrates ordermaker instance to generate them according to
    ingredients for 10 read by 11 recipereaders"""
    def __init__(self, eaters: int):
        self.eaters = eaters

    def generate_order_based_on_recipes(self) -> str:
        """Makes an instance of OrderMaker
        class and eleven instances of RecipeReader
        class. Passes ingredients read by recipereaders to
        ordermaker. Returns order file locations made by ordermaker."""  
        ordermaker = OrderMaker(self.eaters)
        for i in range(0, 11):
            recipereader = RecipeReader(f'files/Day {i} ENG Jan 20.docx')
            recipereader.read()
            ingr_list = recipereader.get_ingredients_list()
            ordermaker.add_ingredients(ingr_list)
        return ordermaker.make_order_files()
