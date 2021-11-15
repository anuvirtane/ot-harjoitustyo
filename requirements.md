# Requirements

## Use of this application

<!-- Using this application enables one to keep track of when a certain song has last been played at band practice. Also saving song lyrics and song structures can be saved in Song Memory. -->
 
This application has been planned and implemented to help one make food orders for a 10 day meditation courses. The program reads a text file (Word or such) with recipes for 11 days (11 days because on the evening of arrival a meal is also served). Based on how many people will be attending the course, it calculates the food amounts needed and saves them in four separate files (.txt) for food ordering. There needs to be four separate files because there are two times the wholesaler delivers food for the course and some of the food products are purchased prior to the course from two different locations (for saving purposes). If there are dry food product leftovers from the previous course, they can be given to the program in a text file. The program will read the file and subtract the amounts from the food order.

## Users

There is only one user role for the application. 



## User interface

<!-- Song Memory user interface hierarchy of views:

- choose function -view which lists different functionalities:
    - add song -view
    - choose song -view which lists saved songs, under which there are options:
        - see song lyrics
            - edit song lyrics
        - see song structure
            - edit song structure
        - remove song
        - see when song has been played
    - list dates for last played songs -->

Graphical user interface with functions to:

- give location of text file with recipes to be read
- give amount of people on the course to calculate food amounts
- give location of text file with leftover food amounts from previous course (if it has been saved)
- get and save the generated files with food order amounts to user's computer
- get the food order files from previous courses 


## Functionality in basic version

### "Minimum viable product"

<!-- - user can add songs
- user can see songs listed
- user can see dates for song plays
- user can remove songs
- user can add date when song was played -->

- user can give a file with recipes and amount of people attending the course, and get four files with food order amounts

<!-- ### "Minimum viable product option 2"
- user can add songs
    - user can add song lyrics
    - user can see song lyrics
    - user can add song structures
    - user can see song structures  
- user can see songs listed
- user can remove songs -->

### What would be really nice to have as well

- user can give a file with leftover food amounts from previous course and they will be subtracted from the food order files
- food order files are saved and user can retrieve them
- user can add and save comments to any food order file


## Future development ideas

When basic version has been implemented, further functionalities can be added

- the food amounts in the original recipes file can be adjusted if needed
- the program makes the recipes file "look nice" and easy to read when amounts are adjusted
- user is not bound to having four food order files but can decide how many food order files and what ingredients go to which file

<!-- - rating songs, adding importance for song to be played
- adding a field for additional info about song
- deleting all info in app
- login functionality, chance to add multiple users
- user teams where everyone can see and edit song info
- chance to create multiple Song Memory lists  -->
