import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
# missing time for spells, max mp , hp and mp regen which need max to compare

class Person:
    def __init__(self, mp, hp, atk, df, magic):
        self.maxmp = mp
        self.mp = mp
        self.maxhp = hp
        self.hp = hp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic Attack"]

    def GenerateDmg(self):
        return random.randrange(self.atkl ,self.atkh)

    def TakeDmg(self, dmg):
        self.hp -= dmg
        if self.hp <0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp> self.maxhp:
            self.hp = self.maxhp

    def GetHP(self):
        return self.hp

    def GetMaxHP(self):
        return self.maxhp

    def GetMP(self):
        return self.mp

    def GetMaxMP(self):
        return self.maxmp

    def ReduceMP(self, cost):
        self.mp -= cost

    def ActionChoice(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + 'Actions' + Bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def SpellChoice(self):
        i = 1
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Magic" + Bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell["name"],"(cost:",str(spell["cost"]),")" )
            i += 1






