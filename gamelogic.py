from tkinter import Label
class GameLogic:
    def __init__(self, root, user):
        self.root = root
        self.winner = ""

        # Self.User is inherited from titlescreen, it's the choice of cross or circle.
        # Currently, the user always starts. The AI (that's yet to be programmed) will take next turn,
        # once second games have been implemented.
        self.user = user
        self.turn = self.user
        self.win = False
        self.tie = False
        self.fields = ['white','white','white','white','white','white','white','white','white']
    def switch_turn(self):
        if self.turn == "circle":
            self.turn = "cross"
        else:
            self.turn = "circle"
    def update(self, id, image):
        self.fields[id-1] = image

        self.checkwin()
        if(self.win):
            self.winner = image
            self.stopgame()
            self.root.print_winner(self.winner)
        elif(self.tie):
            self.stopgame()
            self.root.print_winner(self.winner)

            
    def stopgame(self):
            for x in self.root.fields:
                x.unb()


    def checkwin(self):

        #Check if any winning conditions are true: Numlock grid is used to resemble game grid, so 789 would be the top layer
        #789 horizontal
        if(self.fields[0] == self.fields[1] == self.fields[2] and self.fields[0] != 'white'):
            self.win = True
        #456 horizontal
        elif(self.fields[3] == self.fields[4] == self.fields[5] and self.fields[3] != 'white'):
            self.win = True
        #123 horizontal
        elif(self.fields[6] == self.fields[7] == self.fields[8] and self.fields[6] != 'white'):
            self.win = True
        #753 diagonal
        elif(self.fields[0] == self.fields[4] == self.fields[8] and self.fields[0] != 'white'):
            self.win = True
        #951 diagonal
        elif(self.fields[2] == self.fields[4] == self.fields[6] and self.fields[2] != 'white'):
            self.win = True
        #741 vertical
        elif(self.fields[0] == self.fields[3] == self.fields[6] and self.fields[0] != 'white'):
            self.win = True
        #852 vertical
        elif(self.fields[1] == self.fields[4] == self.fields[7] and self.fields[1] != 'white'):
            self.win = True
        #963 vertical
        elif(self.fields[2] == self.fields[5] == self.fields[8] and self.fields[2] != 'white'):
            self.win = True
        elif(not self.fields.__contains__('white') and self.win == False):
            self.tie = True
        else:
            self.win = False
        
        
        
        

