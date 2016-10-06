"""This is a work in progress. The game currently doesn't run."""

frontDoorOpen = False
balconyDoorOpen = False

class item(Object):
    name = None
    description = None

class consumable(item):
    

class roomState(Object):
"""There are 4 room states: kitchen, bedroom, living room, balcony"""

class livingRoomState(roomState):
"""Every room is connected to the living room. None of the other rooms are directly connected to each other."""
    def enter(self):
	balconyDoorState = 'open' if balconyDoorOpen else 'closed'
	frontDoorState = 'open' if frontDoorOpen else 'closed'
        print("You're in the living room. There's a couch and a TV. The kitchen area is behind you. The bedroom door is lone gone and it's doorway is clear.")
	print("The door to the balcony is" + balconyDoorState "The door to the apartment is" + frontDoorState +".")

    def exit(self):
        print("")
    
class inventoryItem(Object):
    itemReference = None
    itemCopyCount = None
    def __init__(self):
        self.itemCopyCount = 0

class inventory(Object):
    items = None # items contains a dictionary with string keys and dictionary values
    maxNumItems = None
    numItemsHeld = None
    def __init__():
        self.items = {}

class playerInventory(inventory):
    
    def __init__(self):
	super(playerInventory, self).__init__(self)
        self.maxNumItems = 8
	self.numItemsHeld = 0

    def insert(self, itemToInsert):
        if(len(numItemsHeld < maxNumItems))
	    if(itemToInsert.name not in items):
                items[itemToInsert.name] = inventoryItem()
		items[itemToInset.name].itemReference = itemToInsert
	    items[itemToInsert.name].itemCopyCount += 1
	    numItemsHeld += 1
        else:
    	    print("Inventory's full, sorry.")

    def remove(self, nameOfItemToDelete):
	if(nameOfItemToDelete in items):
	    if(items[nameOfItemToDelete].itemCopyCount < 2):
	        del items[nameOfItemToDelete]
	    else:
                items[nameOfItemToDelete].itemCopyCount -=1
            numItemsHeld -= 1
	else:
	    print("Yeah, you don't have one of those in your inventory.")

    def getItemFromInv(self, nameOfItem):
        return items[nameOfItem].itemReference

    def checkInventory(self):
	print("This is what you have on you:")
        for item in self.items:
	    print("Number of" + item + " : " + item.itemCopyCount)

class gameActor(Object):
    health = None
    #methods: move,minusHealth,plusHealth

class npc(gameActor):
    alignment = None #alignment = False -> enemy, True -> friend, None -> neutral
    attackDmg = None

class evilRobot(npc):
    alignment = False
    attackDmg = 1
    def __init__(self):
        self.health = 10
    def minusHealth(self, healthUnits):
        self.health -= healthUnits
    def plusHealth(self, healthUnits):
        self.health += healthUnits
    def attack(self, gameActorToAttack):
        gameActorToAttack.minusHealth(self.attackDmg)

class player(gameActor):
    equippedItemName = None
    playerHealth = None
    inventory = None
    locationState = None
    def __init__(self):
        self.playerHealth = 100
	self.inventory = playerInventory()
	self.locationState = bedroomState()

actionVocab = {

#parse returns a parse tree which the execute function can use
def parse(inputString):
    if

def getInput():
    lineRead = input('>>').split(" ")
    parsedActions = parse(lineRead)
    execute(parsedActions)

if __name__ == '__main__':
    playerOne = player()
    while(True):
        getInput()
