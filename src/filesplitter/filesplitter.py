class FileSplitter():
    """Reads file given at class instance creation,
    and finds recipe ingredients in it, even 
    if there are many recipes. Splits
    the text read from file into lists of recipe ingredients"""

    def __init__(self, recipe_file: str = "files/Day1.txt"):
        self.recipe_file = recipe_file
        self.recipe: str = ''
        self.ingredients_lists: list[list] = []
        self.all_ingredients_found = False

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
        try:
            rows = self.recipe.split("\n")
            while not self.all_ingredients_found:

                rows = self.pick_rows_with_ingredients(rows)
        except Exception as exc:
            print(
                "Something went wrong with finding ingredients from the recipe text:",
                exc)

    def pick_rows_with_ingredients(self, list_to_check_for_ingredients: list):
        rows: list[str] = list_to_check_for_ingredients
        try:
            i = 0
            ingredients_start_row_found = False
            ingredients_end_row_found = False
            recipe_is_rice_recipe = False
            for i in range(len(rows)-1):
                if rows[i - 1].lower() == "ingredients":
                    ingredients_start_row = i
                    ingredients_start_row_found = True
                if rows[i + 1] == '' and rows[i + 2] == '' and ingredients_start_row_found and i > ingredients_start_row + 20:
                    ingredients_end_row_found = True
                    ingredients_end_row = i
                if ingredients_start_row_found and ingredients_end_row_found:
                    for item in rows[ingredients_start_row:ingredients_end_row+1]:
                        if item.lower() == "rice":
                            recipe_is_rice_recipe = True
                        if item.lower() == "\trice":
                            recipe_is_rice_recipe = True
                    if not recipe_is_rice_recipe:
                        self.append_to_ingredients_lists(
                            rows[ingredients_start_row:ingredients_end_row+1])

                    return rows[ingredients_end_row+1:]
                #continue
                else:
                    self.all_ingredients_found = True
                    print(self.ingredients_lists)
                    print(len(self.ingredients_lists))

        except Exception as exc:
            print(
                f"Something went wrong in finding ingredients from recipe text: {exc}")

    def append_to_ingredients_lists(self, list_to_append: list):
        """Contains workaround for extra words having gone into 
        ingredients due to xml format changing
        when .docx or .odt file has been saved as txt and 
        rows having been formed in strange places at times"""
        if "instructions" in list_to_append:
            list_to_append_too = self.remove_item_from_list(
                "See ", list_to_append)
            list_to_append_again = self.remove_item_from_list(
                "instructions", list_to_append_too)
            self.ingredients_lists.append(list_to_append_again)
        #list_to_append_again = self.remove_item_from_ingredients("instructions", list_to_append_too)
        else:
            self.ingredients_lists.append(list_to_append)

    def remove_item_from_list(self, item_to_be_removed: str, list_to_remove_from: list) -> list:
        """Removes unwanted item from list"""
        ingr_list = list(list_to_remove_from)
        ingr_list.remove(item_to_be_removed)
        return list(ingr_list)
