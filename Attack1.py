import random

class Enemy:
    hp = 200


    def __init__(self,attl,atth):
        self.attl = attl
        self.atth = atth


    def GetAtk(self):
        print("Enemy Attack Is",self.attl)

    def GetHp(self):
        print("Enemy HP is",self.hp)


enemy1 = Enemy(40,50)
enemy1.GetAtk()
enemy1.GetHp()

enemy2 = Enemy(75,80)
enemy2.GetAtk()
enemy2.GetHp()
'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("enemy strikes",dmg,"damage","and ur health is",playerhp)

    if playerhp > 30:
        continue

    print("U low on health u have been teleported")
    break
'''