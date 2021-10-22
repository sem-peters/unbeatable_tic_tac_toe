import random
import time
class AI:
    def __init__(self, parent, image):
        self.parent = parent
        self.image = image
        self.turn_counter = 1
    def make_move(self):
        time.sleep(.2) # to make it feel natural, like the computer is thinking

        self.fields = self.parent.fields #fields as inherited from gamelogic
        #print("\n")
        #print("parent.fields: ", fields)
        
        self.openfields = [] #fields that have the image value 'white'
        self.ai_fields = [] #fields that have the same image value as the ai
        self.user_fields = [] #fields that have the same image value as the user


        self.update_fields()
        self.good_moves()
        print("Before make move: ")
        print("Open fields: ", self.openfields)
        print("User fields: ", self.user_fields)
        print("AI fields: ", self.ai_fields)
        try:
            r = random.choice(self.goodmoves) # only pick good moves! 'r' is the move that's eventually made.
            if(self.image == 'cross'):
                self.parent.parent.fields[r].turn_cross()
            elif(self.image == 'circle'):
                self.parent.parent.fields[r].turn_circle()
            self.parent.update(self.openfields[self.openfields.index(r)], self.image)
        except IndexError:
            print("No more open fields!")
        self.update_fields()
        
        self.parent.switch_turn()

    #def consider(self, openfields):
        #print(openfields)

    def update_fields(self):
        self.fields = self.parent.fields #fields as inherited from gamelogic, meaning an array of strings. Not the actual field objects!
        for index, val in enumerate(self.fields):
            if(val == 'white'):
                self.openfields.append(index)
            elif(val == self.image):
                self.ai_fields.append(index)
            else:
                self.user_fields.append(index)
        self.openfields = list(dict.fromkeys(self.openfields))
        self.user_fields = list(dict.fromkeys(self.user_fields))
        self.ai_fields = list(dict.fromkeys(self.ai_fields))
    def good_moves(self):
        # AI's turn: let's think of some good moves.
        self.goodmoves = [self.ai_almost_winning()]
        if(self.goodmoves[0] == 999):
            if(len(self.openfields) == 9): # if all fields are white, AI has first turn.
                self.goodmoves = [0,2,6,8] # if you have first turn, always start in a corner!

            else: # You don't have first turn. What turn is it?

                if(self.turn_counter == 2): # Second turn, AI's turn. User just started and has 1.
                    if(self.user_fields[0] in (0, 2, 6, 8)): # if the user has started on a corner:
                        self.goodmoves = [4] # Only good move is the center, force a tie or win.
                    else: # User has started in the center or somewhere else:
                        self.goodmoves = [0,2,6,8]

                elif(self.turn_counter == 3): # Third turn, AI's turn. AI has just started (in corner), user responded.
                    if(self.user_fields[0] == 4): # User has responded with center
                        # Let AI respond with opposite corner from what they picked:
                        if(self.ai_fields[0] == 0): self.goodmoves = [8]
                        elif(self.ai_fields[0] == 2): self.goodmoves = [6]
                        elif(self.ai_fields[0] == 6): self.goodmoves = [2]
                        else: self.goodmoves = [0]

                    else: # User has NOT responded with center:
                        # Let AI respond with an opposide SIDE from what they picked:
                        if(self.ai_fields[0] == 0): self.goodmoves = [2,6]
                        elif(self.ai_fields[0] == 2): self.goodmoves = [0,8]
                        elif(self.ai_fields[0] == 6): self.goodmoves = [0,8]
                        else: self.goodmoves = [2,6]



                else:
                    print("No good moves implemented, picking at random... ")
                    self.goodmoves = self.openfields
                print("Good moves: ", self.goodmoves)
    
    
    def ai_almost_winning(self):
        x = 999
        #horizontal ltr
        if all(item in self.ai_fields for item in (0,1)) and not self.user_fields.__contains__(2): x = 2
        elif all(item in self.ai_fields for item in (3,4)) and not self.user_fields.__contains__(5): x = 5
        elif all(item in self.ai_fields for item in (6,7)) and not self.user_fields.__contains__(8): x = 8
        #horizontal rtl
        elif all(item in self.ai_fields for item in (2,1)) and not self.user_fields.__contains__(0): x = 0
        elif all(item in self.ai_fields for item in (5,4)) and not self.user_fields.__contains__(3): x = 3
        elif all(item in self.ai_fields for item in (8,7)) and not self.user_fields.__contains__(6): x = 6
        #horitzontal outside_to_middle
        elif all(item in self.ai_fields for item in (0,2)) and not self.user_fields.__contains__(1): x = 1
        elif all(item in self.ai_fields for item in (3,5)) and not self.user_fields.__contains__(4): x = 4
        elif all(item in self.ai_fields for item in (6,8)) and not self.user_fields.__contains__(7): x = 7
        #vertical ttb
        elif all(item in self.ai_fields for item in (0,3)) and not self.user_fields.__contains__(6): x = 6
        elif all(item in self.ai_fields for item in (1,4)) and not self.user_fields.__contains__(7): x = 7
        elif all(item in self.ai_fields for item in (2,5)) and not self.user_fields.__contains__(8): x = 8
        #vertical btt
        elif all(item in self.ai_fields for item in (6,3)) and not self.user_fields.__contains__(0): x = 0
        elif all(item in self.ai_fields for item in (7,4)) and not self.user_fields.__contains__(1): x = 1
        elif all(item in self.ai_fields for item in (8,5)) and not self.user_fields.__contains__(2): x = 2
        #vertical outside_to_middle
        elif all(item in self.ai_fields for item in (0,6)) and not self.user_fields.__contains__(3): x = 3
        elif all(item in self.ai_fields for item in (1,7)) and not self.user_fields.__contains__(4): x = 4
        elif all(item in self.ai_fields for item in (2,8)) and not self.user_fields.__contains__(5): x = 5
        #diagonal ltr
        elif all(item in self.ai_fields for item in (0,4)) and not self.user_fields.__contains__(8): x = 8
        elif all(item in self.ai_fields for item in (1,4)) and not self.user_fields.__contains__(2): x = 2
        #diagonal rtl
        elif all(item in self.ai_fields for item in (2,4)) and not self.user_fields.__contains__(6): x = 6
        elif all(item in self.ai_fields for item in (8,4)) and not self.user_fields.__contains__(0): x = 0
        #diagonal outside_to_middle
        elif all(item in self.ai_fields for item in (0,8)) and not self.user_fields.__contains__(4): x = 4
        elif all(item in self.ai_fields for item in (2,6)) and not self.user_fields.__contains__(4): x = 4
        else:
            x = 999
        print(x)
        return x
    def user_almost_winning(self):
        return False