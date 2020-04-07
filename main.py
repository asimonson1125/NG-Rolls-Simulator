from mathlab import *
from UnitClass import unit

f22 = unit("Infantry",3,9,10,50,20,["Infantry"])
testunit2 = unit("Infantry",20,15,20,50,10,[])
testunit3 = unit("Infantry",3,1,2,50,0,[])
testunit4 = unit("Infantry",3,1,2,50,0,[])
testunit5 = unit("Infantry",3,1,2,50,0,[])
testunit6 = unit("Infantry",3,1,2,50,0,[])

friendlies = [f22,testunit3,testunit5]
enemies = [testunit2,testunit4,testunit6]
order = initiativeRoll(friendlies,enemies)

attack(testunit2,f22)