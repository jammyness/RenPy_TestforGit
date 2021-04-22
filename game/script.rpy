# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Amy", color="#22a6d6")
define b = Character("HR_Person", color ="#409952")
define c = Character("Michael", color = "#8a4ead") #Michael is the department head


# The game starts here.
# motion controls


label start:

    play sound "2_Day_1_Master.mp3" fadein 30.0
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

    show amy confused

    a "Huh?? How did I get here."

    a "New job!? I barely remember being interviewed. Why am I here?"

    show hr_person happy at right 

    b "Welcome! You must be the new recruit!"

    b "Did you read the new hire orientation manual "


    #flashback to interview 

    scene bg interviewroom
    show michael happy at right 
    show amy confused
    c "Hi Amy! I am your interviewer, Michael"

    a "Hi Michael. Nice to meet you! I am excited to learn more about Industri Co. and the role that you are hiring for."

    c "Ok. Let's get right to it! Tell me, Amy, why engineering?"
#Amy's reaction changes from confused to nervous
    show amy nervous 

menu:

    "I love helping people":
        jump biomedE

    "I want to do something creative":
        jump badend

    "I want lots of money and stability to be dangerously honest.":
        jump badend

    "I wanted a hands-on career.":
        jump mechE

    "I hate people and I didn't want to be in any career that involved people. Please, just the microscope and the desk and a closed unventilated room.":
        jump badend

    "I love being outside I would die being inside a building all day":
        jump badend

label badend:
    "You picked the wrong choice"
    return



label biomedE: 
    c "Welcome to the Biomedical Engineering Arm of IndustriCo"    
    return

