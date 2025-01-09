import random

from core.entities.character import Character

class Enemy(Character):
    def choose_action(self):
        return random.choice(["Attack", "Magic"])
