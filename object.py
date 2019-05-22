#! /usr/bin/python
# 面向对象  OOP
# This part takes Warcraft as example.

# Unit, base class of all
class ArmorType:
    Unarmored  = 0
    Light = 1
    Medium = 2
    Heavy = 3
    Hero = 4
    Fortified = 10

class AttackType:
    Normal = 0
    Piercing = 1
    Siege = 2
    Chaos = 3
    MagicDamage = 4
    Hero = 5

class Race:
    Null = 0
    Neutral = 1
    Human = 2
    Orc = 3
    NightElf = 4
    Undead = 5

class Unit:
    __healthPoints = 0
    __armor = 0
    __armorType = ArmorType.Unarmored
    __attack = 0
    __attackType = AttackType.Normal

    __race = Race.Null
    __alive = False

    armor = property()
    armorType = property()
    attack = property()
    attackType = property()
    race = property()

    def __init__(self, hp, am, amType, atck, atckType, r = Race.Null):
        self.__healthPoints = hp
        self.__armor = am
        self.__armorType = amType
        self.__attack = atck
        self.__attackType = atckType
        self.__race = r
        #print "An unit inited."

    # move to coordinate x, y
    def move(self, x, y):
        print "An unit move to %d, %d" % (x, y)

    def doAttack(self, unitx):
        if (isinstance(unitx, Unit)) :
            harm = self.__attack - unitx.armor / 100
            if (harm > 0) :
                hp0 = unitx.getHP() - harm
                unitx.setHP(hp0)
                print "Cause harm %d, and the left HP is %d" % (harm, unitx.getHP())
            if (unitx.getHP() <= 0) :
                unitx.setDead()
                

    def build(hp, am, amType, atck, atckType, r = Race.Null):
        self.__alive = True
        print "An unit has been constructed."
        return self.__init__(self, hp, am, amType, atck, atckType, r)

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, a):
        self.__armor = a

    @armorType.getter
    def armorType(self):
        return self.__armorType
    
    @armorType.setter
    def armorType(self, a):
        self.__armorType = a
        
    @attack.getter
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self, a):
        self.__attack = a

    @attackType.getter
    def attackType(self):
        return self.__attackType
    
    @attackType.setter
    def attackType(self, a):
        self.__attackType = a
        
    @race.getter
    def race(self):
        return self.__race
    
    @race.setter
    def race(self, a):
        self.__race = a

    
    def isAlive(self):
        return self.__alive
    
    def getHP(self):
        return self.__healthPoints
    
    def setHP(self, points):
        self.__healthPoints = points
    
    def setDead(self):
        self.__alive = False
        print "unit died..."
    
    def setAlive(self):
        self.__alive = True
        print "unit alive..."

class Building(Unit):
    def __init__(self, hp, am, amType, r):
        Unit.__init__(self, hp, am, amType, 0, 0, r)
        print "A buidling inited, without attack ability."

    def move(self, x, y):
        print "A building cannot move."

    def doAttack(self, unitx):
        print "A building cannot attack."

    def build(self, hp, am, amType, r):
        print "A building has been constructed."
        return self.__init__(self, hp, am, amType, r)

class AliveUnit(Unit):
    def __init__(self, hp, am, amType, atck, atckType, r):
        Unit.__init__(self, hp, am, amType, atck, atckType, r)
        print "An alive unit inited."

    def build(self, hp, am, amType, atck, atckType, r):
        print "An alive unit has been constructed."
        return self.__init__(self, hp, am, amType, atck, atckType, r)

class Hero(AliveUnit):
    __name = "Dark Ranger"
    __manaPoints = 0
    __skill__ = []

    def __init__(self, hp, am, amType, atck, atckType, r, name, mp):
        AliveUnit.__init__(self, hp, am, amType, atck, atckType, r)
        self.__name = name
        self.__manaPoints = mp
        print "%s is inited." % self.__name

    def reborn(self, hp, mp):
        if (self.isAlive() == True):
            return
        self.build( 
            hp, 
            self.armor, 
            self.armorType, 
            self.attack, 
            self.attackType, 
            self.race, 
            self.__name, 
            mp)
        print "The hero will revenge!"

    def build(self, hp, am, amType, atck, atckType, r, name, mp):
        print "The hero %s has born." % self.__name
        return self.__init__(hp, am, amType, atck, atckType, r, name, mp)

# [sample] Run testcase
print "constructing....................."
barrack = Building(600.0, 200.0, ArmorType.Fortified, Race.Human)
barrack.move(125.0, 305.4)

footman = AliveUnit(200.0, 88.0, ArmorType.Light, 25.0, AttackType.Normal, Race.Human)
footman.move(125.0, 305.4)

prophet = Hero(260.0, 28.0, ArmorType.Hero, 21.0, AttackType.Hero, Race.Orc, "Thrall the Warchief", 200)
print prophet.getHP()

print "attacking ....................."
prophet.move(130.0, 325.4)
prophet.doAttack(barrack)

# let the footman kill the hero. I feel so sorry...
while(prophet.getHP() >= 0) :
    footman.doAttack(prophet)

print "The hero is killed."
print "attacking ....................."
# reborn will half mana
prophet.reborn(260.0, 100.0)

# let's revenge !!!
while(footman.getHP() >= 0):
    prophet.doAttack(footman)


