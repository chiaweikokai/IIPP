# using python3
import simpleguitk as simplegui
import random

# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# first game parameters
secret_number = random.randrange(0, 100)
count = 7
num_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, count, num_range
    if num_range == 100:
        count = 7
    else:
        count = 10
    secret_number = random.randrange(0, num_range)
    print("New game. Range is [0, %d)" % num_range)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100

    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000

    new_game()


def input_guess(guess):
    # main game logic goes here
    global secret_number, count, num_range
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
        new_game()

# print first game message
print("Game Start. Range is [0, %d)" % num_range)

# create frame
f = simplegui.create_frame("Guess the number", 200, 100)

# register event handlers for control elements and start frame
f.add_input("Input a number", input_guess, 50)
f.add_button("Range 100", range100, 100)
f.add_button("Range 1000", range1000, 100)

f.start()



