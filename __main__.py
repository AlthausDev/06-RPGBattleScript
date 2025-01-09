from core.entities.enemy import Enemy
from core.entities.player import Player
from core.mechanics.combat import battle_round
from ui.colors import Bcolors
from ui.messages import combat_start_message, display_victory_message, display_defeat_message
from core.mechanics.spells import magic

def main():
    # Configurar personajes
    player = Player("Hero", 260, 65, 60, 34, magic)
    enemy = Enemy("Goblin", 380, 20, 40, 35, magic)

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