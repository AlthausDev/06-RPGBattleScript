from core.data.loader import load_spells
from core.entities.enemy import Enemy
from core.entities.player import Player
from core.mechanics.combat import battle_round
from ui.messages import combat_start_message, display_victory_message, display_defeat_message

spells = load_spells("assets/data/magic.json")

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
