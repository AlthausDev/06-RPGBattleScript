from typing import List

from core.entities.items.item import Item
from core.entities.items.throwable import Throwable


class Inventory:
    def __init__(self):
        self.items: List[Item] = []


    def add_item(self, item: Item):

        if not isinstance(item, Item):
            raise ValueError("Solo se pueden agregar instancias de Item al inventario.")
        self.items.append(item)