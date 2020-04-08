from mathlab import *
from UnitClass import unit
from visuals import *

unit1 = unit("Armor",15,17,13,1478,0,[])
unit2 = unit("Armor",63,15,10,493,4,[])
unit3 = unit("Armor",15,11,11,1698,0,[])
unit4 = unit("Armor",16,19,10,985,10,[])
unit5 = unit("Armor",15,17,15,1045,0,[])
unit6 = unit("Armor",51,14,15,419,0,[])
unit7 = unit("Armor",30,13,11,517,0,[])
unit8 = unit("Armor",13,16,12,888,0,[])
unit9 = unit("Armor",40,15,10,517,7,[])
unit10 = unit("Armor",30,10,11,615,10,[])
unit11 = unit("Air",80,9,9,112,88,["Air"])
unit12 = unit("Air",70,11,11,136,90,["Air"])
unit13 = unit("Air",88,12,7,136,30,["Air"])
unit14 = unit("Air",16,9,5,420,60,["Air"])
unit15 = unit("Armor",15,11,8,2168,30,[])
unit16 = unit("Air",100,5,11,50,80,["Air"])
unit17 = unit("Air",13,5,12,460,40,["Air"])
unit18 = unit("Air",13,9,10,440,20,["Air"])
unit19 = unit("Air",20,6,10,480,10,["Air"])
unit20 = unit("Air",85,5,6,160,70,["Air"])

eunit1 = unit("Air",130,20,13,249,0,[])
eunit2 = unit("Air",22,24,24,823,15,[])
eunit3 = unit("Air",24,19,17,1029,0,[])
eunit4 = unit("Air",22,15,21,1485,30,[])
eunit5 = unit("Air",69,9,21,436,10,[])
eunit6 = unit("Air",20,11,18,1167,10,[])
eunit7 = unit("Air",16,20,15,1133,0,[])
eunit8 = unit("Air",63,20,11,405,10,[])
eunit9 = unit("Air",75,14,19,344,0,[])
eunit10 = unit("Air",20,15,20,1015,10,[])
eunit11 = unit("Armor",51,10,11,189,10,["Armor"])
eunit12 = unit("Air",80,10,11,208,0,["Air"])
eunit13 = unit("Air",72,10,10,216,23,["Air"])
eunit14 = unit("Armor",23,11,11,2142,15,[])
eunit15 = unit("Armor",26,11,10,1920,0,[])
eunit16 = unit("Armor",22,12,14,2061,10,[])
eunit17 = unit("Armor",25,11,10,2825,75,[])
eunit18 = unit("Air",84,15,10,176,0,["Air"])
eunit19 = unit("Armor",25,12,10,1989,5,[])
eunit20 = unit("Armor",22,10,10,1992,15,[])



def instantBattle(rounds):
    pFriendlies = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10, unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20]
    pEnemies = [eunit1, eunit2, eunit3, eunit4, eunit5, eunit6, eunit7, eunit8, eunit9, eunit10, eunit11, eunit12, eunit13, eunit14, eunit15, eunit16, eunit17, eunit18, eunit19, eunit20]

    friendlies = pFriendlies.copy()
    enemies = pEnemies.copy()

    enemyWins = 0
    friendlyWins = 0
    enemyremainder = 0
    friendlyremainder = 0
    for roundnum in range(rounds):
        winner = "unknown"
        while (winner == "unknown"):
            order = initiativeRoll(friendlies, enemies)
            for i in range(len(order)):
                if (len(friendlies) > 0 and len(enemies) > 0):
                    if (order[i] in friendlies):
                        target = enemies[random.randint(0, len(enemies) - 1)]
                        print("\n\n\n")
                        attack(order[i], target)
                        if (target.alive == False):
                            enemies.remove(target)
                            if (len(enemies) == 0):
                                winner = "friendlies"
                    elif (order[i] in enemies):
                        target = friendlies[random.randint(0, len(friendlies) - 1)]
                        print("\n\n\n")
                        attack(order[i], target)
                        if (target.alive == False):
                            friendlies.remove(target)
                            if (len(friendlies) == 0):
                                winner = "enemies"
                    dispRes(friendlies, enemies)
        print(winner + " won!")
        if (winner == "enemies"):
            enemyWins += 1
            enemyremainder += len(enemies)
        if (winner == "friendlies"):
            friendlyWins += 1
            friendlyremainder += len(friendlies)
        #reset
        friendlies = pFriendlies.copy()
        enemies = pEnemies.copy()
        for unit in pFriendlies:
            unit.hp = unit.maxhp
            unit.alive = True
        for unit in pEnemies:
            unit.hp = unit.maxhp
            unit.alive = True

    if(friendlyWins > 1):
        friendlyremainder /= friendlyWins
    if(enemyWins > 1):
        enemyremainder /= enemyWins
    print(str(friendlyWins) + " friendly wins vs " + str(enemyWins) + " enemy wins")
    print("On average, when the corresponding side won, the enemies had " + str(round(enemyremainder)) + " units left while friendlies had " + str(friendlyremainder) + " units left.")

instantBattle(500)

