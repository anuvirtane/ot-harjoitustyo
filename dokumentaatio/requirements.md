# Requirements

## Use of this application

 
This application has been planned and implemented to help one make food orders for 10 day meditation courses. The program reads a text file (.txt) with recipes for 11 days (11 days because on the evening of arrival a meal is also served). Based on how many people will be attending the course, it calculates the food amounts needed and saves them in four separate files (.txt) for food ordering. There needs to be four separate files because there are two times the wholesaler delivers food for the course and some of the food products are purchased prior to the course from two different locations (for saving purposes). If there are dry food product leftovers from the previous course, they can be given to the program in a text file. The program will read the file and subtract the amounts from the food order.

## Users

There is only one user role for the application. 


## User interface

Graphical user interface with functions to:

- give amount of people on the course to calculate food amounts
- show location of order files generated


## Functionality in basic version

### "Minimum viable product:"


 **user can give a file/files with recipes and amount of people attending the course, and get four files with food order amounts**

 - program (class RecipeReader) *done*
    - reads file/files with recipes
    - finds the part of recipe where ingredients are
    - checks ingredient units and converts them if necessary (eg. l to kg)
    - saves ingredients in dicts and dicts in list. Dict format: {"ingredient": ingredient, "amount": amount, "unit": unit}

- program (class OrderMaker) *done*
    - saves ingredient dicts in a list, and adds same ingredient amount to that ingredient *done*
    - calculates correct amounts according to how many people user asks amounts for *done*
    - knows which ingredient goes to which order file and puts them there *todo*

- program locig (class Logic) *done*
    - coordinates use of RecipeReader and OrderMaker class instances
    - returns location of order files generated


- program has graphical user interface *done*
    - user gives amount of eaters
    - user gets location of food order files generated


### What would be really nice to have as well

- user can give a file with leftover food amounts from previous course and they will be subtracted from the food order files
- food order files are saved and user can retrieve them
- user can add and save comments to any food order file


## Future development ideas

When basic version has been implemented, further functionalities can be added

- the food amounts in the original recipes file can be adjusted if needed
- the program makes the recipes file "look nice" and easy to read when amounts are adjusted
- user is not bound to having four food order files but can decide how many food order files and what ingredients go to which file


