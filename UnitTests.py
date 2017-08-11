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

    "d",    # bottom of the ladder
    "e",    # bat cave room
    "l",    # cave opening
    "n",    # cave entrance
    "d",    # bottom of the ladder

    # to the kitchen
    "s",    # Maze 1
    "n",    # maze 2
    "w",    # maze 3
    "w",    # maze 4

    "n",    # kitchen
    "open stove",
    "take pot",
    "take spoon",

    # to the bat cave then the mine
    "s",    # maze 4
    "s",    # maze 3
    "s",    # maze 1
    "e",    # bottom of the ladder

    "bang pot", # bats fly off
    "hit pot", # make noise
    "e", # bat cave room
    "take terminal",
    "take cog",
    "drop terminal",
    "w",     # bottom of the ladder

    # to the mine
    "s",    # maze 1
    "n",    # maze 2
    "s",    # mine entrance

    # get the coal
    "s",    # top of mine elevator
    "d",    # should fail since the elevator is broken
    "fix elevator",
    "d",    # bottom of the mine
    "take coal",
    "u",    # top of mine elevator
    "n",    # mine entrance

    # to the kitchen
    "n",    # maze 2
    "w",    # maze 3
    "w",    # maze 4
    "n",    # kitchen

    # make dimond from coal
    "put coal",
    "open stove",

    "i"
]

rooms[thePlayer.currentRoom].display(thePlayer)

for command in tests:
    outputText("> " + command + "\n")
    hasQuit = parse(command,  thePlayer)
