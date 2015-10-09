from Gladiator import Gladiator
from math import floor
from copy import deepcopy

##Arena
##  The Arena class handles all movement and
##  positioning within the gamespace as
##  well as tracking boundaries and objects
##  in the environment
class Arena:

	##boundaries
	##  a 2d array of bools where True
	##  represents a wall and False
	##  is empty space
	__boundaries = []

	##environment
	##  a 2d array of objects where any
	##  objects have a .interact() method
	##  and any space without an object is
	##  equal to False
	__environment= []

	##gladiators
	##  An array of lists where the first
	##  index is a Gladiator object and
	##  the second and third index is a
	##  row and a col variable respectivelt
	__gladiators = []


	##Constructor
	##  initializes the Arena class
	##
	##  @param dimensions - A tuple with a
	##    row and a col variable in positions
	##    0 and 1 respectively
	##
	##  @param GladiatorTeamA/B - a list of
	##    Gladiator objects all with the same
	##    team as returned by getTeam
	def __init__(self, dimensions, GladiatorTeamA, GladiatorTeamB):
		self.boundaries = []
		self.environment= []
		self.gladiators = []

		for row in range(dimensions[0]):
			self.boundaries.append([])
			self.environment.append([])
			for col in range(dimensions[1]):
				self.boundaries[row].append(False)
				self.environment[row].append(False)

		for gladiator in GladiatorTeamA:
			self.gladiators.append([gladiator, -1, -1])

		for gladiator in GladiatorTeamB:
			self.gladiators.append([gladiator, -1, -1])

		print(self.gladiators)
		self.gladiators = self.getOrder()

	##isCollision
	##  Returns a bool indicating the
	##  presence of a boundary at position
	##
	##@param position - A tuple with row
	##  and col as values in the first
	##  and second index respectively
	def isCollision(self, position):
		row = position[0]
		col = position[1]
		return self.boundaries[row][col]

	##sortTeams
	##  Sorts all Gladiators in the gladiators
	##  array by speed recursively
	def sortTeams(self, arrayList):
		returnList = []
		if len(arrayList) == 2:
			speedOne = arrayList[0][0].getSpeed()
			speedTwo = arrayList[1][0].getSpeed()
			if speedOne >= speedTwo:
				returnList.append(arrayList[0])
				returnList.append(arrayList[1])
				return returnList
			else:
				returnList.append(arrayList[1])
				returnList.append(arrayList[0])
				return returnList
		
		if len(arrayList) < 3:
			return arrayList
		else:
			splitPoint = int(floor(len(arrayList)/2))
			TeamA =	self.sortTeams(arrayList[:splitPoint])
			TeamB = self.sortTeams(arrayList[splitPoint:])

			while (len(TeamA) > 0 and len(TeamB) > 0):
				speedA = TeamA[0][0].getSpeed()
				speedB = TeamB[0][0].getSpeed()
				if speedA >= speedB:
					returnList.append(TeamA.pop(0))
				if speedB >= speedA:
					returnList.append(TeamB.pop(0))

			return returnList

	##getOrder
	##  returns the Gladiators in order
	##  of their return by sortTeams
	def getOrder(self):
		length = len(self.gladiators)
		inOrder = self.gladiators[:]
		outOrder = self.sortTeams(inOrder)
		if (len(outOrder) != length):
			print("We lost "+str(length-len(outOrder))+" gladiators while sorting!!!")
			return self.gladiators
		return self.sortTeams(self.gladiators)
		
