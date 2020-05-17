class unit:
    unitID = 1
    def __init__(self, type, fp, arm, man, hp, cumulativeBoosts, unitBoosts, counters, healing):
        self.id = unit.unitID
        unit.unitID += 1
        self.type = type
        self.firepower = fp
        self.armor = arm
        self.maneuver = man
        self.hp = hp
        self.maxhp = hp
        self.bonuses = cumulativeBoosts #30% is input as just 30
        self.typeBonuses = unitBoosts
        self.counters = counters
        self.iRoll = 0
        self.alive = True
        self.healing = healing
