def battle_round(player, enemy):
    print("=================")
    player.choose_action()
    choice = int(input("Choose action: ")) - 1

    if choice == 0:  # Attack
        dmg = player.generate_damage()
        effective_dmg = enemy.take_damage(dmg)
        print(f"\n{player.name} attacked for {effective_dmg} points. Enemy HP: {enemy.hp}")
    elif choice == 1:  # Magic
        player.choose_spell()
        spell_choice = int(input("Choose spell: ")) - 1
        spell = player.magic[spell_choice]
        if player.mp >= spell["cost"]:
            player.reduce_mp(spell["cost"])
            effective_dmg = enemy.take_damage(spell["dmg"])
            print(f"\n{player.name} cast {spell['name']} for {effective_dmg} damage. Enemy HP: {enemy.hp}")
        else:
            print("\nNot enough MP!")

    # Acción del enemigo
    enemy_dmg = enemy.generate_damage()
    effective_dmg = player.take_damage(enemy_dmg)
    print(f"\n{enemy.name} attacks for {effective_dmg}. Your HP: {player.hp}")
