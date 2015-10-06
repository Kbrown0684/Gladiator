import Gladiator

bob = Gladiator.Gladiator()

##Test print variables from methods
print (bob.getHealth())
print (bob.getSpeed())
print (bob.getDistance())
print (bob.getDamage())
print ("")

##Test print variables w/o methods
print (bob.health)
print ("")

##Test modify variables
bob.health = 1337
print (bob.getHealth())
print ("")
