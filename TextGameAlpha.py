import time
#class locationState(Object):
bedroom = None
livingRoom = None
kitchen = None
balcony = None
dead = None
playerOne = None

"""class locationState:
    gameActors = {}
    def placeGameEntity(self, gameEntity):
        self.gameActors[gameEntity.name] = gameEntity
"""

class livingRoomState:#(locationState): 
    def __init__(self):
        self.balconyDoorOpen = False
        self.gameActors = {}

    def execute(self, input):
        if(input == 'close door'):
            if (not self.balconyDoorOpen):
                print("The balcony door's already closed.")
            else:
                self.balconyDoorOpen=False
                print("You slide the balcony door closed.")
            return livingRoom
        elif(input == 'open door'):
            if (self.balconyDoorOpen):
                print("The balcony door's already open.")
            else:
                self.balconyDoorOpen=True
                print("You slide the balcony door open.")
            return livingRoom
        elif(input == 'go bedroom'):
            return bedroom
        elif(input == 'go living-room'):
            print("You're already in the living room, amigo.")
            return livingRoom
        elif(input == 'go kitchen'):
            return kitchen
        elif(input == 'go balcony'):
            if self.balconyDoorOpen:
                return balcony
            else:
                print("The balcony door's closed. You should open it. Or you can continue trying to phase through solid matter.")
                return livingRoom
        elif(input == "look room"):
            print("You're in the living room. There's a couch, a TV, and a welded shut front door that grab your attention.")
            print("There's a doorway to the bedroom, a doorway to the kitchen area, and the door to the balcony which is " + ("open" if self.balconyDoorOpen else "closed") + ".")
            return livingRoom
        else:
            print("Yeah, I've got no idea what you're saying, man.")
            return livingRoom

    def enter(self):
        print("You're in the living room.")
	#self.gameActors['player'] = playerOne
    #def exit(self):
    #    del self.gameActors['player']
"""
class doorBool:
    Open = None
    def __init__(self, booleanOpen):
        Open = booleanOpen """

class balconyState:
    def execute(self, input):
        if(input == 'go living-room'):
            return livingRoom
        elif(input == 'go balcony'):
            print("You're already on the balcony.")
            return balcony
        elif(input == 'look room'):
            print("You're pretty high up so it's a long way down... don't make any silly moves, man.")
            return balcony
        elif(input == 'jump up'):
            print("Hey! Careful about jumping here! It's a long way down...")
            return balcony
        elif(input == 'jump off'):
            print("Ok, you're falling now. This is bad...")
            for i in range(5):
                time.sleep(0.75)
                print("")
                print('Falling.' + i*'.')
            playerOne.setHealth(0)
            print("Now you've landed. Hoo boy. ...wow, you left quite the mess.")
            return dead
        else:
            print("You can't get there from here.")
            return balcony

    def enter(self):
	    print("You're on the balcony now. It's a nice day out... IN HELL! MWAHAHAHA-- Not really, it's just really hot out. :3")

class bedroomState:
    def execute(self, input):
        if(input == 'go living-room'):
            return livingRoom
        elif(input == 'go bedroom'):
            print("You're already in the bedroom.")
            return bedroom
        elif(input == "look room"):
            print("The walls are bare except for an exploded view diagram of a furby taped to the wall by the bed. That furby diagram's giving me the creeps. Nightmare fuel galore.")
            return bedroom
        else:
            print("You can't get there from here.")
            return bedroom

    def enter(self):
        print("You're in the bedroom now.")

class kitchenState:
    def execute(self, input):
        if(input == 'go living-room'):
            return livingRoom
        elif(input == 'go kitchen'):
            print("You're already in the bedroom.")
            return kitchen
        elif(input == "look room"):
            print("The kitchen is inexplicably spotless. No dirty dishes, weird floor/wall stains, or errant trash in sight. You do find a wormhole to some hellish alternate reality in the fridge however. That's less than cool.")
            return kitchen
        else:
            print("You can't get there from here.")
            return kitchen
    def enter(self):
        print("You're in the kitchen now.")

class deadState:
    def enter(self):
        print("You're dead now. Do you want to reset? Type 'yes' if you do, 'no' if you don't (case sensitive).")

bedroom = bedroomState()
livingRoom = None
kitchen = kitchenState()
balcony = balconyState()
#balcony.livingRoomDoorOpen = doorBool()
#livingRoom.balconyDoorOpen = balcony.livingRoomDoorOpen
dead = deadState()

class gameActor:
    health = None
    locationState = None
    def attack(self, enemyPointer):
        if (enemyPointer.locationState is self.locationState):
            enemyPointer.minusHealth(self.attackDmg)
    def minusHealth(self, value):
        self.health -= value
    def plusHealth(self, value):
        self.health += value
    def setHealth(self, value):
        self.health = value

class npc(gameActor):
    name = None
    description = None

class friendlyNpc(npc):
    responses = {}

class enemyNpc(npc):
    attackDmg = None
    def __init__(self, location):
        self.locationState = location
	#location.placeGameEntity(self)

class evilRobot(enemyNpc):
    attackDmg = 1
    name = "robot"
    def __init__(self, location):
        super(evilRobot, self).__init__(self, location)
        health = 20
    
class player(gameActor):
    #actionVerbs = {'attack'}
    Verbs = {'go', 'jump', 'open', 'close', 'look'}
    attackDmg = 10
    def __init__(self):
        self.locationState = bedroom
        self.health = 100
        self.locationState.enter()

    def execute(self, command):
        if(command[0] in self.Verbs):
            self.locationState = self.locationState.execute(" ".join(command))
            self.locationState.enter()
        else:
            print('lolwut?')

gameVerbVocab = {'exit','go','jump','attack','open','close','look'}
gameNounPrepVocab = {'game','robot','living-room','kitchen','bedroom','balcony','up','off','door', 'room'}

def getInput():
    commandInput = input(">> ").split(" ")
    if((len(commandInput)==2) and (commandInput[0] in gameVerbVocab) and (commandInput[1] in gameNounPrepVocab)):
        if(" ".join(commandInput) == 'exit game'):
            print('kthxbai!')
            exit()
        else:
            playerOne.execute(commandInput)
    else:
        print("Please limit input to verb-noun or verb-preposition pairs.")
        print("Available verbs: 'look', 'attack', 'go', 'jump'(if you're on the balcony)")
        print("Available nouns/preps: 'living-room', 'bedroom', 'balcony', 'kitchen', 'off' or 'up' (following 'jump' if you're on the balcony), 'robot'")
        print("You can also open and close the balcony door with 'open door' and 'close door'.")

while(True):
    livingRoom = livingRoomState()
    playerOne = player()
    resetInput = False
    while(resetInput != True):
        while(playerOne.health > 0):
            getInput()
        while(resetInput==False):
            print("Please type 'yes' or 'no' (case sensitive).")
            resetInput = input(">> ").split(" ")[0]
            print(resetInput)
            if(resetInput == 'yes'):
                resetInput = True
            elif(resetInput == 'no'):
                print("Ok, way to give up, man.")
                exit()
            else:
                resetInput = False
