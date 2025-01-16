from dataclasses import dataclass, asdict, field
from typing import Optional
from enum import Enum
from core.entities.items.item import Item

class ThrowableType(Enum):
    """
    Tipos principales de objetos arrojadizos.
    """
    KNIFE = "knife"
    GRENADE = "grenade"

class ThrowableSubtype(Enum):
    """
    Subtipos de objetos arrojadizos.
    """
    THROWING_KNIFE = "throwing_knife"
    DAGGER = "dagger"
    POISONED_KNIFE = "poisoned_knife"
    FRAG_GRENADE = "frag_grenade"
    SMOKE_GRENADE = "smoke_grenade"
    FLASH_GRENADE = "flash_grenade"

@dataclass
class Throwable(Item):
    """
    Representa un objeto arrojadizo en el juego. Hereda de Item.
    """
    throwable_type: ThrowableType = ThrowableType.KNIFE
    throwable_subtype: Optional[ThrowableSubtype] = None

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.throwable_type, ThrowableType):
            raise ValueError("El tipo de objeto debe ser una instancia de ThrowableType.")
        if self.throwable_subtype is not None and not isinstance(self.throwable_subtype, ThrowableSubtype):
            raise ValueError("El subtipo debe ser una instancia de ThrowableSubtype.")

        self.validate_subtype()

    def validate_subtype(self):
        """Valida que el subtipo corresponda al tipo principal."""
        if self.throwable_type == ThrowableType.KNIFE:
            valid_subtypes = {ThrowableSubtype.THROWING_KNIFE, ThrowableSubtype.DAGGER, ThrowableSubtype.POISONED_KNIFE}
        elif self.throwable_type == ThrowableType.GRENADE:
            valid_subtypes = {ThrowableSubtype.FRAG_GRENADE, ThrowableSubtype.SMOKE_GRENADE,
                              ThrowableSubtype.FLASH_GRENADE}
        else:
            valid_subtypes = set()

        if self.throwable_subtype and self.throwable_subtype not in valid_subtypes:
            raise ValueError(f"El subtipo {self.throwable_subtype} no es válido para el tipo {self.throwable_type}.")

    def use(self):
        """
        Comportamiento específico al usar el objeto.
        """
        if self.throwable_subtype:
            print(f"Usaste {self.name}, un {self.throwable_type.value} del tipo {self.throwable_subtype.value}.")
        else:
            print(f"Usaste {self.name}, un {self.throwable_type.value} sin subtipo específico.")

    def to_dict(self):
        """
        Convierte la instancia a un diccionario, serializando enums como cadenas.
        """
        data = asdict(self)
        data["throwable_type"] = self.throwable_type.value
        if self.throwable_subtype:
            data["subtype"] = self.throwable_subtype.value
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Throwable desde un diccionario.
        """
        data["throwable_type"] = ThrowableType(data["throwable_type"])
        if "subtype" in data and data["subtype"]:
            data["subtype"] = ThrowableSubtype(data["subtype"])
        return cls(**data)
