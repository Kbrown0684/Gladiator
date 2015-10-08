from math import floor

##Gladiator
##  Contains all information necessary for one
##  gladiator character in the game
class Gladiator:


	##Name is the gladiator's name
	##  duh
	__name =	""

	##Team is the team the gladiator can belong to
	##  Team can be any string
	__team =	""

	##Health tracks the amount of damage a Gladiator 
	##  can take before perishing.  Health cannot
	##  be more than maxHealth
	__health =	0
	__maxHealth =	0
	
	##Speed is used to determine turn order
	##Distance determines how far a gladiator
	##  can move in one turn
	__speed =	0
	__distance =	0

	##Facing keeps track of the direction a
	##  gladiator faces:  1 is North, 2 is East,
	##  3 is South, and 4 is West.  These are
	##  the only acceptable values
	__facing =	1

	##Equipment is a map with the following
	##  keys:  Weapon, Armor, Trinket*
	##  Weapon is a list with Damage, Weight, and Name
	##  Armor is a list with Health, Weight, and Name
	##  Trinket is a list with a pointer to
	##    an Object, a Quantity, a Weight, and Name
	##
	##TODO:  Update equipment system
	__equipment =	{}

	
	##Constructor
	def __init__(self):
		self.name = 	"Nobody"
		self.team =	"Neutral"

		self.health =	10
		self.maxHealth =10
		
		self.speed =	10
		self.distance = 5
		
		self.facing =	1
		
		self.equipment = {
			"Weapon":[0,0,"Nothing"],
			"Armor":[0,0,"Nothing"],
			"Trinket":[-1, 0, 0, "Nothing"]
		}

	##String conversion
	def __str__(self):
		outString = ""
		outString += "Name: "+self.name+"\n"
		outString += "  Team:   "+self.team+"\n"
		outString += "  Health: "+str(self.health)+"/"+str(self.maxHealth)+"\n"
		outString += "  Damage: "+str(self.equipment["Weapon"][0])+"\n"
		outString += "  Weight: "+str(self.getWeight())+"\n"
		outString += "  Speed:  "+str(self.speed)+"\n"
		outString += "  Distance: "+str(self.distance)
		return outString


	##getHealth
	##  returns health value
	def getHealth(self):
		return self.health
	
	##getSpeed
	##  returns speed value
	def getSpeed(self):
		return self.speed
	
	##getDistance
	##  returns distance value
	def getDistance(self):
		return self.distance

	##getFacing
	##  returns facing value
	def getFacing(self):
		return self.facing
	
	##getDamage
	##  returns weapon damage
	##
	##TODO:  update equipment system to objects
	def getDamage(self):
		return self.equipment["Weapon"][0]

	##getWeight
	##  returns the sum of weight across
	##    gladiator's equipment
	def getWeight(self):
		outVal = self.equipment["Weapon"][1]
		outVal += self.equipment["Armor"][1]
		return outVal


	##setHealth
	##  changes the value of health
	##  if newVal is greater than maxHealth
	##    sets health to maxHealth
	##  @param newVal - An int between 0 
	##    and maxHealth
	def setHealth(self, newVal):
		if newVal <= self.maxHealth:
			self.health = newVal
		else:
			self.health = self.maxHealth

	##setFacing
	##  changes the value of facing to newVal
	##  @param newVal - An int between 1 and 4
	def setFacing(self, newVal):
		if (newVal <= 4 and newVal >= 1):
			self.facing = newVal
			return True
		else:
			return False

	##updateMaxHealth
	##  refreshes maxHealth's value based
	##    on equipment.  Raises health by
	##    the difference between the new and old values
	def updateMaxHealth(self):
		oldMaxHealth = self.maxHealth
		self.maxHealth = 10+self.equipment["Armor"][0]
		self.health += (self.maxHealth-oldMaxHealth)

	##updateSpeed
	##  refreshes speed's value based on
	##    equipment weight
	def updateSpeed(self):
		self.speed = 10-self.getWeight()

	##updateDistance
	##  refreshes distance's value based to
	##    6 - (1/4 equipment weight rounded down)
	def updateDistance(self):
		newDistance = 6
		reduction = floor(self.getWeight()/4)
		self.distance = int(newDistance-reduction)  ##make sure the value isn't a float

	##refresh
	##  calls all update functions and then
	##  returns True if the gladiator's health
	##  is greater than 0 or False otherwise
	def refresh(self):
		self.updateMaxHealth()
		self.updateSpeed()
		self.updateDistance()
		if self.health < 1:
			return False
		else:
			return True


	##setWeapon
	##  Changes the values of the gladiator's weapon
	##  @param damage - An int greater than 0
	##  @param weight - An int greater than 0
	##  @param name - A string not equal to "Nothing"
	##
	##  TODO:  Replace params with alias of Weapon obj
	def setWeapon(self, damage, weight, name):
		target = self.equipment["Weapon"]
		target[0] = damage
		target[1] = weight
		target[2] = name


	##setArmor
	##  Changes the values of the gladiator's weapon
	##  @param healthBonus - An int greater than 0
	##  @param weight - An int greater than 0
	##  @param name - A string not equal to "Nothing"
	##
	##  TODO:  Replace params with alias of Armor obj
	def setArmor(self, healthBonus, weight, name):
		target = self.equipment["Armor"]
		target[0] = healthBonus
		target[1] = weight
		target[2] = name


	##takeDamage
	##  reduces gladiator's health by dmg
	##  @param dmg - an int greater than 0
	def takeDamage(self, dmg):
		self.setHealth(self.getHealth() - dmg)

	##attack
	##  calls the target's takeDamage method
	##  @param target - A gladiator object
	def attack(self, target):
		target.takeDamage(self.getDamage())
		return
