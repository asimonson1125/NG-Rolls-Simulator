from mathlab import *
from UnitClass import unit
from visuals import *

unit1 = unit("Armor",126,10,15,467,130,[])
unit2 = unit("Armor",125,17,20,590,160,[])
unit3 = unit("Armor",14,18,14,1548,80,[])
unit4 = unit("Armor",20,16,12,1773,20,[])
unit5 = unit("Armor",19,26,13,1698,50,[])
unit6 = unit("Armor",16,14,19,1995,10,[])
unit7 = unit("Armor",22,14,13,1551,40,[])
unit8 = unit("Armor",17,16,15,1845,20,[])
unit9 = unit("Armor",128,24,13,393,10,[])
unit10 = unit("Armor",15,13,14,2142,50,[])
unit11 = unit("Air",21,18,20,1556,10,[])
unit12 = unit("Air",19,10,22,1744,5,[])
unit13 = unit("Air",21,16,21,1500,5,[])
unit14 = unit("Air",23,13,18,1864,0,[])
unit15 = unit("Air",26,14,19,1436,5,[])
unit16 = unit("Air",20,15,20,1680,0,[])
unit17 = unit("Air",23,14,17,1624,5,[])
unit18 = unit("Air",19,17,17,1680,5,[])
unit19 = unit("Air",80,14,23,258,0,[])
unit20 = unit("Air",23,6,27,1628,5,[])

eunit1 = unit("Air",21,18,14,1620,5,[])
eunit2 = unit("Air",20,11,15,1744,10,[])
eunit3 = unit("Air",18,16,21,1376,0,[])
eunit4 = unit("Air",100,14,14,373,5,[])
eunit5 = unit("Air",156,15,14,264,20,[])
eunit6 = unit("Air",104,14,24,281,0,[])
eunit7 = unit("Air",19,15,20,1560,10,[])
eunit8 = unit("Air",23,14,14,1620,0,[])
eunit9 = unit("Air",21,9,19,1862,0,[])
eunit10 = unit("Air",12,12,13,1996,20,[])
eunit11 = unit("Armor",25,18,15,2095,10,[])
eunit12 = unit("Armor",21,14,12,2465,10,[])
eunit13 = unit("Armor",23,16,6,2585,0,[])
eunit14 = unit("Armor",26,11,9,2460,0,[])
eunit15 = unit("Armor",23,12,6,2345,0,[])
eunit16 = unit("Armor",18,18,20,2465,0,[])
eunit17 = unit("Armor",19,9,13,2580,0,[])
eunit18 = unit("Armor",21,9,14,3070,0,[])
eunit19 = unit("Armor",23,18,14,2215,5,[])
eunit20 = unit("Armor",20,15,5,2955,25,[])



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
    print("On average, when the corresponding side won, the friendlies had " + str(round(friendlyremainder)) + " units left while enemies had " + str(round(enemyremainder)) + " units left.")

instantBattle(100)

