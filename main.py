from tkinter import *
from field import field
from gamelogic import GameLogic
def main():
    root = Tk()
    root.title("TicTacToe by Sem Peters")

    # Gui works as follows:
    # Field_1 - Field_9 are the fields in which X or O is placed.

    field_1 = field(root, 200, 200, 0, 0)
    field_2 = field(root, 200, 200, 1, 0)
    field_3 = field(root, 200, 200, 2, 0)
    field_4 = field(root, 200, 200, 0, 1)
    field_5 = field(root, 200, 200, 1, 1)
    field_6 = field(root, 200, 200, 2, 1)
    field_7 = field(root, 200, 200, 0, 2)
    field_8 = field(root, 200, 200, 1, 2)
    field_9 = field(root, 200, 200, 2, 2)


    fields = [field_1, field_2, field_3, field_4,
        field_5, field_6, field_7, field_8, field_9]

       
    

    root.mainloop()

if __name__ == '__main__':
    main()