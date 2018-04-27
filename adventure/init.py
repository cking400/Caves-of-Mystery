""" Initalize the game """

from adventure.rooms import *

# Room data
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

# Add the room data into the Room objects.
for roomText in roomData:
    room = Room(roomText[0],  roomText[1])
    room.setDirections(roomText[2],  roomText[3],  roomText[4],  roomText[5],  roomText[6],  roomText[7])
    rooms[roomText[0]] = room

itemData = [
    ["leaflet",  "An old leaflet",  "Cave entrance",  "", "y"],
    ["bats",  "A horde of bats",  "Bat cave room",  "", "n"],
    ["spoon",  "A large mettle spoon",  "Kitchen", "", "y"],
    ["pot",  "An old mettle pot",  "In stove", "", "y"],
    ["terminal",  "An old broken computer terminal",  "Bat cave room",  "It looks beyond repair.", "y"],
    ["cog",  "An old rusty cog",  "Under terminal", "", "y"],
    ["coal",  "A chunk of coal",  "Bottom of the mine elevator", "", "y"],
    ["dimond",  "A large bright dimond",  "", "", "y"],
    ["stove",  "An old stove",  "Kitchen",  "The lable on the stove says is Fizby Magic stove.",  "y"]
]

for itemText in itemData:
    item = Item(itemText[0], itemText[1], itemText[2], itemText[3], itemText[4])
    items[itemText[0]] = item

    