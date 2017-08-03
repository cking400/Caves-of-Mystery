""" This file is used to Unit Test the steps to complete the adventure. """

from adventure.io import *
from adventure.player import *
from adventure.rooms import *
from adventure.parser import *

thePlayer = Player()

tests = [
    "n",    # cave entrance
    "take leaflet", 
    "read leaflet",

    # temperary until these can go in the kitchen
    "take pot",
    "take spoon",

    "d",    # bottom of the ladder
    "e",    # bat cave room
    "l",    # cave opening
    "n",    # cave entrance
    "d",    # bottom of the ladder

    "bang pot", # bats fly off
    "hit pot", # make noise
    "e", # bat cave room
    "take terminal",
    "take cog",
    "drop terminal",
    "w",


    "s",    # Maze 1
    "e",    # bottom of the ladder
    "s",    # maze 1
    "n",    # maze 2
    "e",    # maze 1
    "s",    # maze 3
    "s",    # maze 1
    "n",    # maze 2
    "s",    # mine entrance

    "s",    # top of mine elevator
    "d",    # should fail since the elevator is broken
    "fix elevator",
    "d",    # bottom of the mine
    "take coal",
    "u",    # top of mine elevator
    "n",    # mine entrance

    # "n",    # maze 2
    # "w",    # maze 3
    # "e",    # maze 2
    # "w",    # maze 3
    # "w",    # maze 4
    # "s",    # maze 3 
    # "w",    # maze 4

    "i"
]

rooms[thePlayer.currentRoom].display(thePlayer)

for command in tests:
    outputText("> " + command + "\n")
    hasQuit = parse(command,  thePlayer)
