from enum import Enum
from core.entities.items.item import Item

class PotionType(Enum):
    """
    Tipos de pociones disponibles en el juego.
    """
    HEALING = "healing"
    MANA = "mana"
    DAMAGE = "damage"

class Potion(Item):
    """
    Representa una poción en el juego. Hereda de Item.
    """
    def __init__(self, name: str, potion_type: PotionType, description: str, prop: float):
        """
        Constructor para Potion.
        """
        super().__init__(name=name, type="potion", description=description, prop=prop)
        self._potion_type = potion_type

    @property
    def potion_type(self) -> PotionType:
        """
        Getter para el tipo de poción.
        """
        return self._potion_type

    @potion_type.setter
    def potion_type(self, value: PotionType):
        """
        Setter para el tipo de poción con validación.
        """
        if not isinstance(value, PotionType):
            raise ValueError("El tipo de poción debe ser una instancia de PotionType.")
        self._potion_type = value

    def use(self):
        """
        Implementa el uso específico de una poción.
        """
        effect = (
            f"cura {self.prop} puntos de vida"
            if self.potion_type == PotionType.HEALING
            else f"recupera {self.prop} puntos de maná"
            if self.potion_type == PotionType.MANA
            else f"causa {self.prop} puntos de daño"
        )
        print(f"Usaste la poción '{self.name}'. Esta {effect}.")
