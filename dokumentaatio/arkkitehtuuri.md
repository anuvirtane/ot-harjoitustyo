
# Architecture


## User interface
At the moment there is a temporary text user interface. There will be a graphical user interface with views for user to
- input amount of eaters
- input which recipe files to user
- generate order

## Application logic
Application logic consists of classes [RecipeReader](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/src/recipereader/recipereader.py) and [OrderMaker](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/src/ordermaker/ordermaker.py)

![Classes](../files/classes.jpg)

## Files

Application has recipe files in its files/ folder during development. The future version will ask for user input to know which recipe files to use, and will generate order amounts based on the recipes in the files.

Application will generate four food order files based on info given by user. This has not been implemented yet.





