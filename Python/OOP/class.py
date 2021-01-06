# OOP
class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self,name,age):
        self.name = name #attribute
        self.age = age
    
    def shout(self): #method
        print(f'My name is {self.name}')

    # class method, first argument is the class.
    # so that you can instantiate the class inside the method
    # it cares about the status/attribute of the class
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy',  num1 + num2)

    # static class method, no argument for the class.
    # you cannot instantiate the class inside the method
    # it doesn't care about the status/attribute of the class
    @staticmethod
    def adding_things_static(num1, num2):
        return num1 + num2

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)