from tkinter import *
class score():
    def __init__(self):
        

        self.circle_score = 0
        self.cross_score = 0
        self.tie = 0
        self.counter = 0       

    def run(self):
        self.root = Tk()
        self.root.title("Scoreboard")
        self.root.attributes('-topmost',True)
        self.root.resizable(False, False) # Frame is made specifically for certain height and width, not responsive.
        
        label_score = Label(self.root, text="This is the current scoreboard.\n ",padx=20,pady=10)

        self.circle_wins = "Circle wins: "+str(self.circle_score)
        self.label_circle = Label(self.root, text=self.circle_wins,padx=10,pady=5)

        self.cross_wins = "Cross wins: "+str(self.cross_score)
        self.label_cross = Label(self.root, text=self.cross_wins,padx=10,pady=5)

        self.ties = "Ties: "+str(self.tie)
        self.label_ties = Label(self.root, text=self.ties,padx=10,pady=5)

        label_score.grid(column=0,row=0,columnspan=6)
        self.label_circle.grid(column=0,row=1,columnspan=2)
        self.label_ties.grid(column=2,row=1,columnspan=2)
        self.label_cross.grid(column=4,row=1,columnspan=2)

        self.root.protocol("WM_DELETE_WINDOW", func=self.stop)

        self.root.mainloop()
        
    
        



    def stop(self):
        self.root.destroy()
        quit()
    def refresh(self):
        self.circle_wins = "Circle wins: "+str(self.circle_score)
        self.label_circle = Label(self.root, text=self.circle_wins,padx=10,pady=5)

        self.cross_wins = "Cross wins: "+str(self.cross_score)
        self.label_cross = Label(self.root, text=self.cross_wins,padx=10,pady=5)

        self.ties = "Ties: "+str(self.tie)
        self.label_ties = Label(self.root, text=self.ties,padx=10,pady=5)

        self.label_circle.grid(column=0,row=1,columnspan=2)
        self.label_ties.grid(column=2,row=1,columnspan=2)
        self.label_cross.grid(column=4,row=1,columnspan=2)


        

