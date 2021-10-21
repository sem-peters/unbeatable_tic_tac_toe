from tkinter import Label
from ai import AI
class GameLogic:
    def __init__(self, root, startinguser, user, ai):
        self.parent = root
        self.winner = ""
        self.startinguser = startinguser
        # Self.User is inherited from titlescreen, it's the choice of cross or circle.
        # Currently, the user always starts. The AI (that's yet to be programmed) will take next turn,
        # once second games have been implemented.
        self.user = user
        self.ai = ai
        self.turn = self.startinguser
        self.win = False
        self.tie = False
        self.fields = ['white','white','white','white','white','white','white','white','white']
        self.first_turn()

    def first_turn(self):
        if(self.turn == self.ai):
            self.opponentAI = AI(self, self.ai)
            self.opponentAI.make_move()
    def switch_turn(self):

        self.opponentAI = AI(self, self.ai)
        if self.turn == self.parent.user:
            self.turn = self.parent.ai
            self.opponentAI.make_move()
        else:
            self.turn = self.parent.user
        
    def update(self, id, image):
        self.fields[id] = image
        self.checkwin()
        if(self.win or self.tie):
            self.freezegame()
            self.parent.print_winner(self.winner)

    def freezegame(self):
            for x in self.parent.fields:
                x.unb()


    def checkwin(self):

        #Check if any winning conditions are true: Numlock grid is used to resemble game grid, so 789 would be the top layer
        #789 horizontal
        if(self.fields[0] == self.fields[1] == self.fields[2] and self.fields[0] != 'white'):
            self.winner = self.fields[0]
            self.win = True
        #456 horizontal
        elif(self.fields[3] == self.fields[4] == self.fields[5] and self.fields[3] != 'white'):
            self.winner = self.fields[3]
            self.win = True
        #123 horizontal
        elif(self.fields[6] == self.fields[7] == self.fields[8] and self.fields[6] != 'white'):
            self.winner = self.fields[6]
            self.win = True
        #753 diagonal
        elif(self.fields[0] == self.fields[4] == self.fields[8] and self.fields[0] != 'white'):
            self.winner = self.fields[0]
            self.win = True
        #951 diagonal
        elif(self.fields[2] == self.fields[4] == self.fields[6] and self.fields[2] != 'white'):
            self.winner = self.fields[2]
            self.win = True
        #741 vertical
        elif(self.fields[0] == self.fields[3] == self.fields[6] and self.fields[0] != 'white'):
            self.winner = self.fields[0]
            self.win = True
        #852 vertical
        elif(self.fields[1] == self.fields[4] == self.fields[7] and self.fields[1] != 'white'):
            self.winner = self.fields[1]
            self.win = True
        #963 vertical
        elif(self.fields[2] == self.fields[5] == self.fields[8] and self.fields[2] != 'white'):
            self.winner = self.fields[2]
            self.win = True
        elif(not self.fields.__contains__('white') and self.win == False):
            self.winner = ''
            self.tie = True
        else:
            self.win = False
        
        
        
        

