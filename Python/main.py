from mathlab import *
from UnitClass import unit
from visuals import *


# ______________________________________________________________________________
# make your units here:
# just drop the percent sign where necessary.
# syntax is unit(type, fp, arm, man, hp, continent+defense bonuses, type bonuses (like 10% damage against armor), counters, healing, shots per turn (as in jackhammer attacks))

# say I have a mortar infantry with 10% healing to friendly infantry, 20% defense bonus, and  10% damage increase against armor/air
exampleMortar = unit("Infantry", 3, 2, 2, 50, 20, [["Armor", 10],["Air", 10]], ["Infantry"], [["Infantry", 10]],2)
exampleInfantry = unit("Infantry", 3, 1, 2, 50, 0, [], [], [],1)
testHealer = unit("idkMan", 0,0,0,10,0,[],[],[["Infantry",30]],1)


unit1 = unit("Infantry",3,1,2,50,0,[],["Infantry"],[],1)
unit2 = unit("Infantry",3,1,2,50,0,[],["Infantry"],[],1)
unit3 = unit("Infantry",3,1,2,50,0,[],["Infantry"],[],1)
unit4 = unit("Infantry",3,1,2,50,0,[],["Infantry"],[],1)
unit5 = unit("Infantry",3,1,2,50,0,[],["Infantry"],[],1)
unit6 = unit("Infantry",2,1,1,50,0,[],["Armor"],[],1)
unit7 = unit("Infantry",2,1,1,50,0,[],["Armor"],[],1)
unit8 = unit("Infantry",2,1,1,50,0,[],["Armor"],[],1)
unit9 = unit("Infantry",2,1,1,50,0,[],["Armor"],[],1)
unit10 = unit("Infantry",2,2,2,40,0,[],[],[["Infantry",10]],1)

eunit1 = unit("Armor",3,4,2,85,0,[],[],[],1)
eunit2 = unit("Armor",3,3,2,103,0,[],[],[],1)
eunit3 = unit("Armor",3,3,2,85,0,[],[],[["Special Forces",10]],1)
eunit4 = unit("Armor",3,4,1,85,0,[],[],[],1)
eunit5 = unit("Armor",2,4,2,85,0,[],[],[["Infantry",10]],1)
eunit6 = unit("Armor",3,3,1,103,0,[],[],[],1)
eunit7 = unit("Armor",3,3,3,85,0,[],[],[],1)
eunit8 = unit("Armor",4,3,2,94,0,[],[],[],1)
eunit9 = unit("Armor",2,4,2,94,0,[],[],[],1)
eunit10 = unit("Armor",2,5,1,85,0,[],[],[],1)

















# ______________________________________________________________________________

# instantBattle simulates the battle 'rounds' number of times and prints how many each side won with remaining units
# change pFriendlies and pEnemies to fit how many units you have in your battle and what you named them.
def instantBattle(rounds):
    pFriendlies = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10]#, unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20]
    pEnemies = [eunit1]#, eunit2, eunit3, eunit4, eunit5, eunit6, eunit7, eunit8, eunit9, eunit10]#, eunit11, eunit12, eunit13, eunit14, eunit15, eunit16, eunit17, eunit18, eunit19, eunit20]

    friendlies = pFriendlies.copy()
    enemies = pEnemies.copy()

    enemyWins = 0
    friendliesretreated = 0
    friendlyWins = 0
    enemiesretreated = 0
    enemyremainder = 0
    friendlyremainder = 0
    for roundnum in range(rounds):
        winner = "unknown"
        while (winner == "unknown"):
            order = initiativeRoll(friendlies, enemies)
            for i in range(len(order)):
                if (len(friendlies) > 0 and len(enemies) > 0 and order[i].alive and winner == "unknown"):
                    if (order[i] in friendlies):
                        target = enemies[random.randint(0, len(enemies) - 1)]
                        print("\n\n\n")
                        attack(order[i], target, pEnemies)
                        if (target.alive == False):
                            enemies.remove(target)
                            if (len(enemies) == 0):
                                winner = "friendlies"
                    elif (order[i] in enemies):
                        target = friendlies[random.randint(0, len(friendlies) - 1)]
                        print("\n\n\n")
                        attack(order[i], target, pFriendlies)
                        if (target.alive == False):
                            friendlies.remove(target)
                            if (len(friendlies) == 0):
                                winner = "enemies"
                    dispRes(friendlies, enemies)
                    if(winner == "unknown"):
                        winner = checkRetreat(friendlies, enemies)
        print(winner + " won!")
        if (winner == "enemies"):
            enemyWins += 1
            enemyremainder += len(enemies)
            friendliesretreated += len(friendlies)
        if (winner == "friendlies"):
            friendlyWins += 1
            friendlyremainder += len(friendlies)
            enemiesretreated += len(enemies)
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
        enemiesretreated /= friendlyWins
    if(enemyWins > 1):
        enemyremainder /= enemyWins
        friendliesretreated /= enemyWins
    print(str(friendlyWins) + " friendly wins vs " + str(enemyWins) + " enemy wins")
    print("On average, when the friendlies won, the friendlies had " + str(round(friendlyremainder)) + " units left while the enemies had " + str(round(enemiesretreated)) + " units retreat.")
    print("On average, when the enemies won, the enemies had " + str(round(enemyremainder)) + " units left while the friendlies had " + str(round(friendliesretreated)) + " units retreat.")

instantBattle(1000)

#attack(attacker,defender,liveDefenders)
#attack(exampleMortar, exampleInfantry, [exampleInfantry, testHealer])
