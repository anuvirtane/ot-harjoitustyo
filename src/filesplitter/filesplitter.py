from recipereader.recipereader import RecipeReader

class FileSplitter():
    """Reads file given at class instance creation,
    and finds recipe ingredients in it, even if there are many recipes. Splits
    the text read from file into lists of recipe ingredients"""

    def __init__(self, recipe_file: str = "files/Day1.txt"):
        self.recipe_file = recipe_file
        self.recipe: str = ''
        self.ingredients_lists: list [list] = []
        self.all_ingredients_found = False
        self.recipereader = RecipeReader()

    def read(self):
        """Reads recipe file given as argument to class instance
        and saves it as self.recipe"""
        try:
            with open(self.recipe_file, "r") as file:
                self.recipe = file.read()
            self.find_ingredients()
        except Exception as exc:
            print("Something went wrong in reading recipe file:", exc)

    def find_ingredients(self):
        rows = self.recipe.split("\n")
        while not self.all_ingredients_found:
            rows = self.pick_rows_with_ingredients(rows)
            

    def pick_rows_with_ingredients(self, list_to_check_for_ingredients: list):
        rows = list_to_check_for_ingredients
        try:
            i = 0
            ingredients_start_row_found = False
            ingredients_end_row_found = False

            for i in range(len(rows)-1):
                if rows[i - 1].lower() == "ingredients":
                    ingredients_start_row = i
                    ingredients_start_row_found = True
                    # print(f"Starting from row {ingredients_start_row} ingredients will soon be listed")
                    # print(rows[i])
                if rows[i + 1] == '' and rows[i + 2] == '' and ingredients_start_row_found and i > ingredients_start_row + 20:
                #if "preparations" in rows[i + 1].lower() and ingredients_start_row_found:
                    ingredients_end_row_found = True
                    ingredients_end_row = i
                    # print(f"Before row {i} are ingredients")
                    # print(rows[i])
                if ingredients_start_row_found and ingredients_end_row_found:
                    self.save_ingredients_lists(rows[ingredients_start_row:ingredients_end_row])
                    return rows[ingredients_end_row:]
                #self.ingredients = rows[ingredients_start_row:ingredients_end_row]
               # print(rows[ingredients_start_row:ingredients_end_row])
                continue
            else:
                self.all_ingredients_found = True
                print(self.ingredients_lists)
                print(len(self.ingredients_lists))
                # print("""The file given does not seem to contain recipes in a format
                # that this program can read. The program starts reading from 'Ingredients' and
                # stops reading at 'Preparations' and if they are missing, the program does not find anything""")
        except Exception as exc:
            print(
                f"Something went wrong in finding ingredients from recipe text: {exc}")

    def save_ingredients_lists(self, list_to_append: list):
        """Contains workaround for extra words having gone into ingredients due to xml format changing
        when .docx or .odt file has been saved as txt and rows having been formed in strange places at times"""
        if "instructions" in list_to_append:
            list_to_append_too = self.remove_item_from_list("See ", list_to_append)
            list_to_append_again = self.remove_item_from_list("instructions", list_to_append_too)
            self.ingredients_lists.append(list_to_append_again)
        #list_to_append_again = self.remove_item_from_ingredients("instructions", list_to_append_too)
        else:
            self.ingredients_lists.append(list_to_append)  

    def remove_item_from_list(self, item_to_be_removed: str, list_to_remove_from: list) -> list:
        """Removes unwanted item from list"""
        ingr_list = [item for item in list_to_remove_from]
        ingr_list.remove(item_to_be_removed)
        return [item for item in ingr_list]

