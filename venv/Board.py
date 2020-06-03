class Board_Game:
    def __init__ (self, board = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,], used_spaces= None ):
        self.board = board
        self.used_spaces = used_spaces
        #create new list if one hasn't been
        if self.used_spaces is None:
            self.used_spaces = []
        self.done = False

#print tic tac toe board in lines and columns
    def print_board (self):
        print("""
            {} | {} | {}
            ---------
            {} | {} | {}
            ---------
            {} | {} | {}
    """.format(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6], self.board[7], self.board[8]))

    def clear_board (self):
##        for x in self.board: not working
##            x = ' '
##            print (x)
        self.used_spaces.clear() #clear taken spaces?
        for x in range (0, 9):
            self.board[x] = ' '
            x+=1

    #checks for taken spaces on board and adds positions to list
    def taken_spaces (self):
        #for x in self.board:#weird'
        for x in range (0, 9):
            #if space is taken and space isn't already in list add to used_spaces
            if (self.board[x] != ' ' and not(x in self.used_spaces)):
                self.used_spaces.append(x)

    def tie (self):
        #check if all spaces are used and no one won
        if ((len(self.used_spaces) == 9) and not self.done):
            self.print_board()
            self.done = True
            print ("TIE")

    def across (self, player):
        for x in range (0,9,3):
            if (self.board[x] != ' '):
                one = self.board[x]
                two = self.board[x+1]
                three = self.board[x+2]

                if((f"{one}") == (f"{two}") == (f"{three}")):
                    self.print_board()
                    self.done = True
                    print(player.name + " WINS")

                # exit ("WINNER ")

    def down (self,player):
        for x in range (0,3):
            if (self.board[x] != ' '):
                one = self.board[x]
                two = self.board[x+3]
                three = self.board[x+6]

                if((f"{one}") == (f"{two}") == (f"{three}")):
                    self.print_board()
                    self.done = True
                    print(player.name + " WINS")


                    #exit ("WINNER")


    def diagonal (self,player):
        if (self.board[4] != ' '):
            if((self.board[0]) == (self.board[4]) == (self.board[8])):
                self.print_board()
                self.done = True
                print(player.name + " WINS")

                #exit ("WINNER")

            elif((self.board[2]) == (self.board[4]) == (self.board[6])):
                self.print_board()
                self.done = True
                print(player.name + " WINS")

                #exit ("WINNER")



    def game_over (self,player):#add player and their char
        self.down(player)
        self.across(player)
        self.diagonal(player)
        self.tie()
        if self.done:
            exit()



    #place X or O on board, provided it's valid space and not taken
    def place_value (self, num, char, player):
        num = int(num) #if char is entered doesn't work, maybe have some dif check
        #number not on board #0 WORKS/???
        if (not(1 <= num <= 9)):
            num = input("That square is invalid, please enter a number between 1 and 9, representing the square you choose ")
            self.place_value(num, char,player)
        elif ((num-1) in self.used_spaces):
            num = input("That square is taken, please enter a number between 1 and 9, representing the square you choose ")
            return self.place_value(num, char,player)
        else:
            self.board[num-1] = char
        self.taken_spaces() #update taken spaces'
        self.game_over(player)

    def start(self):
        print("This is the board with numerical representations of each square")
        self.print_board()
        self.clear_board()

    def next_turn (self):
        pass


