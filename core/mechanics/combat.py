import random
from ui.colors import Bcolors


def battle_round(player, enemy):
    print("=================")
    print("Inicio de la ronda de batalla\n")

    # Aplicar efectos de estado
    player.apply_status_effects()
    enemy.apply_status_effects()

    # Turno del jugador
    print(f"\n{player.name}, elige tu acción:")
    player.choose_action()
    try:
        choice = int(input("\nElige acción: ")) - 1
    except ValueError:
        print("\n¡Elección inválida! Perdiste tu turno.")
        choice = -1

    match choice:
        case 0:  # Ataque físico
            dmg = player.generate_damage()
            effective_dmg = enemy.take_damage(dmg, "physical")
            print(f"\n{player.name} atacó causando {effective_dmg} puntos de daño.")

        case 1:  # Hechizo
            if not player.magic:
                print("\nNo tienes hechizos disponibles.")
                return

            print(f"\n{player.name}, elige un hechizo:")
            player.choose_spell()
            try:
                spell_choice = int(input("\nElige hechizo: ")) - 1
                if spell_choice < 0 or spell_choice >= len(player.magic):
                    raise ValueError
            except ValueError:
                print("\n¡Elección de hechizo inválida!")
                return

            spell = player.magic[spell_choice]

            if player.mp < spell.cost:
                print("\nNo tienes suficiente MP para lanzar ese hechizo.")
                return

            if spell.dmg > 0:  # Hechizo de daño
                spell_damage = player.generate_spell_damage(spell_choice)
                effective_dmg = enemy.take_damage(spell_damage, "magic")
                print(
                    f"\n{player.name} lanzó {spell.name} causando {effective_dmg} puntos de daño. "
                    f"HP del enemigo: {enemy.hp}\nMP restante: {player.mp}"
                )

            elif spell.heal > 0:  # Hechizo de curación
                healing = random.randint(spell.heal - 2, spell.heal + 2)
                player.hp += healing
                player.reduce_mp(spell.cost)
                print(
                    f"\n{player.name} lanzó {spell.name} y recuperó {healing} puntos de HP. "
                    f"Tu HP: {player.hp}\nMP restante: {player.mp}"
                )

        case _:
            print("\nElección inválida, pierdes tu turno.")

    # Turno del enemigo
    print("\nTurno del enemigo:")
    enemy_dmg = enemy.generate_damage()
    effective_dmg = player.take_damage(enemy_dmg, "physical")
    print(f"{enemy.name} atacó causando {effective_dmg} puntos de daño.")

    # Mostrar estadísticas actuales
    print("\n=== Estadísticas ===")
    print(f"{enemy.name} HP: " + Bcolors.FAIL + f"{enemy.hp}" + Bcolors.ENDC)
    print(f"{player.name} HP: " + Bcolors.OKGREEN + f"{player.hp}" + Bcolors.ENDC)
    print(f"{player.name} MP: " + Bcolors.OKBLUE + f"{player.mp}" + Bcolors.ENDC)
    print("=================\n")
