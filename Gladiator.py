


class Gladiator:

	##double underscore, "__", is used to
	##  declare private variables and methods

	##Health tracks the amount of damage a Gladiator 
	##  can take before perishing.  Health cannot
	##  be more than maxhealth
	__health =	0
	__maxhealth =	0
	
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
	__equipment =	{}

	

	def __init__(self):
		self.health =	10
		self.maxHealth =10
		
		self.speed =	10
		self.distance = 5
		
		self.facing =	1
		
		self.equipment = {
			"Weapon":(0,0,"Nothing"),
			"Armor":(0,0,"Nothing"),
			"Trinket":(-1, 0, 0, "Nothing")
		}

	def getHealth(self):
		return self.health

	def getSpeed(self):
		return self.speed
	
	def getDistance(self):
		return self.distance

	def getFacing(self):
		return self.facing

	def getDamage(self):
		return self.equipment["Weapon"][0]
