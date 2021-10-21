from tkinter import *
class titlescreen:
    def __init__(self):
        self.root = Tk()
        self.root.title("TicTacToe by Sem")
        self.root.resizable(False, False) # Frame is made specifically for certain height and width, not responsive.
        
        self.user = ''
        self.ai = ''
        self.welcome_label = Label(self.root, text="Welcome to TicTacToe!")
        self.cross_circle_label = Label(self.root, text="Do you want to be cross or circle?")
        self.second_label = Label(self.root, text="You begin, but beginning turns alternate.")
        
        self.cross_button = Button(self.root, text="Cross", padx=10, pady=5, command=lambda: self.click('cross'))
        self.circle_button = Button(self.root, text="Circle", padx=10, pady=5, command=lambda: self.click('circle'))

        self.welcome_label.grid(column=1, row=0, columnspan=3, padx=10, pady=5)
        self.cross_circle_label.grid(column=1,row=1,columnspan=3, padx=10)
        self.second_label.grid(column=1, row=2, columnspan=3)
        
        self.cross_button.grid(column=1, row=4, padx=5, pady=10)
        self.circle_button.grid(column=3, row=4, padx=5, pady=10)
        
        #whitespace:
        self.whitespace1 = Label(self.root, text="", width=5).grid(column=1, row=3, columnspan=3)
        self.whitespace2 = Label(self.root, text="", width=5).grid(column=0, row=0, columnspan=1, rowspan=5)
        self.whitespace3 = Label(self.root, text="", width=5).grid(column=4, row=0, columnspan=1, rowspan=5)

    
    def click(self, btn):
        self.user = btn
        if(self.user == 'circle'):
            self.ai = 'cross'
        else:
            self.ai = 'circle'
        self.root.destroy()
        


        
    
