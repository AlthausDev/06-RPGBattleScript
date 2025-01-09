class Spell:
    def __init__(self, name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg

    def __repr__(self):
        return f"{self.name} (Cost: {self.cost}, Damage: {self.dmg})"
