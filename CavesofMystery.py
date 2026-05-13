""" Caves of Mystery - main entry point. """

from adventure.io import readCommand
from adventure.player import Player
from adventure.rooms import rooms
from adventure.parser import parse
import adventure.init  # noqa: F401 - populates rooms and items dicts


def main():
    thePlayer = Player()
    rooms[thePlayer.currentRoom].display(thePlayer)

    hasQuit = False
    while not hasQuit:
        command = readCommand("> ")
        hasQuit = parse(command, thePlayer)

    print("Good bye!")


if __name__ == "__main__":
    main()
