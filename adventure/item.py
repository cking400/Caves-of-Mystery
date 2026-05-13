from adventure.io import outputText

items = {}

class Item:
    def __init__(self, name, description, location, details="", can_take=True):
        self.name = name
        self.description = description
        self.location = location
        self.details = details
        self.can_take = can_take

    @staticmethod
    def examine(thePlayer, noun):
        if items[noun].location == thePlayer.currentRoom or items[noun].location == "Player":
            outputText(items[noun].details or "There is nothing special about it.")
        else:
            outputText("I don't see a " + noun + " here.")

    @staticmethod
    def take(thePlayer, noun):
        if takeHandler(thePlayer, noun):
            if noun not in items:
                outputText("I don't know about a " + noun + ".")
            elif not items[noun].can_take:
                outputText("You can't take a " + noun + ".")
            elif items[noun].location != thePlayer.currentRoom:
                outputText("I don't see a " + noun + " here.")
            else:
                items[noun].location = "Player"
                outputText("You took the " + items[noun].name + ".")

    @staticmethod
    def drop(thePlayer, noun):
        if dropHandler(thePlayer, noun):
            if items[noun].location == "Player":
                items[noun].location = thePlayer.currentRoom
                outputText("You dropped the " + items[noun].name + ".")

    @staticmethod
    def dropAll(thePlayer):
        for noun in list(items.keys()):
            if items[noun].location == "Player":
                Item.drop(thePlayer, noun)


def takeHandler(thePlayer, noun):
    if (noun == "terminal"
            and items['terminal'].location == "Bat cave room"
            and thePlayer.currentRoom == "Bat cave room"
            and items['cog'].location == "Under terminal"):
        outputText("You find a cog under the terminal.")
        items['cog'].location = "Bat cave room"
    return True


def dropHandler(thePlayer, noun):
    return True


def bang(thePlayer, noun):
    if noun != "pot":
        outputText("I don't understand.")
        return
    if items["pot"].location != "Player":
        outputText("You don't have a pot.")
        return
    if items["spoon"].location != "Player":
        outputText("You don't have anything to hit the pot with. Your hand just makes a dull thud.")
        return
    if thePlayer.currentRoom != "Bottom of the ladder":
        outputText("You are making a lot of noise.")
        return
    if items["bats"].location == "Bat cave room":
        items["bats"].location = "left cave"
        outputText("Banging the pot makes a deafening noise and something flies past.")
    else:
        outputText("Banging the pot makes a lot of noise.")


def open_object(thePlayer, noun):
    if thePlayer.currentRoom == "Kitchen" and noun in ("oven", "stove"):
        if items["pot"].location == "In stove":
            items["pot"].location = "Kitchen"
            outputText("The stove opens and you find a pot.")
        elif items["coal"].location == "In stove":
            items["diamond"].location = "Kitchen"
            items["coal"].location = ""
            outputText("The stove opens and the coal is now a diamond! You have won!!! Congratulations!")
        else:
            outputText("The stove opens and nothing is in it.")
    else:
        outputText("I don't understand.")


def put(thePlayer, noun):
    if noun == "coal":
        if items["coal"].location == "Player":
            outputText("(in stove)")
            outputText("(close stove door)")
            items["coal"].location = "In stove"
            outputText("The stove starts to shake and magic sparks fly and then stops.")
    else:
        outputText("I don't understand.")


def read_object(thePlayer, noun):
    if noun == "leaflet":
        if items["leaflet"].location == "Player":
            outputText("'Strike it rich with a diamond', the rest is illegible.")
        else:
            outputText("You don't have it.")
    else:
        outputText("You can't read that.")


def fix(thePlayer, noun):
    if thePlayer.currentRoom == "Mine elevator" and noun == "elevator" and items["cog"].location == "Player":
        items["cog"].location = "elevator"
        outputText("You fix the elevator with the cog.")
    else:
        outputText("You can't fix that.")
