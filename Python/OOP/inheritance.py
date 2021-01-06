# inheritance

class User:
    def sign_in(self):
        print('logged in')

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
        print(f'attacking with arrors: arrows left {self.num_arrows}')

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
print(wizard1.sign_in())

wizard1.attack()

# isinstance(object, class)

print(isinstance(wizard1, Wizard)) # True
print(isinstance(wizard1, User)) # True

# object is the base class for all python classes
print(isinstance(wizard1, object))