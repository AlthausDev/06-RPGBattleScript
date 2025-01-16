from core.data.load_game_data import load_game_data
from core.entities.base import spells
from core.entities.enemy.enemy import Enemy
from core.entities.player.player import Player
from core.mechanics.combat import battle_round
from ui.messages import combat_start_message, display_victory_message, display_defeat_message

# Cargar datos del juego
game_data = load_game_data("spells.json", "items.json")

# Acceder a hechizos
fire_spells = game_data["spells"].get("fire_spells", [])
print("Hechizos de fuego:")
for spell in fire_spells:
    print(f"- {spell.name} (Coste: {spell.cost}, Daño: {spell.dmg})")

# Acceder a ítems
potions = game_data["items"].get("potions", [])
print("\nPociones disponibles:")
for potion in potions:
    print(f"- {potion.name} (Efecto: {potion.potion_type.value}, Prop: {potion.prop})")

throwables = game_data["items"].get("throwables", [])
print("\nObjetos arrojadizos disponibles:")
for throwable in throwables:
    print(f"- {throwable.name} ({throwable.throwable_type.value}, Subtipo: {throwable.subtype.value if throwable.subtype else 'Ninguno'})")


def main():
    player_spells = spells["fire_spells"] + spells["healing_spells"]  # Combina categorías
    enemy_spells = spells["ice_spells"]

    # Configurar personajes
    player = Player("Hero", 26, 65, 6, 3, 2, player_spells)
    enemy = Enemy("Goblin", 38, 20, 5, 3, 2, enemy_spells)

    # Inicio del combate
    combat_start_message(enemy.name)
    game_loop(player, enemy)

def game_loop(player, enemy):
    running = True

    while running:
        battle_round(player, enemy)

        if player.hp <= 0:
            display_defeat_message(player.name)
            running = False
        elif enemy.hp <= 0:
            display_victory_message(enemy.name)
            running = False

if __name__ == "__main__":
    main()
