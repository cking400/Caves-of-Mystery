from adventure.io import outputText
from adventure.item import items

class Player:
    def __init__(self):
        self.currentRoom = "Cave opening"

    def inventory(self):
        have_stuff = False
        display_string = "You are carrying: \n"
        for k in list(items.keys()):
            if items[k].location == "Player":
                display_string = display_string + items[k].name + "\n"
                have_stuff = True
        if have_stuff:
            outputText(display_string)
        else:
            outputText("You don't have anything.")
