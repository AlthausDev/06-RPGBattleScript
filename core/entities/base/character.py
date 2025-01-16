import random
from typing import List, Optional

from core.entities.base.inventory import Inventory
from core.entities.base.spell import Spell


class Character:
    def __init__(self, name: str, hp: int = 10, mp: int = 10, atk: int = 2, defense: int = 0, magic_defense: int = 0, magic: Optional[List[Spell]] = None):
        self._name = name
        self._max_hp = max(1, hp)
        self._hp = hp
        self._max_mp = max(0, mp)
        self._mp = mp
        self._atk = max(0, atk)
        self._defense = max(0, defense)
        self._magic_defense = max(0, magic_defense)
        self._magic = magic or []
        self._status_effects = []
        self._inventory = Inventory()

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
    def defense(self):
        return self._defense

    @property
    def magic_defense(self):
        return self._magic_defense

    @property
    def magic(self):
        return self._magic

    @property
    def status_effects(self):
        return self._status_effects

    @property
    def inventory(self):
        return self._inventory

    # Setters
    @hp.setter
    def hp(self, value):
        self._hp = max(0, min(value, self._max_hp))

    @mp.setter
    def mp(self, value):
        self._mp = max(0, min(value, self._max_mp))

    # Métodos
    def generate_damage(self):
        return random.randint(max(0, self._atk - 5), self._atk + 5)

    def generate_spell_damage(self, spell_choice: int):
        if not (0 <= spell_choice < len(self._magic)):
            raise ValueError("Elección de hechizo inválida.")
        spell = self._magic[spell_choice]
        if self._mp >= spell.cost:
            self.reduce_mp(spell.cost)
            return random.randint(max(0, spell.dmg - 5), spell.dmg + 5)
        else:
            print("Not enough MP!")
            return None

    def take_damage(self, dmg: int, dmg_type: str = "physical"):
        defense = self._defense if dmg_type == "physical" else self._magic_defense
        effective_dmg = max(0, dmg - defense)
        self.hp -= effective_dmg
        return effective_dmg

    def apply_status_effects(self):
        for effect in list(self._status_effects):
            effect.apply(self)
            if effect.duration <= 0:
                self._status_effects.remove(effect)

    def reduce_mp(self, cost: int):
        self.mp -= cost

    def is_alive(self) -> bool:
        return self.hp > 0
