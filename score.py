from tkinter import *
class score():
    def __init__(self, user, ai):
        
        self.user = user
        
        self.ai = ai
        self.ai_score = 0
        self.user_score = 0
        self.tie = 0
        self.counter = 0
        print("in __init__():")
        print("User score: ", self.user_score)
        print("AI scoreL ", self.ai_score)
        if(self.user == ''):
            quit()   

    def run(self):
        print("in score.run()")
        print("User score: ", self.user_score)
        print("AI score ", self.ai_score)
        self.root = Tk()
        self.root.title("Scoreboard")
        self.root.attributes('-topmost',True)
        self.root.resizable(False, False) # Frame is made specifically for certain height and width, not responsive.
        
        label_score = Label(self.root, text="This is the current scoreboard.\n ",padx=20,pady=10)

        self.ai_wins = "AI wins: "+str(self.ai_score)
        self.user_wins = "Your wins: "+str(self.user_score)
        self.ties = "Ties: "+str(self.tie)
        self.label_user = Label(self.root, text=self.user_wins,padx=10,pady=5)
        self.label_ai = Label(self.root, text=self.ai_wins,padx=10,pady=5)
        self.label_ties = Label(self.root, text=self.ties,padx=10,pady=5)

        label_score.grid(column=0,row=0,columnspan=6)
        self.label_user.grid(column=0,row=1,columnspan=2)
        self.label_ties.grid(column=2,row=1,columnspan=2)
        self.label_ai.grid(column=4,row=1,columnspan=2)

        self.root.protocol("WM_DELETE_WINDOW", func=self.stop)
        print(self.user_score)
        self.root.mainloop()
        
    
        



    def stop(self):
        self.root.destroy()
        quit()
    def refresh(self):
        print("in refresh()")
        print("User score: ", self.user_score)
        print("AI scoreL ", self.ai_score)
        self.ai_wins = "AI wins: "+str(self.ai_score)
        self.user_wins = "Your wins: "+str(self.user_score)
        self.ties = "Ties: "+str(self.tie)
        self.label_user = Label(self.root, text=self.user_wins,padx=10,pady=5)
        self.label_ai = Label(self.root, text=self.ai_wins,padx=10,pady=5)
        self.label_ties = Label(self.root, text=self.ties,padx=10,pady=5)

        self.label_user.grid(column=0,row=1,columnspan=2)
        self.label_ties.grid(column=2,row=1,columnspan=2)
        self.label_ai.grid(column=4,row=1,columnspan=2)


        

