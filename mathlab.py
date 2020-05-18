import math
import random


def baseDamage(fp, arm):
    return math.ceil(math.sqrt(47.5 * (fp + 1)) + (math.sqrt(47.5 * (arm + 20)) - 29.5))


def damagemod(fp, bonus):
    return fp * ((bonus / 100) + 1) * 4


def mitigation(arm, bonus):
    return arm * ((bonus / 100) + 1) *4


def hitResult(firerMan, targetMan):
    baseRoll = random.randint(0, 100)
    if (baseRoll <= 5):
        return "MISS"
    elif (baseRoll >= 95):
        return "CRIT"
    elif (baseRoll >= 80):
        return "HIT"
    modifier = firerMan * 10 - 50
    toBeat = targetMan * 10
    finalRoll = baseRoll + modifier
    if (finalRoll > toBeat):
        return "HIT"
    else:
        return "GRAZE"


def attack(firer, target, targetAllies):
    if (firer.alive == False):
        return  # he dead bruh
    targetBonus = 0
    for i in firer.typeBonuses:
        if(i[0] == target.type):
            targetBonus = i[1]
    multiplier = (firer.bonuses + targetBonus)
    if (target.type in firer.counters):
        fp = (1.25 * firer.firepower + 6)
        man = (1.25 * firer.maneuver + 3)
    else:
        fp = firer.firepower
        man = firer.maneuver
    for i in target.typeBonuses:
        if(i[0] == target.type):
            targetBonus = i[1]
    tMultiplier = (target.bonuses + targetBonus)
    if (firer.type in target.counters):
        tArm = (1.25 * target.armor + 3)
        tMan = (1.25 * target.maneuver + 3)
    else:
        tArm = target.armor
        tMan = target.maneuver
    roll = hitResult(man * (multiplier/100 + 1), tMan * (tMultiplier/100 + 1))
    print(roll)
    if (roll == "MISS"):
        return
    damage = math.ceil(baseDamage(firer.firepower, firer.armor)) + math.ceil(damagemod(fp, multiplier)) # 90% sure base doesn't include bonuses or counter stat
    damage -= mitigation(tArm, tMultiplier)
    if (roll == "CRIT"):
        damage *= 1.5
    elif (roll == "GRAZE"):
        damage *= .5
    # healing
    damageReduct = 0
    for i in targetAllies:
        for type in i.healing:
            if (type[0] == target.type):
                damageReduct += type[1]
    if(damageReduct > 30): # 30% is max friendly damage reduction
        damageReduct = 30
    if (firer.type in target.counters): # healing rounds normally, counter 50% reduction is listed under healing
        healing = round(damage * ((damageReduct + 50) / 100))
    else:
        healing = round(damage * (damageReduct / 100))
    damage = math.ceil(damage - healing)
    # damage cannot be 0 or negative, so this is my compensation since we don't know how the real calculation works
    if (damage < 5):
        damage = 5
    print(str(damage) + " damage done.")
    target.hp -= damage
    if (target.hp <= 0):
        target.alive = False
    return


def initiativeRoll(friendlies, enemies):
    # roll random number then multiply by hp percentage (estimate).  Return array with objects in order
    unitList = []
    allUnits = friendlies + enemies
    for unit in allUnits:
        for i in range(unit.jackhammerFactor):
            unitList.append([unit,0])
    for x in unitList:
        iRoll = random.randint(0, 100)
        x[1] = iRoll * ((x[0].hp / x[0].maxhp) ** 2)  # hp factor squared for more dramatic effect
        if("Special Forces" in x[0].counters):
            x[1] *= 3
    # Now each unit is assigned an initiative roll.  Now to sort them.
    unitList.sort(key=lambda x: x[1], reverse=True)
    ret = []
    for i in unitList:
        ret.append(i[0])
    return ret
