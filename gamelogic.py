class GameLogic:
    def __init__(self):
        self.turn = "circle"
        self.win = False
    def switch_turn(self):
        if self.turn == "circle":
            self.turn = "cross"
        else:
            self.turn = "circle"

