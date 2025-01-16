from core.data.load_items import load_items
from core.data.load_spells import load_spells


def load_game_data(spells_path: str, items_path: str):
    """
    Carga hechizos e ítems desde archivos JSON separados.

    Args:
        spells_path (str): Ruta al archivo JSON de hechizos.
        items_path (str): Ruta al archivo JSON de ítems.

    Returns:
        dict: Un diccionario con los datos del juego (hechizos e ítems).
    """
    return {
        "spells": load_spells(spells_path),
        "items": load_items(items_path),
    }
