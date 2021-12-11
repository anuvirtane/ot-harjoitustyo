class OrderMaker:
    """Has ingredients to be ordered in self.ingredients_for_ten list with dicts in it. Saves ingredients to it when given a list of the same format.
    todo: Creates four order files according to how many eaters there will be."""
    def __init__(self, eaters: int):
        self.ingredients_for_ten: list [dict] = []
        self.multiplier: float = eaters / 10

    def add_ingredients(self, ingredients_list: list):
        for item in ingredients_list:
            if not self.dict_already_in_ingredients_for_ten(item):
                self.ingredients_for_ten.append({'ingredient': item['ingredient'], 'amount': item['amount']* self.multiplier, 'unit': item['unit']})
            else:
                self.add_to_existing_ingredient_for_ten(item)

    def dict_already_in_ingredients_for_ten(self, ingr_dict: dict) -> bool:
        for item in self.ingredients_for_ten:
            if item['ingredient'].lower().strip() == ingr_dict['ingredient'].lower().strip():
                return True
        return False
        
    def add_to_existing_ingredient_for_ten(self, ingr_dict: dict):
        for ingr in self.ingredients_for_ten:
            if ingr['ingredient'].lower() == ingr_dict['ingredient'].lower():
                ingr['amount'] += ingr_dict['amount'] * self.multiplier
    
    def print(self):
        print(self.ingredients_for_ten)

    



    

