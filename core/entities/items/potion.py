import json
from enum import Enum
from dataclasses import dataclass, asdict, field
from core.entities.items.item import Item

class PotionType(Enum):
    """
    Tipos de pociones disponibles en el juego.
    """
    HEALING = "healing"
    MANA = "mana"
    DAMAGE = "damage"

@dataclass
class Potion(Item):
    """
    Representa una poción en el juego. Hereda de Item.
    """
    potion_type: PotionType = PotionType.HEALING

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.potion_type, PotionType):
            raise ValueError("El tipo de poción debe ser una instancia de PotionType.")

    def use(self):
        effect = (
            f"cura {self.prop} puntos de vida"
            if self.potion_type == PotionType.HEALING
            else f"recupera {self.prop} puntos de maná"
            if self.potion_type == PotionType.MANA
            else f"causa {self.prop} puntos de daño"
        )
        print(f"Usaste la poción '{self.name}'. Esta {effect}.")

    def to_dict(self):
        """
        Convierte la poción a un diccionario, serializando enums como cadenas.
        """
        data = asdict(self)
        data["potion_type"] = self.potion_type.value
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Potion desde un diccionario.
        """
        data["potion_type"] = PotionType(data["potion_type"])
        return cls(**data)
