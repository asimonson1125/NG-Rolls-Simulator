from mathlab import *
from UnitClass import unit
from visuals import *

unit1 = unit("Armor",16,11,25,1293,0,[])
unit2 = unit("Armor",19,9,13,1290,0,[])
unit3 = unit("Armor",19,19,12,1415,0,[])
unit4 = unit("Armor",18,17,7,1355,0,[])
unit5 = unit("Armor",10,16,15,1783,0,[])
unit6 = unit("Armor",15,21,18,1233,0,[])
unit7 = unit("Armor",16,22,13,985,0,[])
unit8 = unit("Armor",95,10,10,443,60,[])
unit9 = unit("Armor",14,15,13,1413,0,[])
unit10 = unit("Armor",17,17,21,1230,0,[])
unit11 = unit("Armor",112,17,18,493,20,[])
unit12 = unit("Armor",72,15,17,492,0,[])
unit13 = unit("Armor",81,17,15,491,10,[])
unit14 = unit("Armor",15,14,10,2583,0,[])
unit15 = unit("Armor",19,18,9,2136,0,[])
unit16 = unit("Armor",90,18,12,417,0,[])
unit17 = unit("Armor",18,18,12,1995,0,[])
unit18 = unit("Armor",87,12,16,443,0,[])
unit19 = unit("Armor",72,20,15,394,0,[])
unit20 = unit("Armor",14,14,17,2364,0,[])

eunit1 = unit("Armor",27,21,21,3344,10,[])
eunit2 = unit("Armor",24,15,21,3148,0,[])
eunit3 = unit("Armor",21,23,18,3540,0,[])
eunit4 = unit("Armor",22,19,20,3052,0,[])
eunit5 = unit("Armor",24,26,20,2756,0,[])
eunit6 = unit("Armor",27,20,18,3248,0,[])
eunit7 = unit("Armor",25,15,19,3148,0,[])
eunit8 = unit("Armor",24,21,19,3348,0,[])
eunit9 = unit("Armor",28,19,23,2956,0,[])
eunit10 = unit("Armor",24,13,27,3148,0,[])
eunit11 = unit("Armor",22,11,22,3200,0,[])
eunit12 = unit("Armor",22,9,23,3320,0,[])
eunit13 = unit("Armor",28,15,22,3575,0,[])
eunit14 = unit("Armor",126,10,23,419,90,[])
eunit15 = unit("Armor",102,8,19,590,70,[])
eunit16 = unit("Armor",25,15,20,2952,20,[])
eunit17 = unit("Armor",23,15,24,3570,0,[])
eunit18 = unit("Armor",90,17,18,443,60,[])
eunit19 = unit("Armor",30,10,23,2460,10,[])
eunit20 = unit("Armor",132,13,17,442,40,[])




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

#attack(attacker,defender)