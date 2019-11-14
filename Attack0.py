import random



playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg
    if playerhp <= 30:
        playerhp = 30

    print("enemy strikes",dmg,"damage","and ur health is",playerhp)

    if playerhp == 30:
        print("U low on health u have been teleported")
        break
