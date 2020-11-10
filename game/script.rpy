# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amy")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "amy happy.png" to the images
    # directory.

    show amy happy

    # These display lines of dialogue.

    "Welcome to Industri Co. Congratulations on your first day!"

    a "Huh?? How did I get here."

    a "New job!? I barely remember being interviewed."


    # This ends the game.

    return
