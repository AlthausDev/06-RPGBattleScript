class StatusEffect:
    def __init__(self, name, duration, apply_effect):
        self.name = name
        self.duration = duration
        self.apply_effect = apply_effect

    def apply(self, target):
        self.apply_effect(target)
        self.duration -= 1

def poison_effect(target):
    dmg = 10
    target.take_damage(dmg)
    print(f"{target.name} takes {dmg} poison damage!")
