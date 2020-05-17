from mathlab import *
from UnitClass import unit
from visuals import *


# ______________________________________________________________________________
# make your units here:
# just drop the percent sign where necessary.
# syntax is unit(type, fp, arm, man, hp, continent+defense bonuses, type bonuses (like 10% damage against armor), counters, healing)

# say I have a mortar infantry with 10% healing to friendly infantry, 20% defense bonus, and  10% damage increase against armor/air
exampleMortar = unit("Infantry", 3, 1, 2, 50, 20, [["Armor", 10],["Air", 10]], ["Infantry"], [["Infantry", 10]])
exampleInfantry = unit("Infantry", 3, 1, 2, 50, 0, [], [], [])


# ______________________________________________________________________________

# instantBattle simulates the battle 'rounds' number of times and prints how many each side won with remaining units
# change pFriendlies and pEnemies to fit how many units you have in your battle and what you named them.
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