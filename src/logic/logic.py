from ordermaker.ordermaker import OrderMaker
from recipereader.recipereader import RecipeReader


class Logic:
    def __init__(self, eaters: int):
        self.eaters = eaters

    def generate_order_based_on_recipes(self) -> str:
        ordermaker = OrderMaker(self.eaters)
        for i in range(0, 11):
            recipereader = RecipeReader(f'files/Day {i} ENG Jan 20.docx')
            recipereader.read()
            ingr_list = recipereader.get_ingredients_list()
            ordermaker.add_ingredients(ingr_list)
        return ordermaker.make_order_files()
