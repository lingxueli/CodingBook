# super()

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing")

class Wizard(User):
    def __init__(self, name, power, email):

        # inherite the attribute
        # User. is legitimate, because User is an argument passed in to the class
        User.__init__(self, email)

        # another way to inherit the attribute
        # super() refers to the parent class
        super().__init__(email)

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

wizard1 = Wizard("Merlin", 50, "Merlin@gmail.com")

print(wizard1.sign_in()) # sign_in is inherited from the parent classe
# print(wizard1.email) # email is not inherited from the parent class
# because Wizard has its own __init__ method