from mathlab import *
from UnitClass import unit

testunit1 = unit("Infantry",3,1,2,50,0,["Infantry"])
testunit2 = unit("Infantry",3,1,2,50,0,[])
testunit3 = unit("Infantry",3,1,2,50,0,[])
testunit4 = unit("Infantry",3,1,2,50,0,[])
testunit5 = unit("Infantry",3,1,2,50,0,[])
testunit6 = unit("Infantry",3,1,2,50,0,[])

friendlies = [testunit1,testunit3,testunit5]
enemies = [testunit2,testunit4,testunit6]
order = initiativeRoll(friendlies,enemies)
attack(testunit1,testunit2)