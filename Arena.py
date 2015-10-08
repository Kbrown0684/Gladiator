from Gladiator import Gladiator


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

