from os.path import expanduser


class OrderMaker:
    """Has ingredients to be ordered in self.ingredients 
    list with dicts in it. Saves ingredients to it when given a list of the same format.
    Creates four order files according to how many eaters there will be."""

    def __init__(self, eaters: int, folderpath_for_order_files=expanduser("~")):
        self.ingredients: list[dict] = []
        self.multiplier: float = eaters / 10
        self.asia_shop_ingredients = ["Peanut butter", "Lentils", "Rice",
        "Tahini", "Black beans", "Chick peas", "Butter beans", "Basil", "Black pepper",
        "Sweet pepper spice", "Chili/cayenne", "Cinnamon", "Fennel", "Jeera", "Coriander",
        "Parsley", "Oregano", "Mustard seeds", "Cardamom", "Tarragon", "Bay leaf"]
        self.lidl_ingredients = ["Soy milk", "Oat milk",
                                 "Coconut flakes", "Quinoa", "Raisins"]
        self.folderpath_for_order_files = folderpath_for_order_files

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

    def make_order_files(self):
        '''Creates three order files based on where the ingredients are ordered from. Saves files in folder_path fiven by user'''
        print(
            f"Creating three files in '{str(self.folderpath_for_order_files)}':")
        for ingr in self.ingredients:
            if ingr['ingredient'] in self.asia_shop_ingredients:
                with open(f'{self.folderpath_for_order_files}/asia_order.txt', 'a+') as a_file:
                    a_file.write(
                        f"{ingr['ingredient']:30}{ingr['amount']:.1f} {ingr['unit']}\n")
            elif ingr['ingredient'] in self.lidl_ingredients:
                with open(f'{self.folderpath_for_order_files}/lidl_order.txt', 'a+') as l_file:
                    l_file.write(
                        f"{ingr['ingredient']:30}{ingr['amount']:.1f} {ingr['unit']}\n")
            else:
                with open(f'{self.folderpath_for_order_files}/wholesaler_order.txt', 'a+') as file:
                    file.write(
                        f"{ingr['ingredient']:30}{ingr['amount']:.1f} {ingr['unit']}\n")
        print(
            f"Asia shop order in {self.folderpath_for_order_files}/asia_order.txt'")
        print(
            f"Lidl order in {self.folderpath_for_order_files}/lidl_order.txt'")
        print(
            f"Wholesaler order in {self.folderpath_for_order_files}/wholesaler_order.txt'")
