# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amy", color="#22a6d6")
define b = Character("HR_Person", color ="#409952")
define c = Character("Michael", color = "#8a4ead") #Michael is the department head


# The game starts here.
# motion controls


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "amy happy.png" to the images
    # directory.

    show amy happy 


    #move amy to the right

    # These display lines of dialogue.

    "Welcome to Industri Co. Congratulations on your first day!"

    a "Huh?? How did I get here."

    a "New job!? I barely remember being interviewed. Why am I here?"

    show hr_person happy at right 

    b "Welcome! You must be the new recruit!"]

    b "Did you read the new hire orientation manual "


    menu:

    "It's a videogame.":
        jump game

    "It's an interactive book.":
        jump book

label game:

    m "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    m "It's like an interactive book that you can read on a computer or a console."

    jump marry

label marry:

    "And so, we become a visual novel creating duo."


    # This ends the game.
     

    return
