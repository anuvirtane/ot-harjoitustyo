class OrderMaker:
    """Has ingredients to be ordered in self.ingredients 
    list with dicts in it. Saves ingredients to it when given a list of the same format.
    todo: Creates four order files according to how many eaters there will be."""

    def __init__(self, eaters: int):
        self.ingredients: list[dict] = []
        self.multiplier: float = eaters / 10

    def add_ingredients(self, ingredients_list: list):
        '''Ingredients come in amounts calculated for ten. 
        When added, they are also multiplied to match wished amount.'''
        for item in ingredients_list:
            if not self.dict_already_in_ingredients(item):
                self.ingredients.append(
                    {'ingredient': item['ingredient'], 'amount': item['amount'] * self.multiplier, 'unit': item['unit']})
            else:
                self.add_to_existing_ingredient_for_ten(item)

    def dict_already_in_ingredients(self, ingr_dict: dict) -> bool:
        for item in self.ingredients:
            if item['ingredient'].lower().strip() == ingr_dict['ingredient'].lower().strip():
                return True
        return False

    def add_to_existing_ingredient_for_ten(self, ingr_dict: dict):
        '''Adds ingredients to already existing dicts so that amount is increased.'''
        for ingr in self.ingredients:
            if ingr['ingredient'].lower() == ingr_dict['ingredient'].lower():
                ingr['amount'] += ingr_dict['amount'] * self.multiplier

    def print(self):
        print(self.ingredients)
