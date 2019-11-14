from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 160},
         {"name": "Thunder", "cost": 40, "dmg": 220},
         {"name": "Blizzard", "cost": 30, "dmg": 190},
         {"name": "Ice", "cost": 10, "dmg": 160},
         {"name": "Cure", "cost": 20, "dmg": -200}]

player = Person(60, 450, 50, 40, magic)
enemy = Person(40, 1200, 30, 25, magic)

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "ENEMY ATTACKING!!" + Bcolors.ENDC)

while running:
    print("=============================================")
    player.ActionChoice()
    choice = input("Choose Action FAST Warrior!! :")
    index = int(choice) - 1

    if index == 0:
        dmg = player.GenerateDmg()
        enemy.TakeDmg(dmg)
        print("U attacked for", dmg, "points of Damage.")

    elif index == 1:
        player.SpellChoice()
        magic_choice = int(input("Choose Magic:"))
        magic_dmg = player.GenerateMagicDmg(magic_choice)

        spell = player.SpellName(magic_choice)

        cost = player.GetMpSpellCost(magic_choice)
        current_mp = player.GetMP()
        if cost > current_mp:
            print(Bcolors.FAIL, "\n Not Enough MP\n", Bcolors.ENDC)
            continue
        player.ReduceMP(cost)
        enemy.TakeDmg(magic_dmg)
        print(Bcolors.OKBLUE, "\n", spell ,"Deals", str(magic_dmg), "Points of Damage", Bcolors.ENDC)

    enemy_choice = 1
    enemy_damage = enemy.GenerateDmg()
    playerDmged = player.TakeDmg(enemy_damage)
    print("enemy attacks for:", enemy_damage)
    print("---------------------------------------")
    print("Enemy HP:", Bcolors.FAIL, str(enemy.GetHP()), "/", str(enemy.GetMaxHP()), Bcolors.ENDC, "\n")
    print("Ur HP:", Bcolors.OKGREEN, str(player.GetHP()), "/", str(player.GetMaxHP()),Bcolors.ENDC, "\n")
    print("Ur MP:", Bcolors.OKBLUE, str(player.GetMP()), "/", str(player.GetMaxMP()),Bcolors.ENDC, "\n")
    # playerDmged we can use that instead of player.GetHP() also.

    if enemy.GetHP() == 0:
        print(Bcolors.OKGREEN,"U Win!", Bcolors.ENDC)
        running = False
    elif player.GetHP() == 0:
        print(Bcolors.FAIL, "Enemy defeated u", Bcolors.ENDC)
        running = False