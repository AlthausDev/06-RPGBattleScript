import random

class Character:
    def __init__(self, name, hp, mp, atk, df, magic=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.magic = magic or []
        self.status_effects = []  # Lista de efectos de estado

    def generate_damage(self):
        return random.randint(self.atk - 10, self.atk + 10)

    def take_damage(self, dmg):
        effective_dmg = max(0, dmg - self.df)  # Daño real después de la defensa
        self.hp -= effective_dmg
        if self.hp < 0:
            self.hp = 0
        return effective_dmg  # Devuelve solo el daño real

    def apply_status_effects(self):
        for effect in self.status_effects:
            effect.apply(self)
            if effect.duration <= 0:
                self.status_effects.remove(effect)

    def reduce_mp(self, cost):
        self.mp -= cost

    def is_alive(self):
        return self.hp > 0
