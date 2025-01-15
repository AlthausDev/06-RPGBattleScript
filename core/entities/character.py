import random

class Character:
    def __init__(self, name, hp=10, mp=10, atk=2, df=0, mdf=0, magic=None):
        self._name = name
        self._max_hp = hp
        self._hp = hp
        self._max_mp = mp
        self._mp = mp
        self._atk = atk
        self._df = df
        self._mdf = mdf
        self._magic = magic or []
        self._status_effects = []

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    @property
    def max_mp(self):
        return self._max_mp

    @property
    def mp(self):
        return self._mp

    @property
    def atk(self):
        return self._atk

    @property
    def df(self):
        return self._df

    @property
    def mdf(self):
        return self._mdf

    @property
    def magic(self):
        return self._magic

    @property
    def status_effects(self):
        return self._status_effects

    # Métodos de la clase
    def generate_damage(self):
        return random.randint(self.atk - 5, self.atk + 5)

    def generate_spell_damage(self, spell_choice):
        spell = self.magic[spell_choice]

        if self.mp >= spell.cost:
            self.reduce_mp(spell.cost)
            return random.randint(spell.dmg - 5, spell.dmg + 5)
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
        self._hp -= effective_dmg
        if self._hp < 0:
            self._hp = 0
        return effective_dmg  # Devuelve solo el daño real

    def apply_status_effects(self):
        for effect in self.status_effects:
            effect.apply(self)
            if effect.duration <= 0:
                self.status_effects.remove(effect)

    def reduce_mp(self, cost):
        self._mp -= cost

    def is_alive(self):
        return self.hp > 0
