
# Architecture


## User interface
At the moment there is a temporary text user interface. There will be a graphical user interface with views for user to
- input amount of eaters
- input which recipe files to user
- generate order

## Application logic
Application logic consists of classes [RecipeReader](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/src/recipereader/recipereader.py) and [OrderMaker](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/src/ordermaker/ordermaker.py) directed by class [Logic](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/src/logic/logic.py)

![Classes](../files/classes.jpg)

Logic creates instances of RecipeReader and OrderMaker. Recipereader instances read recipe files (.doxc), find ingredients from them and Logic passes the ingredients from the recipereaders to the ordermaker instance. Ordermaker generates order files for the amount of eaters user has inputted.

## Files

Application has recipe files in its files/ folder in this first MVP version. A future version could ask for user input to know which recipe files to use. Program generates order amounts based on the recipes in the files.






