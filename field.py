from tkinter import *
from gamelogic import GameLogic
game = GameLogic()

class field(Canvas):
    
    def __init__(self, master, width, height, c, r):
        self.master = master
        self.width = width
        self.height = height
        self.c = c
        self.r = r
        self.canvas = Canvas(self.master, width=self.width, height=self.height)
        self.canvas.grid(column=self.c, row=self.r)
        self.white = PhotoImage(master=self.master, file="images/white.png")
        self.cross = PhotoImage(master=self.master, file="images/cross.png")
        self.circle = PhotoImage(master=self.master, file="images/circle.png")
        self.canvas.create_image(0,0,anchor=NW, image=self.white)
        self.canvas.bind("<Button-1>", self.clickhandler)

    def turn_cross(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.cross)
    def turn_circle(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.circle)
    def turn_white(self):
        self.canvas.create_image(0,0,anchor=NW, image=self.white)
    
    def clickhandler(self, event):
        if(game.turn == "circle"):
            self.turn_circle()
            game.switch_turn()
        else:
            self.turn_cross()
            game.switch_turn()

