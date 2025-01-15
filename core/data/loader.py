import json
from core.entities.base.spells import Spell

def load_spells(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    spells = {}
    for category, spell_list in data.items():
        spells[category] = [
            Spell(spell.get("name"), spell.get("cost"), spell.get("dmg", 0), spell.get("heal", 0))
            for spell in spell_list
        ]

    return spells