from math import floor
import Gladiator
import Arena

adam= Gladiator.Gladiator()
adam.name= "Adam"
adam.team= "Team A"
adam.setWeapon(5,4,"Greatsword")
adam.setArmor(6,4,"Breastplate")
adam.refresh()

bob = Gladiator.Gladiator()
bob.name = "Bob"
bob.team = "Team B"
bob.setWeapon(3, 1, "Shortsword")
bob.setArmor(4, 1, "Leather")
bob.refresh()


##Test attacking
adam.attack(bob)
bob.attack(adam)

print (adam)
print("")
print (bob)
print("")

