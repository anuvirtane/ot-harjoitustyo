from recipereader.recipereader import RecipeReader


class IngredientAnalyser:
    def __init__(self):
        self.ingredients: list[dict] = []
        self.recipereader: RecipeReader = None

    def save_ingredients(self, recipe_file: str):
        self.recipereader = RecipeReader(recipe_file)
        self.recipereader.read()
        print("using recipes for 10 people as basis")
        self.save_in_dict()

    def save_in_dict(self):
        ingr_names = self.recipereader.get_ingredients_names()
        amounts_for_10: list[str] = self.recipereader.get_ingredients_dict()[
            '10 p']
        for i in range(0, len(ingr_names)):
            amount, unit = self.split_ingredient_amounts_and_units(
                amounts_for_10[i])
            if not self.ingredient_already_added(ingr_names[i]):
                ingr_dict = {
                    'ingredient': ingr_names[i], 'amount': amount, 'unit': unit}
                self.ingredients.append(ingr_dict)
            else:
                self.add_to_existing_ingredient(ingr_names[i], amount, unit)
        self.convert_units()

    def add_to_existing_ingredient(self, ingredient: str, amount: float, unit: str):
        for ingr in self.ingredients:
            if ingr['ingredient'].lower() == ingredient.lower():
                if ingr['unit'].lower() == unit.lower():
                    ingr['amount'] += amount
                else:
                    print("Could not add", ingredient, amount, unit, "to",
                          ingr['ingredient'], ingr['amount'], ingr['unit'], "because unit did not match")

    def ingredient_already_added(self, ingredient: str) -> bool:
        for item in self.ingredients:
            if item['ingredient'].lower() == ingredient.lower():
                return True
        return False

    def convert_units(self):
        spices = ['basil', 'black pepper', 'turmeric', 'chili/cayenne']
        for item in self.ingredients:
            # spices are always ordered in a certain amount
            if item['ingredient'].lower() in spices:
                item['amount'] = 100
                item['unit'] = "g"
            elif item['ingredient'].lower() == "salt":
                item['amount'] = 1
                item['unit'] = 'kg'
            elif item['unit'].lower() == "l" and item['ingredient'].lower() != "soy sauce":
                item['unit'] = "kg"
            elif item['ingredient'].lower() == "soy sauce":
                item['amount'] = 3
                item['unit'] = 'l'
        print(self.ingredients)

    def split_ingredient_amounts_and_units(self, item):
        amount_and_unit = item.split(" ")
        amount: float = float(amount_and_unit[0].replace(",", "."))
        unit: str = amount_and_unit[1]
        return amount, unit
