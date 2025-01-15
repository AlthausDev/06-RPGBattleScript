import random

from ui.colors import Bcolors


def battle_round(player, enemy):
    print("=================")
    player.apply_status_effects()
    enemy.apply_status_effects()

    player.choose_action()
    choice = int(input("\nChoose action: ")) - 1

    match choice:
        case 0:  # Attack
            dmg = player.generate_damage()
            effective_dmg = enemy.take_damage(dmg, "physical")
            print(f"\n{player.name} attacked for {effective_dmg} points.")

        case 1:  # Magic
            player.choose_spell()
            spell_choice = int(input("\nChoose spell: ")) - 1

            if spell_choice < 0 or spell_choice >= len(player.magic):
                print("\nInvalid spell choice!")
                return

            spell = player.magic[spell_choice]

            if player.mp < spell.cost:
                print("\nNot enough MP!")
                return

            if spell.dmg > 0:  # Hechizo de daño
                spell_damage = random.randint(spell.dmg - 2, spell.dmg + 2)
                effective_dmg = enemy.take_damage(spell_damage, "magic")
                player.reduce_mp(spell.cost)
                print(f"\n{player.name} cast {spell.name} for {effective_dmg} damage. Enemy HP: {enemy.hp}")
                print(f"Remaining MP: {player.mp}")

            elif spell.heal > 0:  # Hechizo de curación
                healing = random.randint(spell.heal - 2, spell.heal + 2)
                player.hp = min(player.max_hp, player.hp + healing)
                player.reduce_mp(spell.cost)
                print(f"\n{player.name} cast {spell.name} and healed for {healing} HP. Your HP: {player.hp}")
                print(f"Remaining MP: {player.mp}")

        case __:
            pass


    # Enemy action
    enemy_dmg = enemy.generate_damage()
    effective_dmg = player.take_damage(enemy_dmg, "physical")
    print(f"{enemy.name} attacks for {effective_dmg}.")

    print("\nEnemy HP: " + Bcolors.FAIL + Bcolors.BOLD + f"{enemy.hp}" + Bcolors.ENDC)
    print("\nYour HP: " + Bcolors.OKGREEN + Bcolors.BOLD + f"{player.hp}" + Bcolors.ENDC )
    print("Your MP: " + Bcolors.OKBLUE + Bcolors.BOLD + f"{player.mp}" + Bcolors.ENDC)

