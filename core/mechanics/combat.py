def battle_round(player, enemy):
    print("=================")
    player.apply_status_effects()
    enemy.apply_status_effects()

    player.choose_action()
    choice = int(input("Choose action: ")) - 1

    if choice == 0:  # Attack
        dmg = player.generate_damage()
        effective_dmg = enemy.take_damage(dmg, "physical")
        print(f"\n{player.name} attacked for {effective_dmg} points. Enemy HP: {enemy.hp}")

    elif choice == 1:  # Magic
        player.choose_spell()
        spell_choice = int(input("Choose spell: ")) - 1

        if spell_choice < 0 or spell_choice >= len(player.magic):
            print("\nInvalid spell choice!")
            return

        spell_damage = player.generate_spell_damage(spell_choice)
        if spell_damage is None:
            return  # No hay suficiente MP, se sale de la función

        spell = player.magic[spell_choice]
        effective_dmg = enemy.take_damage(spell_damage, "magic")
        print(f"\n{player.name} cast {spell.name} for {effective_dmg} damage. Enemy HP: {enemy.hp}. Enemy MP: {enemy.mp}")

    # Acción del enemigo
    enemy_dmg = enemy.generate_damage()
    effective_dmg = player.take_damage(enemy_dmg, "physical")
    print(f"\n{enemy.name} attacks for {effective_dmg}. Your HP: {player.hp}. Your MP: {player.mp}")
