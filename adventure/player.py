from adventure.item import *

class Player:
    def __init__(self):
        self.currentRoom = "Cave opening"

    def inventory(self):
        haveStuff = bool(False)
        displayString = "You are carrying: \n"
        for k in list(items.keys()):
            if items[k].location == "Player":
                displayString = displayString + items[k].name +"\n"
                haveStuff = bool(True)
        if haveStuff:
            outputText(displayString)
        else:
            outputText("You don't have anything.")
        
