""" Caves of Mystery main file. """

from adventure.io import readCommand
from adventure.player import Player
from adventure.rooms import *
from adventure.parser import *
from adventure.init import *

thePlayer = Player()

""" main function handles the main loop of the game system. """
def main():

    rooms[thePlayer.currentRoom].display(thePlayer)
    
    hasQuit = bool(False)

    while not hasQuit:
        command = readCommand("> ")
        hasQuit = parse(command,  thePlayer)

    print("Good bye!!")
    
# Start main function.
if __name__ == "__main__":
    main()
