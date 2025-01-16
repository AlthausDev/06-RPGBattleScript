import json

from core.entities.base.spell import Spell


def load_spells(file_path):
    """
    Carga hechizos desde un archivo JSON y los organiza por categoría.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los datos de los hechizos.

    Returns:
        dict: Un diccionario donde las claves son las categorías y los valores son listas de objetos Spell.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{file_path}' no se encontró.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al parsear el JSON en '{file_path}': {e}")

    spells = {}
    for category, spell_list in data.items():
        if not isinstance(spell_list, list):
            raise ValueError(f"La categoría '{category}' debe contener una lista de hechizos.")

        spells[category] = [
            Spell(
                id=spell.get("id", 0),
                name=spell.get("name", "Desconocido"),
                cost=spell.get("cost", 0),
                dmg=spell.get("dmg", 0),
                heal=spell.get("heal", 0)
            )
            for spell in spell_list
        ]

    return spells
