from adventure.rooms import *
from adventure.item import *

def parse(command,  thePlayer):
    command = command.lower().strip()
    sentence = command.split(' ')
    sentenceLen = len(sentence)
    if sentenceLen > 2:
        print("I don't understand.\n")
    verb = sentence[0]
    if sentenceLen == 2:
        noun = sentence[1]
    else:
        noun = ""
    if verb == "quit" and noun == "":
        return bool(True)
    elif verb in ['n', 's', 'e', 'w', 'u', 'd']:
        rooms[thePlayer.currentRoom].go(thePlayer,  command)
    elif verb == "take" and noun != "":
            Item.take(thePlayer,  noun)
    elif verb == "drop" and noun != "":
        if noun == 'all':
            Item.dropAll(thePlayer)
        else:
            Item.drop(thePlayer,  noun) 
    elif verb in ['i', 'inventory'] and noun == "":
        thePlayer.inventory()
    elif verb in ['l', 'look'] and noun == "":
         rooms[thePlayer.currentRoom].display(thePlayer)  
    elif verb == "examine" and noun != "":
        Item.examine(thePlayer,  noun)
    elif verb == "insert" and noun != "":
        insert(thePlayer,  noun)
    elif verb == "bang" and noun != "":
        bang(thePlayer,  noun)
    elif verb == "hit" and noun != "":
        bang(thePlayer,  noun)
    elif verb == "open" and noun != "":
        open(thePlayer,  noun)    
    elif verb == "read" and noun != "":
        read(thePlayer,  noun)
    elif verb == "kick" and noun != "":
        kick(thePlayer,  noun)
    elif verb == "put" and noun != "":
        put(thePlayer,  noun)
    elif verb == "fix" and noun != "":
        fix(thePlayer,  noun)
    elif verb == "eat" and noun != "":
        pass
    elif verb == "start" and noun != "":
        pass
    else:
        print("I don't understand.\n")

