# Name: Shahroz Siddiqi
# Date: June 17, 2016
# File: game.py
# Description: This is the card game Blackjack, rules are included in the game
# if you press the Instructions button

# Import Modules
from graphics import *
from button import Button
import random

# Define Functions

# Set up the GUI
def setupGUI():
    
    global win, hit_button, stand_button, quit_button, again_button, result, \
           dealer_score, player_score, dealer_msg, player_msg, start
    
    if start:

        # Draw Intro Screen GUI
        win = GraphWin("Black Jack", 500, 400)
        win.setCoords(0, 0, 500, 400)

        Image(Point(250, 200), "start_background.png").draw(win)

        logo = Image(Point(100, 295), "logo.png")
        logo.draw(win)

        play_button = Button(win, Point(250, 50), 100, 40, "PLAY",
                             "chartreuse3")
        play_button.activate()

        instruct_button = Button(win, Point(78, 50), 125, 40, "INSTRUCTIONS",
                                 "steelblue2")
        instruct_button.activate()

        exit_button = Button(win, Point(425, 50), 125, 40, "QUIT", "indianred")
        exit_button.activate()

        pt = win.getMouse()

        # Event Loop for intro screen buttons
        while not play_button.clicked(pt):

            # Quit button
            if exit_button.clicked(pt):
                win.close()

            # Instructions button
            elif instruct_button.clicked(pt):
                instruct_button.deactivate()

                # Draw Instructions GUI
                Image(Point(250, 200), "instruct_background.png").draw(win)

                play_button = Button(win, Point(250, 50), 100, 40, "PLAY",
                                     "chartreuse3")
                play_button.activate()

                instruct_button = Button(win, Point(78, 50), 125, 40,
                                         "INSTRUCTIONS", "steelblue2")

                exit_button = Button(win, Point(425, 50), 125, 40, "QUIT",
                                     "indianred")
                exit_button.activate()
                
                title = Text(Point(250, 375), "INSTRUCTIONS")
                title.setOutline("white")
                title.setStyle("bold")
                title.setFace("helvetica")
                title.setSize(18)
                title.draw(win)

                text = Text(Point(250, 320), "The goal of this game is to get "\
                            "a total of 21")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 300), "If you get 21 with your first "\
                            "two cards you automatically win")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 280), "If your total goes over 21 "\
                            "you bust, and the dealer wins")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)
                
                text = Text(Point(250, 260), "If the dealer's total goes over "\
                            "21, the dealer busts, and you win")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 240), "If both your totals are the same "\
                            "you tie, which is called a push")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win) 

                text = Text(Point(250, 220), "You can choose to stand if you "\
                            "think you may bust")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)
                
                text = Text(Point(250, 200), "and let the dealer do his turn")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)
                
                text = Text(Point(250, 180), "The same rules apply to the "\
                            "dealer, except when it's the")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 160), "dealer's turn, the dealer has "\
                            "to get cards until his total is more than 17")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)
                 
                text = Text(Point(250, 140), "Kings, Queens and Jacks are "\
                            "worth 10")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 120), "Aces can be worth 1 or 11 "\
                            "depending on what's more favourable")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win)

                text = Text(Point(250, 100), "All other cards are worth "\
                            "their numerical value")
                text.setOutline("white")
                text.setSize(11)
                text.setStyle("bold")
                text.draw(win) 
                
                pt = win.getMouse()

    # Draw Game GUI        
    Image(Point(250, 200), "game_background.png").draw(win)
    time.sleep(0.25)
    title = Text(Point(250, 375), "Black Jack")
    title.setOutline("white")
    title.setSize(15)
    title.setFace("helvetica")
    title.draw(win)

    Image(Point(175, 375), "logo_small.png").draw(win)
    Image(Point(325, 375), "logo_small.png").draw(win)

    dealer_title = Text(Point(45, 325), "Dealer")
    dealer_title.setOutline("white")
    dealer_title.setStyle("bold")
    dealer_title.draw(win)

    player_title = Text(Point(45, 135), "Player")
    player_title.setOutline("white")
    player_title.setStyle("bold")
    player_title.draw(win)

    dealer_score = Text(Point(90, 325), "")
    dealer_score.setOutline("white")
    dealer_score.setStyle("bold")
    dealer_score.draw(win)

    player_score = Text(Point(90, 135), "")
    player_score.setOutline("white")
    player_score.setStyle("bold")
    player_score.draw(win)
    
    result = Text(Point(250, 165), "")
    result.setOutline("white")
    result.setStyle("bold")
    result.draw(win)

    dealer_msg = Text(Point(430.25, 250), "")
    dealer_msg.setOutline("white")
    dealer_msg.setStyle("bold")
    dealer_msg.draw(win)

    player_msg = Text(Point(430.25, 60), "")
    player_msg.setOutline("white")
    player_msg.setStyle("bold")
    player_msg.draw(win)

    hit_button = Button(win, Point(140, 165), 70, 30, "HIT", "gold2")
    hit_button.activate()

    stand_button = Button(win, Point(360, 165), 70, 30, "STAND", "gold2")
    stand_button.activate()

    quit_button = Button(win, Point(455, 375), 70, 30, "QUIT", "indianred")
    quit_button.activate()

    again_button = Button(win, Point(45, 375), 70, 30, "AGAIN", "chartreuse3")

# Returns a shuffled deck of cards as a list
def build_deck():
    deck = []  
    for i in range(2,11):
          for j in ['C', 'D', 'H', 'S']:
              deck += [str(i) + j]         
    for i in ['J', 'Q', 'K', 'A']:
          for j in ['C', 'D', 'H', 'S']:
              deck += [str(i) + j]
    random.shuffle(deck)
    return deck

# Returns the value of a card
def value(card):
    if card[0] in ['J', 'Q', 'K']:
        card_value = 10
    elif card[0] == 'A':
        card_value = 1
    elif card[0] == '1' and card[1] == '0':
        card_value = 10
    else:
        card_value = int(card[0])
    return card_value

# Deal with aces
def aces(total):

    if total.count(1) > 0 or total.count(11) > 0:

        # Checks if ace is 11 and changes it to 1 if needed
        for x in range(total.count(11)):
            if sum(total) - 10 <= 21:
                total[total.index(11)] = 1

        # Checks if ace is 1 and changes it to 11 if needed
        for x in range(total.count(1)):
            if sum(total) + 10 <= 21:
                total[total.index(1)] = 11
                
    return total

# Initialize Game
def initialize():
    
    # Initialize Variables
    player_total = []
    dealer_total = []
    x_player = 100

    # Setup GUI
    setupGUI()

    # Build the deck
    deck = build_deck()

    # Deal starting cards
    dealer_total, player_total, flip_card = start_deck(deck, dealer_total,
                                                       player_total)
    # Check for blackjack
    blackjack(player_total, dealer_total, flip_card)

    return player_total, dealer_total, x_player, deck, flip_card
    
# Deal out starting cards
def start_deck(deck, dealer_total, player_total):
    
    # Initialize Variables
    x_player = 50
    x_dealer = 50
    
    # Give dealer two cards and to dealer total
    Image(Point(x_dealer, 250), "./cards/" + str(deck[0]) + ".png").draw(win)
    dealer_total += [value(deck[0])]
    del(deck[0])
    x_dealer += 25
    Image(Point(x_dealer, 250), "./cards/stock.png").draw(win)
    dealer_total += [value(deck[0])]
    flip_card = deck[0]
    del(deck[0])

    # Give player two cards and add to player total
    for i in range(2):
        Image(Point(x_player, 60), "./cards/" + str(deck[0]) + ".png").draw(win)
        player_total += [value(deck[0])]
        del(deck[0])
        x_player += 25

    # Deal with aces
    player_total = aces(player_total)
    dealer_total = aces(dealer_total)

    # Draw player total and dealer total to the screen
    dealer_score.setText(dealer_total[0])
    player_score.setText(sum(player_total))

    return dealer_total, player_total, flip_card

# Check for blackjack
def blackjack(player_total, dealer_total, flip_card):

    if sum(player_total) == 21 or sum(dealer_total) == 21:
        time.sleep(0.75)
        
        # Reveal dealer's card
        Image(Point(75, 250), "./cards/" + flip_card + ".png").draw(win)

        # Draw dealer total to the screen
        dealer_score.setText(sum(dealer_total))

        hit_button.deactivate()
        stand_button.deactivate()
        again_button.activate()

        # Check who has blackjack
        if sum(player_total) == 21:
            player_msg.setText("Blackjack!")

        if sum(dealer_total) == 21:
            dealer_msg.setText("Blackjack!")

        # Decide who won or push
        if sum(dealer_total) == sum(player_total):
            result.setText("Push")
        elif sum(dealer_total) > sum(player_total):
            result.setText("Dealer Wins!")
        elif sum(dealer_total) < sum(player_total):
            result.setText("Player Wins!")

# Hit Button
def hit(player_total, dealer_total, deck, x_player, flip_card):

    # Deal cards to the player and add to player total
    Image(Point(x_player, 60), "./cards/" + str(deck[0]) + ".png").draw(win)
    player_total += [value(deck[0])]
    del(deck[0])

    # Deal with aces
    player_total = aces(player_total)

    # Draw player total to the screen
    player_score.setText(sum(player_total))

    # Check for bust
    if sum(player_total) > 21:
        player_msg.setText("Player Bust!")
        hit_button.deactivate()
        stand_button.deactivate()

        # Dealer's turn
        dealers_turn(dealer_total, player_total, deck, flip_card)

    return player_total, deck

# Does the dealer's turn
def dealers_turn(dealer_total, player_total, deck, flip_card):
    x_dealer = 100

    # Reveal dealer's card
    Image(Point(75, 250), "./cards/" + flip_card + ".png").draw(win)

    # Draw dealer total to the screen
    dealer_score.setText(sum(dealer_total))

    # Check for bust
    if sum(player_total) > 21:
        result.setText("Dealer Wins!")
        again_button.activate()

    else:
        # Deal cards to dealer and add to dealer total
        while sum(dealer_total) < 17:
            time.sleep(1)
            Image(Point(x_dealer, 250), "./cards/" + str(deck[0]) +
                  ".png").draw(win)
            dealer_total += [value(deck[0])]
            del(deck[0])
            x_dealer += 25

            # Deal with aces
            dealer_total = aces(dealer_total)

            # Draw dealer total to the screen
            dealer_score.setText(sum(dealer_total))

        # Decide who won or push
        if sum(dealer_total) <= 21:
            
            if sum(player_total) > sum(dealer_total):
                result.setText("Player Wins!")
                again_button.activate()

            elif sum(player_total) < sum(dealer_total):
                result.setText("Dealer Wins!")
                again_button.activate()

            elif sum(player_total) == sum(dealer_total):
                result.setText("Push")
                again_button.activate()
        else:
            result.setText("Player Wins!")
            dealer_msg.setText("Dealer Bust!")
            again_button.activate()

##################
#  Main program  #
##################

# Initialize Game
start = True
player_total, dealer_total, x_player, deck, flip_card = initialize()

# Get mouse click
pt = win.getMouse()

# Event Loop
while not quit_button.clicked(pt):

    # Hit Button
    if hit_button.clicked(pt):
        player_total, deck = hit(player_total, dealer_total, deck, x_player,
                                 flip_card)
        x_player += 25

    # Stand Button
    elif stand_button.clicked(pt):
        hit_button.deactivate()
        stand_button.deactivate()

        # Dealer's turn
        dealers_turn(dealer_total, player_total, deck, flip_card)

    # Again Button
    elif again_button.clicked(pt):

        # Initialize Game
        start = False
        player_total, dealer_total, x_player, deck, flip_card = initialize()
        
    # Get mouse click
    pt = win.getMouse()

# Closes the window   
win.close()
