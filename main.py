from field import field
from gamelogic import GameLogic
from tictactoe import TicTacToeGUI

#Starts up the TicTacToe GUI, which is currently the only GUI screen in use.
def main():
    maingui = TicTacToeGUI()
    maingui.root.mainloop()

if __name__ == '__main__':
    main()