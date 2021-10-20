from tkinter import *
from gamelogic import GameLogic
from field import field
class TicTacToeGUI:
    def __init__(self) -> None:
        #this is empty because i got nothin yet
        self.root = Tk()
        self.root.title("TicTacToe by Sem Peters")

        # Gui works as follows:
        # Field_1 - Field_9 are the fields in which X or O is placed.
        self.game = GameLogic(self)
        self.field_1 = field(self.root, 200, 200, 0, 0, self.game, 1)
        self.field_2 = field(self.root, 200, 200, 1, 0, self.game, 2)
        self.field_3 = field(self.root, 200, 200, 2, 0, self.game, 3)
        self.field_4 = field(self.root, 200, 200, 0, 1, self.game, 4)
        self.field_5 = field(self.root, 200, 200, 1, 1, self.game, 5)
        self.field_6 = field(self.root, 200, 200, 2, 1, self.game, 6)
        self.field_7 = field(self.root, 200, 200, 0, 2, self.game, 7)
        self.field_8 = field(self.root, 200, 200, 1, 2, self.game, 8)
        self.field_9 = field(self.root, 200, 200, 2, 2, self.game, 9)
        self.fields = [self.field_1, self.field_2, self.field_3, self.field_4,
            self.field_5, self.field_6, self.field_7,self.field_8, self.field_9]
        
    def stopgame(self, condition):
        for x in self.fields:
            x.unb()
        if(condition == "win"):
            winnertext = "We have a winner:\n" + self.game.winner 
            self.winnerlabel = Label(self.root, text=winnertext, font=("Courier",12), relief="solid", borderwidth="3",padx=5,pady=5).grid(column=1,row=1)
        else:
            tietext = "We have a tie!"
            self.tielabel = Label(self.root, text=tietext, font=("Courier",12), relief="solid", borderwidth="3",padx=5,pady=5).grid(column=1,row=1)
    def nothing(self):
        #purposely does nothing
        pass