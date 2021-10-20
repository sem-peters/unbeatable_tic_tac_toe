from tkinter import *
from gamelogic import GameLogic


class field(Canvas):
    
    def __init__(self, master, width, height, c, r, game, id):
        self.id = id
        self.game = game
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
        if(self.game.turn == "circle" and self.current_image == "white"):
            self.turn_circle()
            self.game.switch_turn()
        elif(self.game.turn == "cross" and self.current_image == "white"):
            self.turn_cross()
            self.game.switch_turn()
        self.game.update(self.id, self.current_image)


        


