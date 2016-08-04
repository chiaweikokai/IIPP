# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user41_4jWEVno4dk_6.py

import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hand_list = []

    def __str__(self):
        # return a string representation of a hand
        return "Hand card points: " + str(self.get_value())

    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        is_ace_in_list = False
        for card in self.hand_list:
            if card.get_rank() == 'A':
                is_ace_in_list = True
            hand_value += VALUES[card.get_rank()]

        if is_ace_in_list and hand_value <= 11:
            hand_value += 10

        return hand_value


# define deck class
class Deck:
    def __init__(self):
        self.deck_list = [(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck_list)

    def deal_card(self):
        # deal a card object from the deck
        if len(self.deck_list) == 0:
            self.deck_list = [(suit, rank) for suit in SUITS for rank in RANKS]

        suit, rank = self.deck_list.pop(0)
        card = Card(suit, rank)
        return card


# define event handlers for buttons
def deal():
    global outcome, in_play, deck, score

    # your code goes here
    deck.shuffle()

    global player, dealer
    player = Hand()
    dealer = Hand()

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    # Pressing the "Deal" button in the middle of the round
    # causes the player to lose the current round
    if in_play:
        score -= 1

    in_play = True


def hit():
    global in_play, player, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "You have busted! New deal?"
            score -= 1
            in_play = False
            # print("Current score: " + str(score))


def stand():
    global in_play, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

        in_play = False
        # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            outcome = "Player wins! New deal?"
            score += 1
        elif dealer.get_value() < player.get_value():
            outcome = "Player wins! New deal?"
            score += 1
        else:
            outcome = "Dealer wins! New deal?"
            score -= 1
            # print("Current score: " + str(score))


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    pos = 0
    for card in player.hand_list:
        card.draw(canvas, [50 + pos, 180])
        pos += CARD_SIZE[0]
        pos += 5

    pos = 0
    for card in dealer.hand_list:
        card.draw(canvas, [50 + pos, 400])
        pos += CARD_SIZE[0]
        pos += 5

    msg_pos = (150, 360)
    if in_play:

        canvas.draw_image(card_back,
                          [CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE,
                          [50 + CARD_BACK_CENTER[0], 400 + CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE)

        canvas.draw_text("Hit or stand?", msg_pos, 32, "White")
    else:
        canvas.draw_text(outcome, msg_pos, 32, "Yellow")
    score_color = "Aqua"
    if score < 0:
        score_color = "Red"
    canvas.draw_text("Player score: %d" % score, [360, 150], 24, score_color)
    canvas.draw_text("Blackjack", [150, 80], 60, "White")

    canvas.draw_text("Player's hand", [50, 150], 24, "White")
    canvas.draw_text("Dealer's hand", [50, 540], 24, "White")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deck = Deck()
deal()

frame.start()


