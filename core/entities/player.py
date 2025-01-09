from core.entities.character import Character

class Player(Character):
    def choose_action(self):
        print("\nActions:")
        for i, action in enumerate(["Attack", "Magic"], 1):
            print(f"  {i}. {action}")

    def choose_spell(self):
        print("\nSpells:")
        for i, spell in enumerate(self.magic, 1):
            print(f"  {i}. {spell.name} (cost: {spell.cost})")
