# simple tic tac toe game with 2 players
#tommor ow - make players into class?
import random

#input player class
from Board import *
from Player import *





starting = False
#intalize board
b1 = Board_Game()

while not starting:
    choice = (input("Welcome to Tic Tac Toe, Enter 1 to START and 0 to QUIT "))
    if choice == '1':
        starting = True
    elif choice == '0':
        exit()

#setting up players
player1 = Player(str(input("What is your name? ")),random.randint(1, 2), 'X' )

if (player1.pos == 1) :
    player2 = Player(str(input("What is your name? ")), 2, 'O' )
else:
    player2 = Player(str(input("What is your name? ")), 1, 'O')

#show starting board
b1.start()

while (not b1.done):
    if player1.current_player:
        # stops user from entering input that isn't a number
        try:
            player1.next_player(player2)
            b1.place_value(input(player1.name + " please enter a number between 1 and 9, representing the square you choose "),player1.char,player1)
            b1.print_board()

        except ValueError:
            print('Non-numeric input')

    elif player2.current_player:
        # stops user from entering input that isn't a number
        try:
            player2.next_player(player1)
            b1.place_value(
                input(player2.name + " please enter a number between 1 and 9, representing the square you choose "),
                player2.char,player2)
            b1.print_board()
        except ValueError:
            print('Non-numeric input')
