from mathlab import *
from UnitClass import unit

unit1 = unit("Infantry",27,15,15,2286,0,[])
unit2 = unit("Infantry",26,15,18,1590,0,[])
testunit3 = unit("Infantry",3,1,2,50,0,[])
testunit4 = unit("Infantry",3,1,2,50,0,[])
testunit5 = unit("Infantry",3,1,2,50,0,[])
testunit6 = unit("Infantry",3,1,2,50,0,[])

friendlies = [unit1]
enemies = [unit2]
winner = "unknown"

#while(winner == "unknown"):
while(unit1.hp > 0 and unit2.hp > 0):
    order = initiativeRoll(friendlies, enemies)
    for i in range(len(order)):
        if(order[i] in friendlies):
            attack(order[i],enemies[random.randint(0,len(enemies)-1)])
            if(len(enemies) == 0):
                winner = "friendlies"
        elif(order[i] in enemies):
            attack(order[i],friendlies[random.randint(0,len(friendlies)-1)])
            if (len(friendlies) == 0):
                winner = "enemies"
        else:
            print("bruh what")

        #display results
        print("unit1 has " + str(unit1.hp) + " hp")
        print("unit2 has " + str(unit2.hp) + " hp\n")
        #input("Press enter to resolve next attack")

