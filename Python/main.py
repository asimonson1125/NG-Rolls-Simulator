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


unit1 = unit("Armor",11,17,13,234,60,[["Armor",40], ["Static",40]],[],[["Air",20]],1)
unit2 = unit("Armor",14,15,10,260,40,[["Infantry",20], ["Armor",20]],[],[["Armor",20], ["Special Forces",20], ["Air",40]],1)
unit3 = unit("Infantry",13,12,8,128,40,[],[],[["Air",20], ["Static",20], ["Special Forces",20], ["Infantry",20]],1)
unit4 = unit("Infantry",8,19,10,104,40,[["Static",20]],[],[["Static",20]],1)
unit5 = unit("Infantry",12,15,10,104,80,[["Special forces",20], ["Infantry",20]],[],[["Infantry",20], ["Static",20]],1)
unit6 = unit("Infantry",8,14,17,80,40,[["Special forces",20]],["Armor"],[["Air",40], ["Static",20]],1)
unit7 = unit("Infantry",17,8,12,104,80,[["Infantry",40]],[],[["Special Forces",20]],1)
unit8 = unit("Infantry",14,10,13,92,20,[["Armor",40], ["Special forces",20]],["Armor"],[["Special Forces",40], ["Armor",20], ["Air",20]],1)
unit9 = unit("Infantry",12,14,10,110,0,[["Static",20], ["Air",40]],[],[["Air",20], ["Static",20], ["Special Forces",20], ["Armor",20]],1)
unit10 = unit("Infantry",9,12,12,116,20,[["Static",20], ["Air",20], ["Special forces",20], ["Infantry",20]],["Armor"],[["Infantry",20], ["Static",20]],1)
unit11 = unit("Infantry",13,10,11,110,80,[],["Armor"],[["Static",40], ["Special Forces",20], ["Armor",20]],1)
unit12 = unit("Infantry",11,9,13,128,60,[],[],[["Static",20], ["Infantry",40], ["Special Forces",20]],1)
unit13 = unit("Infantry",13,15,13,80,80,[],[],[["Air",40]],1)
unit14 = unit("Infantry",15,11,12,98,20,[["Infantry",20], ["Special forces",20]],[],[["Static",20], ["Armor",20], ["Infantry",40]],1)
unit15 = unit("Infantry",12,8,13,128,20,[["Special forces",20], ["Air",20]],[],[["Armor",20], ["Special Forces",40]],1)
unit16 = unit("Infantry",15,13,12,74,40,[["Static",20], ["Infantry",20]],["Armor"],[["Static",20], ["Air",20]],1)
unit17 = unit("Infantry",11,12,12,104,40,[["Air",20], ["Armor",40]],["Armor"],[["Static",20], ["Armor",20]],1)
unit18 = unit("Infantry",12,7,16,116,20,[["Static",20], ["Air",20]],[],[["Air",20], ["Infantry",20]],1)
unit19 = unit("Infantry",12,13,13,98,80,[["Static",20], ["Air",20]],[],[["Armor",20], ["Infantry",20]],1)
unit20 = unit("Infantry",7,14,15,110,40,[["Static",40], ["Armor",20]],[],[["Armor",20], ["Air",20]],1)

eunit1 = unit("Air",14,8,16,182,0,[["Infantry",30], ["Static",20]],["Infantry", "Armor"],[["Special Forces",10]],1)
eunit2 = unit("Air",18,12,9,189,0,[["Infantry",30]],["Infantry", "Armor"],[["Armor",10]],1)
eunit3 = unit("Air",22,12,11,140,0,[["Special forces",10], ["Infantry",50]],["Infantry", "Armor"],[],1)
eunit4 = unit("Air",23,8,17,140,0,[["Infantry",30]],["Infantry", "Armor"],[],1)
eunit5 = unit("Air",20,8,15,147,0,[["Infantry",40]],["Infantry", "Armor"],[["Special Forces",10]],1)
eunit6 = unit("Air",19,10,10,161,0,[["Infantry",50], ["Static",20]],["Infantry", "Armor"],[],1)
eunit7 = unit("Air",21,11,13,147,10,[["Infantry",30]],["Infantry", "Armor"],[["Armor",10]],1)
eunit8 = unit("Air",17,10,13,182,0,[["Infantry",30]],["Infantry", "Armor"],[["Air",10]],1)
eunit9 = unit("Air",21,10,11,126,0,[["Infantry",40]],["Infantry", "Armor"],[["Static",10], ["Special Forces",10], ["Air",30], ["Armor",10]],1)
eunit10 = unit("Air",15,14,14,147,0,[["Infantry",40], ["Special forces",10]],["Infantry", "Armor"],[],1)


# ______________________________________________________________________________

# instantBattle simulates the battle 'rounds' number of times and prints how many each side won with remaining units
# change pFriendlies and pEnemies to fit how many units you have in your battle and what you named them.
def instantBattle(rounds):
    pFriendlies = [unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9, unit10, unit11, unit12, unit13, unit14, unit15, unit16, unit17, unit18, unit19, unit20]
    pEnemies = [eunit1, eunit2, eunit3, eunit4, eunit5, eunit6, eunit7, eunit8, eunit9, eunit10]#, eunit11, eunit12, eunit13, eunit14, eunit15, eunit16, eunit17, eunit18, eunit19, eunit20]

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

instantBattle(100)

#attack(attacker,defender,liveDefenders)
#attack(exampleMortar, exampleInfantry, [exampleInfantry, testHealer])
