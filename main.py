from field import field
from gamelogic import GameLogic
from tictactoe import TicTacToeGUI
from titlescreen import titlescreen
from score import score
import threading
import ctypes
#Starts up the TicTacToe GUI, which is currently the only GUI screen in use.

def main():
    
    ts = titlescreen()
    ts.root.mainloop()
    sc = score()
    t = threading.Thread(target=sc.run)
    t.daemon = True
    t.start()
  
    while True:
        maingui = TicTacToeGUI(ts.user,sc)
        maingui.root.mainloop()
        sc.refresh()
        if(maingui.play_again):
            del maingui
        else:
            maingui.root.destroy()
            quit()
            break



if __name__ == '__main__':
    main()