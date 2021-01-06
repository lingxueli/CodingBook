# polymorphism

class User(object):
    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attaching with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        User.attack(self)
        print(f'attacking with arrors: arrows left {self.num_arrows}')


def player_attack(char):
    char.attack()

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(wizard1.sign_in())

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()