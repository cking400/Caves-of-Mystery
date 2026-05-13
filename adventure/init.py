""" Initialize the game world. """

from adventure.rooms import rooms, Room
from adventure.item import items, Item

roomData = [
    ["Cave opening", "You are in an open field standing in front of the mouth of a large cave just north of you.",
            'Cave entrance', '', '', '', '', ''],
    ["Cave entrance", "You are in the entrance of a large cave system. A ladder leads down a dark hole in the floor of the cave.",
            '', 'Cave opening', '', '', '', 'Bottom of the ladder'],
    ["Bottom of the ladder", "You are at the bottom of a ladder that goes up through a hole in the cave ceiling. There is a path through the caves to the south and east.",
            '', 'Maze 1', 'Bat cave room', '', 'Cave entrance', ''],
    ["Bat cave room", "This is another muddy cave room in the labyrinth.",
            '', '', '', 'Bottom of the ladder', '', ''],
    ["Maze 1", "This is a winding passage with exits to the north, south and east.",
            'Maze 2', 'Maze 3', 'Bottom of the ladder', '', '', ''],
    ["Maze 2", "This is a winding passage with exits to the south, east and west.",
            '', 'Mine entrance', 'Maze 1', 'Maze 3', '', ''],
    ["Maze 3", "This is a winding passage with exits to the south, east and west.",
            '', 'Maze 1', 'Maze 2', 'Maze 4', '', ''],
    ["Maze 4", "This is a winding passage with exits to the north and south.",
            'Kitchen', 'Maze 3', '', '', '', ''],
    ["Mine entrance", "You are in the entrance of an old abandoned mine. There is an elevator to the south and an entrance to the caves to the north.",
            'Maze 2', 'Mine elevator', '', '', '', ''],
    ["Mine elevator", "You are in a rickety old mine elevator. You can go down in the elevator or north to the mine entrance.",
            'Mine entrance', '', '', '', '', 'Bottom of the mine elevator'],
    ["Bottom of the mine elevator", "You are at the bottom of the mine. There is an elevator to go up.",
            '', '', '', '', 'Mine elevator', ''],
    ["Kitchen", "This is a strange sight to see in a cave labyrinth, but you are standing in a kitchen. There is an exit to the south.",
            '', 'Maze 4', '', '', '', ''],
]

for roomText in roomData:
    room = Room(roomText[0], roomText[1])
    room.setDirections(roomText[2], roomText[3], roomText[4], roomText[5], roomText[6], roomText[7])
    rooms[roomText[0]] = room

itemData = [
    ["leaflet",  "An old leaflet",               "Cave entrance",             "",                                          True],
    ["bats",     "A horde of bats",               "Bat cave room",             "",                                          False],
    ["spoon",    "A large metal spoon",            "Kitchen",                  "",                                          True],
    ["pot",      "An old metal pot",               "In stove",                 "",                                          True],
    ["terminal", "An old broken computer terminal","Bat cave room",             "It looks beyond repair.",                   False],
    ["cog",      "An old rusty cog",               "Under terminal",            "",                                          True],
    ["coal",     "A chunk of coal",                "Bottom of the mine elevator","",                                         True],
    ["diamond",  "A large bright diamond",         "",                          "",                                          True],
    ["stove",    "An old stove",                   "Kitchen",                   "The label on the stove reads: Fizby Magic Stove.", False],
]

for itemText in itemData:
    item = Item(itemText[0], itemText[1], itemText[2], itemText[3], itemText[4])
    items[itemText[0]] = item
