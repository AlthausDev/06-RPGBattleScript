import os
from core.data.load_game_data import load_game_data
from core.entities.enemy.enemy import Enemy
from core.entities.player.player import Player
from core.mechanics.combat import battle_round
from ui.messages import combat_start_message, display_victory_message, display_defeat_message


def load_game_assets():
    """
    Carga los datos del juego, como hechizos e ítems.
    """
    # Definir rutas de los archivos
    spells_path = os.path.join("assets", "data", "spells.json")
    items_path = os.path.join("assets", "data", "items.json")

    # Cargar datos del juego
    return load_game_data(spells_path, items_path)


def display_available_data(game_data):
    """
    Muestra información sobre los hechizos e ítems disponibles.
    """
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
        print(
            f"- {throwable.name} ({throwable.throwable_type.value}, "
            f"Subtipo: {throwable.throwable_subtype.value if throwable.throwable_subtype else 'Ninguno'})"
        )

def configure_characters(game_data):
    """
    Configura al jugador y al enemigo con hechizos y atributos predeterminados.

    Returns:
        tuple: Instancias de Player y Enemy configuradas.
    """
    spells = game_data["spells"]

    # Configurar los hechizos del jugador y el enemigo
    player_spells = spells.get("fire_spells", []) + spells.get("healing_spells", [])
    enemy_spells = spells.get("ice_spells", [])

    if not player_spells or not enemy_spells:
        raise ValueError("No se pudieron cargar los hechizos necesarios para los personajes.")

    # Crear instancias de Player y Enemy
    player = Player(name="Hero", hp=26, mp=65, atk=6, defense=3, magic_defense=2, magic=player_spells)
    enemy = Enemy(name="Goblin", hp=38, mp=20, atk=5, defense=3, magic_defense=2, magic=enemy_spells)

    return player, enemy

def game_loop(player, enemy):
    """
    Ciclo principal del juego. Controla el combate entre el jugador y el enemigo.
    """
    running = True

    while running:
        battle_round(player, enemy)

        if player.hp <= 0:
            display_defeat_message(player.name)
            running = False
        elif enemy.hp <= 0:
            display_victory_message(enemy.name)
            running = False


def main():
    """
    Punto de entrada principal del juego.
    """
    # Cargar datos del juego
    game_data = load_game_assets()

    # Mostrar datos disponibles
    display_available_data(game_data)

    # Configurar personajes
    player, enemy = configure_characters(game_data)

    # Inicio del combate
    combat_start_message(enemy.name)
    game_loop(player, enemy)


if __name__ == "__main__":
    main()
