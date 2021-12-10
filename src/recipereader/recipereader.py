from docx import Document

class RecipeReader():
    """Reads file given at class instance creation, 
    and finds recipe ingredients in it. Saves ingredients in dict.
    Dict format is {amount_of_eaters: [ingredient amount, 
    another ingredient amount,...], amount of eaters: [..]
    Ingredient amounts in dict lists are in 
    same order as items in self.ingredient_names list}"""
    def __init__(self, recipe_file: str = "files/Day0.txt"):
        self.recipe_file = recipe_file

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
        print("ingredients are")
        print(list_from_table[4])
        print("amounts for 10 people are")
        print(list_from_table[5])