from tkinter import *
from gamelogic import GameLogic
from field import field
class TicTacToeGUI(Tk):
    def __init__(self, user, ai, score):
        
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", func=self.stop)
        self.root.title("TicTacToe by Sem Peters")
        self.root.resizable(False, False) # Frame is made specifically for certain height and width, not responsive.
        
        self.score = score
        self.play_again = False

        # The user is the choice of either circle or cross.
        # If it's empty, the user has clicked the exit button on the first screen,
        # indicating they don't want to play.

        self.user = user
        self.ai = ai
        if(self.user == ''):
            quit()
        
        # This determines who starts.
        
        if(self.score.counter % 2 == 0):
            self.game = GameLogic(self, self.user, self.user, self.ai)
        elif(self.score.counter % 2 != 0):
            self.game = GameLogic(self, self.ai, self.user, self.ai)
        #self.game = GameLogic(self, self.user, self.user, self.ai)
        
        # Gui works as follows:
        # Field_1 - Field_9 are the fields in which X or O is placed.
        self.field_1 = field(self.root, 200, 200, 0, 0, self.game, 0)
        self.field_2 = field(self.root, 200, 200, 1, 0, self.game, 1)
        self.field_3 = field(self.root, 200, 200, 2, 0, self.game, 2)
        self.field_4 = field(self.root, 200, 200, 0, 1, self.game, 3)
        self.field_5 = field(self.root, 200, 200, 1, 1, self.game, 4)
        self.field_6 = field(self.root, 200, 200, 2, 1, self.game, 5)
        self.field_7 = field(self.root, 200, 200, 0, 2, self.game, 6)
        self.field_8 = field(self.root, 200, 200, 1, 2, self.game, 7)
        self.field_9 = field(self.root, 200, 200, 2, 2, self.game, 8)
        self.fields = [self.field_1, self.field_2, self.field_3, self.field_4,
            self.field_5, self.field_6, self.field_7,self.field_8, self.field_9]
        
        
        
    def run(self):
        self.root.mainloop()
        
    def print_winner(self, winner):
        if(winner == self.user):
            winner_label = Label(self.root, text="We have a winner:\nYou!", font=("Courier", 12), padx=10, pady=5, relief='solid', borderwidth=2)
            winner_label.grid(column=1,row=0)
            self.score.user_score = self.score.user_score + 1
            print("Added: ", self.score.user_score)
        elif(winner == self.ai):
            winner_label = Label(self.root, text="We have a winner:\nthe Computer!", font=("Courier", 12), padx=10, pady=5, relief='solid', borderwidth=2)
            winner_label.grid(column=1,row=0)
            self.score.ai_score += 1
        else:
            winner_label = Label(self.root, text="We have a tie!", font=("Courier", 12), padx=10, pady=5, relief='solid', borderwidth=2)
            winner_label.grid(column=1,row=0)
            self.score.tie += 1
        play_again_button = Button(self.root, text="Play again", command=self.play).grid(column=1,row=1)
        stop_button = Button(self.root, text="Quit", command=self.stop).grid(column=1,row=2)
    
    def play(self):
        self.play_again = True
        self.root.destroy()
    def stop(self):
        self.play_again = False
        self.root.destroy()
        quit()


    def nothing(self):
        #purposely does nothing
        pass