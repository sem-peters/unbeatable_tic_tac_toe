import random
import time
class AI:
    def __init__(self, parent, image):
        self.parent = parent
        self.image = image
        
    def make_move(self):
        time.sleep(.1) # to make it feel natural, like the computer is thinking

        fields = self.parent.fields #fields as inherited from gamelogic
        print("\n")
        print("parent.fields: ", fields)
        
        openfields = [] #fields that have the image value 'white'
        for index, val in enumerate(fields):
            if(val == 'white'):
                openfields.append(index)
                
        print("openfields[]: ", openfields)
        
        try:
            r = random.choice(openfields)
            print("Random number: ", r)
        
            if(self.image == 'cross'):
                self.parent.parent.fields[r].turn_cross()
            elif(self.image == 'circle'):
                
                self.parent.parent.fields[r].turn_circle()

            self.parent.update(openfields[openfields.index(r)], self.image)
            
            
            print("new parent.fields: ", self.parent.fields)
            print("\n")
        except IndexError:
            print("No more open fields!")
        self.parent.switch_turn()

