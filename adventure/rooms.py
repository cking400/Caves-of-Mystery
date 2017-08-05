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



roomData = [
    ["Cave opening",  "You are in an open field standing in front of the month of a large cave just north of you.",  
            'Cave entrance', '', '', '', '', ''], 
    ["Cave entrance",  "You are in the entrance of a large cave system. A ladder leading down a dark hole in the floor of the cave.",  
            '', 'Cave opening', '', '', '', 'Bottom of the ladder'], 
    ["Bottom of the ladder", "You are at the bottom of a ladder that goes up through a hole in the cave ceiling. There is a path through the caves to the south and east.", 
            '', 'Maze 1', 'Bat cave room', '', 'Cave entrance', ''], 
    ["Bat cave room", "This another muddy cave room in the labyrinth.", 
            '', '', '', 'Bottom of the ladder', '', ''], 
    ["Maze 1", "This is a winding passage with exists to the north, south and east.", 
            'Maze 2', 'Maze 3', 'Bottom of the ladder', '', '', ''], 
    ["Maze 2", "This is a winding passage with exists to the south, east and west.", 
            '', 'Mine entrance', 'Maze 1', 'Maze 3', '', ''], 
    ["Maze 3", "This is a winding passage with exists to the south, east and west.", 
            '', 'Maze 1', 'Maze 2', 'Maze 4', '', ''], 
    ["Maze 4", "This is a winding passage with exists to the north and south.", 
            'Kitchen', 'Maze 3', '', '', '', ''], 
    ["Mine entrance", "You are in the entrance of an old abandoned mine. There is an elevator to the south and an entrance to the caves is north.", 
            'Maze 2', 'Mine elevator', '', '', '', ''], 
    ["Mine elevator", "You are in a rickity old mine elevator. You can go down in the elevator or north to the mine entrance.", 
            'Mine entrance', '', '', '', '', 'Bottom of the mine elevator'],
    ["Bottom of the mine elevator", "You are at the bottom of the mine. There is an elevator to go up.", 
        '', '', '', '', 'Mine elevator', ''], 
    ["Kitchen", "This is a strange site to see in a cave labyrinth but you are standing in a kitchen. There is an exist to the east.", 
        '', 'Maze 4', '', '', '', ''], 
     
    ["empty", "", '', '', '', '', '', ''], 
    ["name", "description", 'n', 's', 'e', 'w', 'u', 'd']
]

for roomText in roomData:
    room = Room(roomText[0],  roomText[1])
    room.setDirections(roomText[2],  roomText[3],  roomText[4],  roomText[5],  roomText[6],  roomText[7])
    rooms[roomText[0]] = room
    
    
