from tkinter import *
from gamelogic import GameLogic

# The Field object inherits the Canvas class from tkinter,
# There are 9 fields. Each begins 'white', they can change to 'cross' and 'circle'.
class field(Canvas):
    
    def __init__(self, master, width, height, c, r, parent, id):
        self.id = id
        self.parent = parent
        self.master = master
        self.width = width
        self.height = height
        self.c = c #column placement
        self.r = r #row placement

        self.canvas = Canvas(self.master, width=self.width, height=self.height)
        self.canvas.grid(column=self.c, row=self.r)

        self.white = PhotoImage(master=self.master, file="images/white.png")
        self.cross = PhotoImage(master=self.master, file="images/cross.png")
        self.circle = PhotoImage(master=self.master, file="images/circle.png")

        self.canvas.create_image(0,0,anchor=NW, image=self.white)
        self.canvas.bind("<Button-1>", self.clickhandler)
        self.current_image = "white"
    def unb(self):
        self.canvas.unbind("<Button-1>")
    def turn_cross(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.cross)
        self.current_image = "cross"
    def turn_circle(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.circle)
        self.current_image = "circle"
    def turn_white(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.white)
        self.current_image = "white"
    
    
    def clickhandler(self, event):
        if(self.parent.game.turn == self.parent.game.user):
            if(self.current_image == "white"):
                if(self.parent.game.user == 'circle'):
                    self.turn_circle()
                else:
                    self.turn_cross()
                self.parent.game.update(self.id, self.current_image)
                if(not(self.parent.game.win or self.parent.game.tie)):
                    self.parent.game.switch_turn()


        


