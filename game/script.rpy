# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define brian = Character("Brian")
image bg haveueverwentfast = im.Scale("haveueverwentfast.png", 1280,720)
define brian_normal = im.FactorScale(Image("brian.png"), .1)
image brian normal = brian_normal
image brian stretched = Frame(im.FactorScale(Image("brian.png"), .1),left=50,right=50)
image brian inverted = im.MatrixColor(brian_normal, im.matrix.invert())
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg haveueverwentfast

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show brian stretched

    # These display lines of dialogue.
    "HELLO"
    hide brian stretched
    show brian normal at left

    brian "i am brian"

    hide brian normal

    show brian inverted
    brian "asd;lfkja;sldkjf"

    # This ends the game.

    return
    
init python:
    style.window.background = Frame("haveueverwentfast.png", 10, 10)