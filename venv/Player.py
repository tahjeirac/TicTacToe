class Player:
    def __init__ (self, name, pos, char ):
        self.name = name
        self.pos = pos
        self.char = char

        if self.pos == 1:
            self.current_player = True
        else:
            self.current_player = False
        print("hello " + self.name + " you are player " + str(self.pos) + " and your charachter is " + self.char)

    def next_player(self, next_player):
        self.current_player = False
        next_player.current_player = True
        print ("It is " + next_player.name + "'s turn")

