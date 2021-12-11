from docx import Document

class RecipeReader():
    """Reads file given at class instance creation, 
    and finds recipe ingredients in it. Saves ingredients in list withs dicts in it,
    self.ingredients_list. Format of dicts in self.ingredients_list is e. g.
    {'ingredient': 'Salt', 'amount': 10, 'unit': 'g'}
   """
    def __init__(self, recipe_file: str = "files/Day0.txt"):
        self.recipe_file = recipe_file
        self.ingredients_list: list [dict] = []

    def read(self):
        """Reads recipe file given as argument to class instance and
        gets gets recipe tables from it"""
        try:
           
            document = Document(self.recipe_file)
            for index, table in enumerate(document.tables[1:]): #first table is not a recipe
                list_from_table = []
                for row in range(len(table.rows)):
                    for col in range(len(table.columns)):
                        if not "Ingredients" in table.cell(row, col).text: #this string starts recipe                 
                            list_from_table.append(table.cell(row, col).text)
                self.save_ingredients_for_ten(list_from_table)
        except Exception as exc:
            raise TypeError("Something went wrong in finding ingredients from recipe text:", exc)

    def save_ingredients_for_ten(self, list_from_table: list):
        """Chooses parts from table where ingredient names and amounts for 10 people are. Saves them in dict, e. g.
        {'ingredient': 'Salt', 'amount': 10, 'unit': 'g'} and saves dicts in ingredients_list or if ingredient
        already exists in ingredients_list, adds to amount of existing ingredient"""
        ingredients_names = list_from_table[4].split("\n")
        ingredient_amounts_for_ten = list_from_table[5].split("\n")
        if len(ingredients_names) < len(ingredient_amounts_for_ten):
            ingredient_amounts_for_ten = ingredient_amounts_for_ten[:len(ingredients_names)]
        for i in range(0, len(ingredient_amounts_for_ten)):
            if ingredient_amounts_for_ten[i].strip() != 'pinch' and ingredient_amounts_for_ten[i] != '':
                if ingredients_names[i].lower().strip() != 'water' and ingredients_names[i] != '' and ingredients_names[i].lower().strip() != "broth (cpeas cooking water)":
                    if not self.ingredient_already_in_ingredients_list(ingredients_names[i]):
                        amount, unit = self.split_ingredient_amounts_and_units(ingredient_amounts_for_ten[i])
                        ingr_dict = {'ingredient': ingredients_names[i].strip(), 'amount': amount, 'unit': unit}
                        self.ingredients_list.append(ingr_dict)
                    else:
                        if ingredient_amounts_for_ten[i].strip() != 'pinch' and ingredient_amounts_for_ten[i] != '':
                            amount, unit = self.split_ingredient_amounts_and_units(ingredient_amounts_for_ten[i])
                            self.add_to_existing_ingredient(ingredients_names[i], amount, unit)

    def ingredient_already_in_ingredients_list(self, ingredient: str) -> bool:
        for item in self.ingredients_list:
            if item['ingredient'].lower().strip() == ingredient.lower().strip():
                return True
        return False

    def split_ingredient_amounts_and_units(self, item: str) -> tuple:
        """splits string, e. g. '1 kg' into amount and unit (1, 'kg') and returns them as tuple"""
        amount_and_unit:list  = item.split(" ")
        if "-" in amount_and_unit[0]:
            amount_and_unit[0] = amount_and_unit[0][2:]
        amount: float = float(amount_and_unit[0].replace(",", "."))
        unit: str = amount_and_unit[1]
        return self.convert_units(amount, unit)

    def convert_units(self, amount: float, unit: str)-> tuple:
        """Converts units to l, kg etc"""
        if unit.lower().strip() == 'ml':
            unit = 'l'
            amount = amount / 100
        if unit.lower().strip() == 'dl':
            unit = 'l'
            amount = amount / 10
        if unit.lower().strip() == 'tsp':
            unit = 'g'
            amount = 50
        if unit.lower().strip() == 'tbsp':
            unit = 'g'
            amount = 50
        if unit.lower().strip() == 'g':
            unit = 'kg'
            amount = amount / 100
        return amount, unit
        
    def add_to_existing_ingredient(self, ingredient: str, amount: float, unit: str):
        for ingr in self.ingredients_list:
            if ingr['ingredient'].lower() == ingredient.lower():
                if ingr['unit'].lower() == unit.lower():
                    ingr['amount'] += amount
                else:
                    print("Could not add", ingredient, amount, unit, "to",
                          ingr['ingredient'], ingr['amount'], ingr['unit'],
                          "because unit did not match")

    def get_ingredients_list(self):
        return self.ingredients_list

 
           