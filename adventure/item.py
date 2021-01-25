from adventure.io import *

items = {}

class Item:
    def __init__(self,  name,  description,  location,  details="There is nothing special about it.",  canTake="y"):
        self.name = name
        self.description = description
        self.location = location
        self.details = details
        self.canTake = canTake
 
    @staticmethod
    def examine(thePlayer,  noun):
        if items[noun].location == thePlayer.currentRoom or items[noun].location == "Player":
            outputText(items[noun].details)
        else:
            outputText("I don't see a " + noun + " here.")
    
    @staticmethod
    def take(thePlayer,  noun):
        if takeHandler(thePlayer,  noun):
            if noun not in list(items.keys()):
                outputText("I don't know about a " + noun + ".")
            elif items[noun].canTake == 'n':
                outputText("You can't take a " + noun + ".")
            elif items[noun].location != thePlayer.currentRoom:
                outputText("I don't see a " + noun + " here.")
            else:
                items[noun].location = "Player"
                outputText("You took the " + items[noun].name + ".")    
     
    @staticmethod    
    def drop(thePlayer,  noun):
        if dropHandler(thePlayer,  noun):
            if items[noun].location == "Player":
                items[noun].location = thePlayer.currentRoom
                outputText("You dropped the " + items[noun].name + ".")       

    @staticmethod
    def dropAll(thePlayer):
        for noun in list(items.keys()):
            if items[noun].location == "Player":
                items[noun].drop(thePlayer,  noun)

def takeHandler(thePlayer,  noun):
    if noun == "terminal" and items['terminal'].location == "Bat cave room" and thePlayer.currentRoom == "Bat cave room" and items['cog'].location == "Under terminal":
        outputText("You find a cog under the terminal.")
        items['cog'].location = "Bat cave room"
    return bool(True)

def dropHandler(thePlayer,  noun):
    # Custom drop logic goes here.
    return bool(True)

def bang(thePlayer,  noun):
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
""" 
    if noun == "pot":
        if items["pot"].location == "Player":
            if items["spoon"].location == "Player":
                if thePlayer.currentRoom == "Bottom of the ladder":
                    if items["bats"].location == "Bat cave room":
                        items["bats"].location = "left cave"
                        outputText("Banging the pot makes a deafening noise and something flies past.")
                    else:
                        outputText("Banging the pot makes a lot of noise.")
                else:
                    outputText("You are making a lot of noise.")
            else:
                outputText("You don't have anything to hit the pot with. Your hand just makes a dull thud.")
        else:
            outputText("You don't have a pot.")
    else:
        outputText("I don't understand.")
         """

def open(thePlayer,  noun):
    if thePlayer.currentRoom == "Kitchen" and (noun == "oven" or noun == "stove"):
        if items["pot"].location == "In stove":
            items["pot"].location = "Kitchen"
            outputText("The stove opens and you find a pot.")
        elif items["coal"].location == "In stove":
            items["dimond"].locaton = "Kitchen"
            items["coal"].location = ""
            outputText("The stove opens and the coal is now a dimond! You have won!!! Congratulations!")
        else:
            outputText("The stove opens and nothing is in it.")
    else:
        outputText("I don't understand.") # todo: make it so anything can go into stove

def put(thePlayer, noun):
    if noun == "coal":
        if items["coal"].location == "Player":
            outputText("(in stove)")
            outputText("(close stove door)")
            items["coal"].location = "In stove"
            outputText("The stove starts to shack and magic sparks fly and then stops.")
    else:
        outputText("I don't understand.") # todo: make it so anything can go into stove

def read(thePlayer,  noun):
    if noun == "leaflet":
        if items["leaflet"].location == "Player":
            outputText("'Strike it rich with a dimond', the rest is illegible.")
        else:
            outputText("You don't have it.")
    else:
        outputText("You can't read that.")
     
def fix(thePlayer,  noun):
    if thePlayer.currentRoom == "Mine elevator" and noun == "elevator" and items["cog"].location == "Player":
         items["cog"].location = "elevator"
         outputText("You fix the elevator with the cog.")
    else:
        outputText("You can't fix that.")

# todo: this should work more like room init and should be in an init file.
items['leaflet'] = Item("leaflet",  "An old leaflet",  "Cave entrance",  canTake="y")
items['bats'] = Item("bats",  "A horde of bats",  "Bat cave room",  canTake="n")
items['spoon'] = Item("spoon",  "A large mettle spoon",  "Kitchen") 
items['pot'] = Item("pot",  "An old mettle pot",  "In stove") 
items['terminal'] = Item("terminal",  "An old broken computer terminal",  "Bat cave room",  details="It looks beyond repair.")
items['cog'] = Item("cog",  "An old rusty cog",  "Under terminal") 
items['coal'] = Item("coal",  "A chunk of coal",  "Bottom of the mine elevator")
items['dimond'] = Item("dimond",  "A large bright dimond",  "")
items['stove'] = Item("stove",  "An old stove",  "Kitchen",  details="The lable on the stove says is Fizby Magic stove.",  canTake="y")

