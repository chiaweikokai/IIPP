# implementation of card game - Memory

import simpleguitk as simplegui
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 130
CARD_WIDTH = CANVAS_WIDTH // 16

FONT_SIZE = 50
EXPOSED = True
UNEXPOSED = False
NO_CARD_EXPOSED = 0
ONE_CARD_EXPOSED = 1
state = NO_CARD_EXPOSED
current_card = 0
previous_click = 0
card_list = []
exposed = []
turns_count = 0


# helper function to initialize globals
def new_game():
    global card_list, exposed, turns_count, label
    card_list = []
    exposed = []
    turns_count = 0
    label.set_text("Turns = %d" % turns_count)
    card_list.extend([[num, UNEXPOSED] for num in range(1, 9)])
    card_list.extend([[num, UNEXPOSED] for num in range(1, 9)])
    random.shuffle(card_list)
    # print(card_list)


# define event handlers
def mouse_click(pos):
    # add game state logic here
    global state, exposed, current_card, previous_click, turns_count, label
    card_clicked = pos[0] // CARD_WIDTH
    if state == NO_CARD_EXPOSED:
        card_list[card_clicked][1] = EXPOSED
        current_card = card_list[card_clicked][0]
        previous_click = card_clicked
        turns_count += 1
        state += 1
    elif state == ONE_CARD_EXPOSED:
        card_list[card_clicked][1] = EXPOSED
        if card_clicked != previous_click:
            if card_list[card_clicked][0] == current_card:
                exposed.append(current_card)
            previous_click = card_clicked
            state += 1
    else:
        if card_clicked != previous_click and card_list[card_clicked][1] == UNEXPOSED:
            for card in card_list:
                if card[0] not in exposed:
                    card[1] = UNEXPOSED
            card_list[card_clicked][1] = EXPOSED
            current_card = card_list[card_clicked][0]

            previous_click = card_clicked
            turns_count += 1
            state = 1

    label.set_text("Turns = %d" % turns_count)


# cards are logically 50x100 pixels in size
def draw(canvas):
    card_pos = 0
    for card in card_list:
        if card[1] == EXPOSED:
            canvas.draw_text(str(card[0]),
                             [card_pos + CARD_WIDTH * 0.2, CANVAS_HEIGHT * 0.65],
                             FONT_SIZE, "White")

        else:
            canvas.draw_polygon([[card_pos, 0],
                                 [card_pos + CARD_WIDTH, 0],
                                 [card_pos + CARD_WIDTH, CANVAS_HEIGHT],
                                 [card_pos, CANVAS_HEIGHT]],
                                1, "Black", "Green")
        card_pos += CARD_WIDTH

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = %d" % turns_count)

# register event handlers
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



