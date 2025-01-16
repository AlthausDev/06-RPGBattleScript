import json

from core.entities.items.potion import Potion, PotionType
from core.entities.items.throwable import Throwable, ThrowableType, ThrowableSubtype


def load_items(file_path):
    """
    Carga ítems desde un archivo JSON y los organiza por categoría.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los datos de los ítems.

    Returns:
        dict: Un diccionario donde las claves son las categorías y los valores son listas de ítems.
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo '{file_path}' no se encontró.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error al parsear el JSON en '{file_path}': {e}")

    items = {}

    # Procesar pociones
    if "potions" in data:
        items["potions"] = [
            Potion(
                id=item.get("id", -1),
                name=item.get("name", "Desconocido"),
                type=item.get("type", "potion"),
                description=item.get("description", ""),
                prop=item.get("prop", 0.0),
                potion_type=PotionType(item.get("potion_type", "healing"))
            )
            for item in data["potions"]
        ]

    # Procesar objetos arrojadizos
    if "throwables" in data:
        items["throwables"] = [
            Throwable(
                id=item.get("id", -1),
                name=item.get("name", "Desconocido"),
                type=item.get("type", "throwable"),
                description=item.get("description", ""),
                prop=item.get("prop", 0.0),
                throwable_type=ThrowableType(item.get("throwable_type", "knife")),
                throwable_subtype=ThrowableSubtype(item["subtype"]) if "subtype" in item else None
            )
            for item in data["throwables"]
        ]

    return items
