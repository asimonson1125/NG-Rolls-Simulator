import math
import random


def baseDamage(fp, arm):
    return math.ceil(math.sqrt(47.5 * (fp + 1)) + (math.sqrt(47.5 * (arm + 20)) - 29.5))


def damagemod(fp, bonus):
    return fp * 4 * ((bonus / 100) + 1)


def mitigation(arm, bonus):
    return arm * 4 * ((bonus / 100) + 1)


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


def attack(firer, target):
    if (firer.alive == False):
        return  # he dead bruh
    if (target.type in firer.counters):
        fp = 1.25 * firer.firepower + 6
        man = 1.25 * firer.maneuver + 3
    else:
        fp = firer.firepower
        man = firer.maneuver
    if (firer.type in target.counters):
        tArm = 1.25 * target.armor + 3
        tMan = 1.25 * target.maneuver + 3
    else:
        tArm = target.armor
        tMan = target.maneuver

    roll = hitResult(man * (firer.bonuses/100 + 1), tMan * (target.bonuses/100 + 1))
    print(roll)
    if (roll == "MISS"):
        return
    damage = math.ceil(baseDamage(firer.firepower, firer.armor)) + math.ceil(damagemod(fp, firer.bonuses))
    damage -= mitigation(tArm, target.bonuses)
    # healing rounds normally, counter 50% reduction is listed under healing
    # also if the target counters the firer, healing is applied before crit multiplier (NOT GRAZE!)
    if (firer.type in target.counters):
        healing = round(damage * ((target.healing + 50) / 100))
        if(roll == "CRIT"):
            damage -= healing
            damage *= 1.5
            damage = math.ceil(damage)
        else:
            if(roll == "GRAZE"):
                damage *= .5
            damage -= healing
            damage = math.ceil(damage)
    else:
        healing = round(damage * (target.healing / 100))
        if (roll == "CRIT"):
            damage *= 1.5
        elif (roll == "GRAZE"):
            damage *= .5
        damage = math.ceil(damage - healing)
    # damage cannot be 0 or negative, so this is my compensation since we don't know how th real calculation works
    if (damage < 5):
        damage = 2
    print(str(damage) + " damage done.")
    target.hp -= damage
    if (target.hp <= 0):
        target.alive = False
    return


def initiativeRoll(friendlies, enemies):
    # roll random number then multiply by hp percentage (estimate).  Return array with objects in order
    unitList = friendlies + enemies
    for x in unitList:
        initialRoll = random.randint(0, 100)
        x.iRoll = initialRoll * ((x.hp / x.maxhp) ** 2)  # hp factor squared for more dramatic effect
        if("Special Forces" in x.counters):
            x.iRoll *= 3
    # Now each unit is assigned an initiative roll.  Now to sort them.
    unitList.sort(key=lambda x: x.iRoll, reverse=True)
    return unitList
