from package.field import field
from package.gamelogic import GameLogic
from package.tictactoe import TicTacToeGUI
from package.titlescreen import titlescreen
from package.score import score
import threading
import time
errormessage = "Ungraceful exit..."
def main():
    try:
        ts = titlescreen()
        ts.root.mainloop()

        # Scoreboard instance is a thread, becaues this allows two GUI windows to be open at once.
        # It's a daemon, because I want it to die when the main TicTacToe GUI is closed, so the
        # user doesn't have to close two windows.
        sc = score(ts.user,ts.ai)
        scoreboard = threading.Thread(target=sc.run)
        scoreboard.daemon = True
        scoreboard.start()
        maingui = TicTacToeGUI(ts.user, ts.ai, sc)

        # This thread keeps track whether the scoreboard thread is alive. If it's closed, the entire program should shut down.
        alive_checker_1 = threading.Thread(target=lambda: alive(scoreboard, maingui))
        alive_checker_1.daemon = True
        alive_checker_1.start()


        while True:
            maingui.run()
            sc.refresh()
            if(maingui.play_again):
                maingui.__init__(ts.user, ts.ai, sc)
            else:
                quit()
                break
    except ValueError:
        print(errormessage)
    except NameError:
        print(errormessage)
    except RuntimeError:
        print(errormessage)

def alive(thread, gui):
    while True:
        if(not thread.is_alive()):
            gui.root.destroy()
            quit()
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
