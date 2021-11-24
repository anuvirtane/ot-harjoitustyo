class RecipeReader():
    """Reads file given at class instance creation, and finds recipe ingredients in it. Saves ingredients in dict.
    Dict format is {amount_of_eaters: [ingredient amount, another ingredient amount,...], amount of eaters: [..]
    Ingredient amounts in dict lists are in same order as items in self.ingredient_names list}"""
    def __init__(self, recipe_file: str = "files/Day0.txt"):
        self.recipe_file = recipe_file
        self.recipe: str = ''
        self.ingredients: list [str] = []
        self.ingredients_dict: dict = {}
        self.ingredient_names: list [str] = []

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
        self.pick_rows_with_ingredients()
        self.clean_ingredients_list()
        self.create_ingredients_dict()
        self.add_ingredients_to_dict()

    def add_ingredients_to_dict(self):
        self.add_ingredients_names()
        self.save_ingredient_amounts_according_to_dict_keys()
        self.print_what_is_there_now()

    def print_what_is_there_now(self):
        print("Print for checking:\n")
        i = 0
        for key in self.ingredients_dict:
            print("\nCooking for", key)
            for i in range(len(self.ingredient_names)):
                print("ingredient:")
                print(self.ingredient_names[i])
                print("amount:")
                print(self.ingredients_dict[key][i])

    def get_ingredients_names(self):
        return self.ingredient_names

    def get_ingredients_dict(self):
        return self.ingredients_dict


    def save_ingredient_amounts_according_to_dict_keys(self):
        if self.check_amounts_are_even():
            beginning = 0
            list_len = len(self.ingredient_names)
            for key in self.ingredients_dict:
                self.ingredients_dict[key] = self.ingredients[beginning:list_len]
                beginning += len(self.ingredient_names)
                list_len += len(self.ingredient_names)                          

    def check_amounts_are_even(self):
        if len(self.ingredients) % len(self.ingredients_dict) != 0 or len(self.ingredients) / len(self.ingredients_dict) != len(self.ingredient_names):
            raise Exception("""Something has gone wrong after starting to sort ingredients read from file
            to ingredients dict.""")
        return True
        

    def add_ingredients_names(self):
        """Finds and removes ingredient names from self.ingredients and saves them to self.ingredient_names"""
        for item in self.ingredients:
            if item.lstrip()[0].isalpha():
                self.ingredient_names.append(item)
                self.remove_item_from_ingredients(item)

    def create_ingredients_dict(self):
        """Sets amounts of eaters as keys in self.ingredients_dict and removes them from self.ingredients"""
        self.set_person_amounts_as_dict_keys()
        for key in self.ingredients_dict:
            self.remove_item_from_ingredients(key) #remove person amounts from ingredients list
    
    def set_person_amounts_as_dict_keys(self):
        for item in self.ingredients:
            if item[-2:].lower() == " p": #person amounts are listed as e. g. '10 p'
                self.ingredients_dict[item] = []
        if len(self.ingredients_dict) == 0:
            raise Exception('''Unable to find person amounts from ingredients list. 
            The program assumes person amounts to be listed as "10 p" or such so that
            there is a number, a space and then a letter p''')

    def remove_item_from_ingredients(self, item_to_be_removed: str):
        """Removes values from self.ingredients that have been already put to their place elsewhere"""
        ingr_list = [item for item in self.ingredients]
        ingr_list.remove(item_to_be_removed)
        self.ingredients = [item for item in ingr_list]

    def clean_ingredients_list(self):
        self.ingredients = [item.replace('\t', '') for item in self.ingredients if item != '' and item != '\t']

    def pick_rows_with_ingredients(self):
        """Finds place where ingredients list begins and ends from self.recipe and saves that part as self.ingredients list"""
        try:
            rows = self.recipe.split("\n")
            i = 0
            ingredients_start_row_found = False
            ingredients_end_row_found = False
            for i in range(len(rows)-1):
                if rows[i - 1].lower() == "ingredients":
                    ingredients_start_row = i
                    ingredients_start_row_found = True
                   # print(f"Starting from row {ingredients_start_row} ingredients will soon be listed")
               # if rows[i + 1] == '' and rows[i + 2] == '' and ingredients_start_row_found and i > ingredients_start_row + 20:
                if "preparations" in rows[i + 1].lower() and ingredients_start_row_found:
                    ingredients_end_row_found = True
                    ingredients_end_row = i
                    #print(f"Before row {i} are ingredients")
            if ingredients_start_row_found and ingredients_end_row_found:
                self.ingredients = rows[ingredients_start_row:ingredients_end_row]
                print(rows[ingredients_start_row:ingredients_end_row])
            else:
                print("""The file given does not seem to contain recipes in a format
                that this program can read. The program starts reading from 'Ingredients' and
                stops reading at 'Preparations' and if they are missing, the program does not find anything""")   
        except Exception as exc:
            print(f"Something went wrong in finding ingredients from recipe text: {exc}")
           
            
  

