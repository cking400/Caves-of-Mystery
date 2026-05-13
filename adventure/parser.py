from adventure.io import outputText
from adventure.rooms import rooms
from adventure.item import Item, bang, open_object, read_object, put, fix

def parse(command, thePlayer):
    command = command.lower().strip()
    sentence = command.split(' ')
    sentence_len = len(sentence)
    verb = sentence[0]
    noun = sentence[1] if sentence_len == 2 else ""

    if sentence_len > 2:
        outputText("I don't understand.")
        return False

    if verb == "quit" and noun == "":
        return True
    elif verb in ['n', 's', 'e', 'w', 'u', 'd']:
        rooms[thePlayer.currentRoom].go(thePlayer, verb)
    elif verb == "take" and noun != "":
        Item.take(thePlayer, noun)
    elif verb == "drop" and noun != "":
        if noun == 'all':
            Item.dropAll(thePlayer)
        else:
            Item.drop(thePlayer, noun)
    elif verb in ['i', 'inventory'] and noun == "":
        thePlayer.inventory()
    elif verb in ['l', 'look'] and noun == "":
        rooms[thePlayer.currentRoom].display(thePlayer)
    elif verb == "examine" and noun != "":
        Item.examine(thePlayer, noun)
    elif verb in ("bang", "hit") and noun != "":
        bang(thePlayer, noun)
    elif verb == "open" and noun != "":
        open_object(thePlayer, noun)
    elif verb == "read" and noun != "":
        read_object(thePlayer, noun)
    elif verb == "put" and noun != "":
        put(thePlayer, noun)
    elif verb == "fix" and noun != "":
        fix(thePlayer, noun)
    else:
        outputText("I don't understand.")

    return False
