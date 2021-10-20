from field import field
from gamelogic import GameLogic
from tictactoe import TicTacToeGUI
from titlescreen import titlescreen
#Starts up the TicTacToe GUI, which is currently the only GUI screen in use.
def main():
    ts = titlescreen()
    ts.root.mainloop()
    
    maingui = TicTacToeGUI(ts.user)
    maingui.root.mainloop()


if __name__ == '__main__':
    main()