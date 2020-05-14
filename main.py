from mathlab import *
from UnitClass import unit
from visuals import *

unit1 = unit("Armor",155,15,7,737,120,[])
unit2 = unit("Armor",21,15,12,2460,35,[])
unit3 = unit("Armor",23,15,18,2856,30,[])
unit4 = unit("Armor",110,9,9,690,80,[])
unit5 = unit("Armor",105,16,9,567,80,[])
unit6 = unit("Armor",19,15,9,2268,70,[])
unit7 = unit("Armor",18,22,9,2830,40,[])
unit8 = unit("Armor",21,18,16,2064,10,[])
unit9 = unit("Armor",108,13,12,764,125,[])
unit10 = unit("Armor",16,14,9,3430,0,[])
unit11 = unit("Armor",23,14,15,2545,0,[])
unit12 = unit("Armor",28,19,16,2090,15,[])
unit13 = unit("Armor",25,25,7,1475,5,[])
unit14 = unit("Armor",28,12,11,2335,0,[])
unit15 = unit("Armor",25,22,14,1842,5,[])
unit16 = unit("Armor",26,17,14,960,10,[])
unit17 = unit("Armor",25,13,15,1329,0,[])
unit18 = unit("Armor",27,17,6,1260,10,[])
unit19 = unit("Armor",25,17,18,2064,0,[])
unit20 = unit("Armor",28,11,16,1257,20,[])

eunit1 = unit("Air",26,20,26,2340,20,[])
eunit2 = unit("Air",27,23,24,2345,0,[])
eunit3 = unit("Air",25,24,27,2265,0,[])
eunit4 = unit("Air",42,14,27,2988,10,[])
eunit5 = unit("Air",25,22,26,2025,0,[])
eunit6 = unit("Air",26,17,24,2110,0,[])
eunit7 = unit("Air",27,13,26,2265,0,[])
eunit8 = unit("Air",34,22,32,2105,0,[])
eunit9 = unit("Air",23,26,27,2190,0,[])
eunit10 = unit("Air",29,17,26,2345,10,[])
eunit11 = unit("Armor",27,21,21,4180,0,[])
eunit12 = unit("Armor",24,15,21,3935,0,[])
eunit13 = unit("Armor",21,23,18,4425,0,[])
eunit14 = unit("Armor",22,19,20,3815,0,[])
eunit15 = unit("Armor",24,26,20,3445,10,[])
eunit16 = unit("Armor",27,20,18,4060,40,[])
eunit17 = unit("Armor",25,15,19,3935,20,[])
eunit18 = unit("Armor",24,21,19,4185,10,[])
eunit19 = unit("Armor",28,19,23,3695,0,[])
eunit20 = unit("Armor",24,13,27,3935,20,[])



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

