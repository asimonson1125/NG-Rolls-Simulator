import math
import random
def baseDamage(fp,arm):
    return math.ceil(math.sqrt(47.5*(fp+1)) + (math.sqrt(47.5*(arm+20))-29.5))

def damagemod(fp,bonus):
    return fp*4*(bonus+1)

def mitigation(arm,bonus):
    return arm*4*(bonus+1)

def hitResult(firerMan,targetMan):
    baseRoll = random.randint(0,100)
    if(baseRoll <= 5):
        return "MISS"
    elif(baseRoll >= 95):
        return "CRIT"
    elif(baseRoll >= 80):
        return "HIT"
    modifier = firerMan*10-50
    toBeat = targetMan*10
    finalRoll = baseRoll + modifier
    if(finalRoll > toBeat):
        return "HIT"
    else:
        return "GRAZE"

def attack(firer,target):
    roll = hitResult(firer.maneuver,target.maneuver)
    print(roll)
    if(roll == "MISS"):
        return
    damage = math.ceil(baseDamage(firer.firepower,firer.armor)) + math.ceil(damagemod(firer.firepower,firer.bonuses))
    damage -= mitigation(target.armor,target.bonuses)
    #healing rounds normally
    healing = round(damage*(target.bonuses/100))
    if(roll == "CRIT"):
        damage *= 1.5
    elif(roll == "GRAZE"):
        damage *= .5
    damage = math.ceil(damage - healing)
    print(str(damage) + " damage done.")
    target.hp -= damage
    #check if dead
    #
    return
