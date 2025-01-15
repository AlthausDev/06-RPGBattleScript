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
        self._invetory = Inventory()

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

    @property
    def inventory(self):
        return self._invetory

    # Setters
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._name = value

    @max_hp.setter
    def max_hp(self, value):
        if value <= 0:
            raise ValueError("La salud máxima debe ser mayor que 0.")
        self._max_hp = value

    @hp.setter
    def hp(self, value):
        if value < 0:
            raise ValueError("La salud no puede ser negativa.")
        self._hp = min(value, self._max_hp)  # Asegura que hp no exceda max_hp

    @max_mp.setter
    def max_mp(self, value):
        if value < 0:
            raise ValueError("El maná máximo no puede ser negativo.")
        self._max_mp = value

    @mp.setter
    def mp(self, value):
        if value < 0:
            raise ValueError("El maná no puede ser negativo.")
        self._mp = min(value, self._max_mp)  # Asegura que mp no exceda max_mp

    @atk.setter
    def atk(self, value):
        if value < 0:
            raise ValueError("El ataque no puede ser negativo.")
        self._atk = value

    @df.setter
    def df(self, value):
        if value < 0:
            raise ValueError("La defensa no puede ser negativa.")
        self._df = value

    @mdf.setter
    def mdf(self, value):
        if value < 0:
            raise ValueError("La defensa mágica no puede ser negativa.")
        self._mdf = value

    @magic.setter
    def magic(self, value):
        if not isinstance(value, list):
            raise ValueError("La magia debe ser una lista.")
        self._magic = value

    @status_effects.setter
    def status_effects(self, value):
        if not isinstance(value, list):
            raise ValueError("Los efectos de estado deben ser una lista.")
        self._status_effects = value




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
