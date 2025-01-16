from dataclasses import dataclass, field

@dataclass
class Item:
    """
    Representa un ítem genérico en el juego.
    """
    id: int
    name: str
    type: str
    description: str
    prop: float = field(default=0.0)

    def __post_init__(self):
        """
        Realiza validaciones después de la inicialización automática de la dataclass.
        """
        self.validate_id(self.id)
        self.validate_name(self.name)
        self.validate_type(self.type)
        self.validate_description(self.description)
        self.validate_prop(self.prop)

    @staticmethod
    def validate_id(value: int):
        """Valida el atributo `id`."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El ID debe ser un entero positivo.")

    @staticmethod
    def validate_name(value: str):
        """Valida el atributo `name`."""
        if not value:
            raise ValueError("El nombre no puede estar vacío.")

    @staticmethod
    def validate_type(value: str):
        """Valida el atributo `type`."""
        if not value:
            raise ValueError("El tipo no puede estar vacío.")

    @staticmethod
    def validate_description(value: str):
        """Valida el atributo `description`."""
        if not value:
            raise ValueError("La descripción no puede estar vacía.")

    @staticmethod
    def validate_prop(value: float):
        """Valida el atributo `prop`."""
        if value < 0:
            raise ValueError("La propiedad no puede ser negativa.")

    @property
    def prop(self) -> float:
        """Getter para el atributo `prop`."""
        return self._prop

    @prop.setter
    def prop(self, value: float):
        """Setter para validar y asignar `prop`."""
        self.validate_prop(value)
        self._prop = value

    def use(self):
        """
        Método genérico para usar un ítem. Puede ser sobrescrito por clases derivadas.
        """
        print(f"Usaste el ítem '{self.name}' con un efecto de {self.prop}.")
