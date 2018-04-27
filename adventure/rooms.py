from adventure.io import *
from adventure.item import *

rooms = {}

class Room:
    def __init__(self,  name,  description):
        self.name = name
        self.description = description
        self.directions = {}

    def display(self,  thePlayer):
        displayString = self.name + "\n" + self.description + "\n"
        for k in list(items.keys()):
            if items[k].location == thePlayer.currentRoom:
                displayString = displayString + items[k].description +" is here.\n"
        outputText(displayString)

    def setDirections(self,  n,  s,  e,  w,  u,  d):
        self.directions['n'] = n
        self.directions['s'] = s
        self.directions['e'] = e
        self.directions['w'] = w
        self.directions['u'] = u
        self.directions['d'] = d

    def go(self, thePlayer,  direction):
        if goHandler(thePlayer,  direction):
            if direction in self.directions:
                if self.directions[direction] == '':
                    outputText("You can't go that direction")
                else:
                    thePlayer.currentRoom = self.directions[direction]
                    rooms[thePlayer.currentRoom].display(thePlayer)
            
# for custom game logic
def goHandler(thePlayer,  direction):
    if thePlayer.currentRoom == "Bottom of the ladder" and direction == "e":
        if items["bats"].location == "Bat cave room":
            thePlayer.currentRoom = "Cave opening"
            outputText("A horde of bats carries you out of the cave.")
            return (False)
    if thePlayer.currentRoom == "Mine elevator" and direction == "d":
        if items["cog"].location != "elevator":
            outputText("The elevator seems to be broken and won't go down.")
            return (False)
    return bool(True) # built in logic can continue if turn.




    
    
