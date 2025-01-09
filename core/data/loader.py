import json
from core.entities.spells import Spell

def load_spells(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)

    spells = {}
    for category, spell_list in data.items():
        spells[category] = [Spell(spell["name"], spell["cost"], spell["dmg"]) for spell in spell_list]

    return spells