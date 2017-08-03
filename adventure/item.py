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
    if thePlayer.currentRoom == "Damp cellar" and noun == "candy":
        items['rats'].description = "Group of sleeping rats"
        items['candy'].location = 'eaten'
        outputText("The rats eat the candy and fall asleep.")
    return bool(True)

def insert(thePlayer,  noun):
    if noun == "coin" and thePlayer.currentRoom == "Cafeteria" and items['coin'].location == "Player" and items['candy'].location == "In machine":
        items['coin'].location = "In machine"
        items['candy'].location = "Cafeteria"
        outputText("The machine takes the coin and despenses a candy.")
    elif items['candy'].locaiton != "In machine":
        outputText("There is no more candy in the vending machine.")
    else:
        outputText("You can't do that.")

def bang(thePlayer,  noun):
    if thePlayer.currentRoom == "Bottom of the ladder" and noun == "pot":
        if items["bats"].location == "Bat cave room":
            items["bats"].location = "left cave"
            outputText("Banging the pot makes a deafening noise and something flies past.")
        else:
            outputText("Banging the pot makes a lot of noise.")
    else:
        outputText("I don't understand.")

def open(thePlayer,  noun):
    if thePlayer.currentRoom == "East end of corridor" and (noun == "desk" or noun == "drawer"):
        if items["manual"].location == "In desk":
            items["manual"].location = "East end of corridor"
            outputText("The desk drawer opens and you find a maunal.")
        else:
            outputText("The desk drawer opens but nothing is in it.")
    else:
        outputText("I don't understand.")

def read(thePlayer,  noun):
    if noun == "leaflet":
        if items["leaflet"].location == "Player":
            outputText("'Strike it rich with a dimond', the rest is illegible.")
        else:
            outputText("You don't have it.")
    else:
        outputText("You can't read that.")

def kick(thePlayer,  noun):
    if noun in ["computer",  "mainframe"] and thePlayer.currentRoom == "Computer room":
        items["computer"].kick(thePlayer,  noun)
    else:
        outputText("What did that ever do to you?")

def type(thePlayer,  noun):
    if thePlayer.currentRoom == "Computer room":
        items["computer"].type(thePlayer,  noun)
    else:
       outputText("You can't type on that.")
        
def fix(thePlayer,  noun):
    if thePlayer.currentRoom == "Mine elevator" and noun == "elevator" and items["cog"].location == "Player":
         items["cog"].location = "elevator"
         outputText("You fix the elevator with the cog.")
    else:
        outputText("You can't fix that.")
           
# This is the class for the mainframe computer in the adventure.
class Computer(Item):

    def __init__(self,  name,  description,  location,  details="There is nothing special about it.",  canTake="y"):
       super().__init__(name,  description,  location,  details,  canTake)
       self.condition = "off"
       self.login = "no"
       self.copied = "no"
       
    # This method handles all the kick commands for the computer.
    def kick(self, thePlayer,  noun):
        
        # If the computer is off and the user kicks it it will start.
        if self.condition == "off":
            self.condition = "on"
            outputText("The mainframe struggles but it finally powers up.")
            outputText("A message appears on the screen, 'ENTER LOGIN NAME'")
        
        # if the computer is already running let the user know if they kick it a second time.
        elif self.condition == "on":
            outputText("What did this computer do to you?")
            
    # This method handles all the typing commands to the mainframe comouter.
    def type(self, thePlayer,  noun):
        
        # Login to the mainframe. The computer must be running first however.
        if noun == "road" and self.login == "no" and self.condition =="on":
            self.login = "yes"
            outputText("The computer respondes, 'Welcome you have logged in successfully.'")
        
        # Type dir to display the instructions.
        elif noun == "dir" and self.login == "yes" and self.condition =="on":
            outputText("The computer responds, 'type COPY to load adventure then type ADVEN to start it.'")
        
        # Copy the adventure game from the tape to the computer mainframe.
        elif noun == "copy" and self.login == "yes" and self.condition == "on" and items["tape"].location == "Tape mount":
            self.copied = "yes"
            outputText("The tape spins and the computer displays, 'ADVEN loaded successfully.'")
        
        # Handle the tape is not mounted.
        elif noun == "copy" and self.login == "yes" and self.condition == "on" and items["tape"].location != "Tape mount":
            outputText("The computer displays, 'Error: no tape to copy'")
        
        # Win the game
        elif noun == "adven" and self.login == "yes" and self.condition == "on" and self.copied == "yes":
            outputText("The computer starts the adventure game. You have successfully completed this adventure game! Congratulations!!!")
        
        # if the computer is not on.
        elif self.condition != "on":
            outputText("The mainframe computer is not powered on.")
        
        # if the user is not logged into the computer. 
        elif self.login != "no":
            outputText("You are not logged on.")
        
        # if the user is already login and tries to again. 
        elif noun == "road" and self.login == "yes":
            outputText("You are already logged in.")

items['leaflet'] = Item("leaflet",  "An old leaflet",  "Cave entrance",  canTake="y")
items['bats'] = Item("bats",  "A horde of bats",  "Bat cave room",  canTake="n")

items['spoon'] = Item("spoon",  "A large mettle spoon",  "Cave entrance") # needs to be in kitchen
items['pot'] = Item("pot",  "An old mettle pot",  "Cave entrance") # needs to be in stove

items['terminal'] = Item("terminal",  "An old broken computer terminal",  "Bat cave room",  details="It looks beyond repair.")
items['cog'] = Item("cog",  "An old rusty cog",  "Under terminal")

items['coal'] = Item("coal",  "A chunck of coal",  "Bottom of the mine elevator")


items['machine'] = Item("machine",  "A vending machine with candy",  "Cafeteria",  details="The label on the machine says to insert a coin.",  canTake="n")
items['clock'] = Item("clock",  "The tower's clock works",  "Inside clock tower",  details="There is a large handle for winding the clock.",  canTake="n")
items['desk'] = Item("desk",  "An old desk",  "East end of corridor",  details="The desk has a drawer.",  canTake="n")
items['manual'] = Item("manual",  "A computer manual",  "In desk",  details="Something is written there.")
items['computer'] = Computer("computer",  "An old mainframe computer",  "Computer room",  canTake="n")
items['mount'] = Item("mount",  "An old mainframe computer tape mount",  "Computer room",  canTake="n")
