from mathlab import *
from UnitClass import unit

testunit1 = unit("Infantry",3,1,2,50,0)
testunit2 = unit("Infantry",3,1,2,50,0)
print(str(testunit1.hp) + ", " + str(testunit2.hp))
attack(testunit1,testunit2)
print(str(testunit1.hp) + ", " + str(testunit2.hp))
