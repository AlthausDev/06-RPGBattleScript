from dataclasses import dataclass, field

@dataclass
class Item:
    """
    Representa un ítem genérico en el juego.
    """
    _name: str = field(default="")
    _type: str = field(default="")
    _description: str = field(default="")
    _prop: float = field(default=0.0, repr=False)  # Campo protegido, oculto en la representación oficial.

    def __post_init__(self):
        """
        Realiza validaciones después de la inicialización automática de la dataclass.
        """
        if not self._name:
            raise ValueError("El nombre no puede estar vacío.")
        if not self._type:
            raise ValueError("El tipo no puede estar vacío.")
        if not self._description:
            raise ValueError("La descripción no puede estar vacía.")
        if self._prop < 0:
            raise ValueError("La propiedad no puede ser negativa.")

    @property
    def name(self) -> str:
        """Getter para el atributo `name`."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter para validar y asignar `name`."""
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self._name = value

    @property
    def type(self) -> str:
        """Getter para el atributo `type`."""
        return self._type

    @type.setter
    def type(self, value: str):
        """Setter para validar y asignar `type`."""
        if not value:
            raise ValueError("El tipo no puede estar vacío.")
        self._type = value

    @property
    def description(self) -> str:
        """Getter para el atributo `description`."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Setter para validar y asignar `description`."""
        if not value:
            raise ValueError("La descripción no puede estar vacía.")
        self._description = value

    @property
    def prop(self) -> float:
        """Getter para el atributo `prop`."""
        return self._prop

    @prop.setter
    def prop(self, value: float):
        """Setter para validar y asignar `prop`."""
        if value < 0:
            raise ValueError("La propiedad no puede ser negativa.")
        self._prop = value

    def use(self):
        """
        Método genérico para usar un ítem. Puede ser sobrescrito por clases derivadas.
        """
        print(f"Usaste el ítem '{self.name}' con un efecto de {self.prop}.")

    def __repr__(self):
        """
        Representación oficial de la clase para propósitos de depuración.
        """
        return f"Item(name='{self.name}', type='{self.type}', description='{self.description}', prop={self.prop})"
