import random

from core.mechanics.spells import magic


class Character:
    def __init__(self, name, hp=10, mp=10, atk=2, df=0, mdf=0, magic=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.mdf = mdf
        self.magic = magic or []
        self.status_effects = []

    def generate_damage(self):
        return random.randint(self.atk - 5, self.atk + 5)

    def generate_spell_damage(self, spell_choice):
        spell = magic[spell_choice]

        if self.mp >= spell["cost"]:

            self.reduce_mp(spell["cost"])
            return random.randint(spell["dmg"] - 5, spell["dmg"] + 5)

        else:
            print("\nNot enough MP!")
            return None


    def take_damage(self, dmg, type):

        df = 0
        if type == "physical":
            df = self.df
        elif type == "magic":
            df = self.mdf

        effective_dmg = max(0, dmg - df)
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
