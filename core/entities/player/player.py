from core.entities.base.character import Character
from ui.colors import Bcolors


class Player(Character):
    def choose_action(self):
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Actions:" + Bcolors.ENDC)
        for i, action in enumerate(["Attack", "Magic"], 1):
            print(f"  {i}. {action}")

    def choose_spell(self):
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Spells:" + Bcolors.ENDC)
        for i, spell in enumerate(self.magic, 1):
            print(f"  {i}. {spell.name} (cost: {spell.cost})")
