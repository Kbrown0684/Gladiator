from math import floor
import Gladiator
import Arena


##\mainpage Gladiator Project
##
##\section intro_sec Introduction
##
##This is why we do documentation, Kevin!
##additional witty remark


adam= Gladiator.Gladiator()
adam.name= "Adam"
adam.team= "Team A"
adam.setWeapon(5,1,"Greatsword")
adam.setArmor(6,1,"Breastplate")
adam.refresh()

bob = Gladiator.Gladiator()
bob.name = "Bob"
bob.team = "Team A"
bob.setWeapon(3, 3, "Shortsword")
bob.setArmor(4, 3, "Leather")
bob.refresh()

carl= Gladiator.Gladiator()
carl.name= "Carl"
carl.team= "Team B"
carl.setWeapon(5,2,"Greatsword")
carl.setArmor(6,2,"Breastplate")
carl.refresh()

dave= Gladiator.Gladiator()
dave.name= "Dave"
dave.team= "Team B"
dave.setWeapon(5,4,"Greatsword")
dave.setArmor(6,4,"Breastplate")
dave.refresh()

theArena = Arena.Arena((10,10), (adam, bob), (carl, dave))

print (adam)
print("")
print (bob)
print("")
print (carl)
print("")
print(dave)
print("")

turnOrder = theArena.gladiators
for gladiator in turnOrder:
	print(gladiator.getName())
print("")
