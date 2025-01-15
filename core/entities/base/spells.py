class Spell:
    def __init__(self, name, cost, dmg = 0, heal = 0):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.heal = heal

    def __repr__(self):
        if self.dmg > 0:
            return f"{self.name} (Cost: {self.cost}, Damage: {self.dmg})"
        elif self.heal > 0:
            return f"{self.name} (Cost: {self.cost}, Heal: {self.heal})"
        return f"{self.name} (Cost: {self.cost})"