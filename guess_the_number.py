# using python3
import simpleguitk as simplegui
import random

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
CHANCE_100 = 7
CHANCE_1000 = 10

secret_number = random.randrange(0, 100)
count = CHANCE_100
num_range = 100


# helper function to start and restart the game
def new_game(num):
    # initialize global variables used in your code here
    global secret_number, count
    count
    secret_number = random.randrange(0, num)
    print("New game. Range is [0, %d)" % num)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global count, num_range
    num_range = 100
    count = CHANCE_100
    new_game(num_range)


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global count, num_range
    num_range = 1000
    count = CHANCE_1000
    new_game(num_range)


def input_guess(guess):
    # main game logic goes here
    global secret_number, count
    count -= 1
    print("Number or remaining guesses is " + str(count))

    guess_number = int(guess)
    print("Guess was " + str(guess_number))

    if guess_number == secret_number:
        print("Correct!")
        new_game()
    elif count > 0:
        if guess_number < secret_number:
            print("Higher!")
        else:
            print("Lower!")

    else:
        print("You lose.")
        new_game(num_range)



# create frame
f = simplegui.create_frame("Guess the number", 100, 100)

# register event handlers for control elements and start frame
f.add_input("Input a number", input_guess, 50)
f.add_button("Range 100", range100, 100)
f.add_button("Range 1000", range1000, 100)

f.start()

# call new_game
new_game(num_range)


# always remember to check your completed program against the grading rubric


