from dataclasses import dataclass

@dataclass
class Spell:
    """
    Representa un hechizo en el juego.
    """
    id: int
    name: str
    cost: int
    dmg: int = 0
    heal: int = 0

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        if not self.name:
            raise ValueError("El nombre no puede estar vacío.")
        if self.cost < 0:
            raise ValueError("El coste no puede ser negativo.")
        if self.dmg < 0:
            raise ValueError("El daño no puede ser negativo.")
        if self.heal < 0:
            raise ValueError("La curación no puede ser negativa.")
