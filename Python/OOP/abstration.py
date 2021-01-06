# OOP
class PlayerCharacter:
    # class object attribute
    membership = True

    # dunder method is python built-in method
    # __method__ is the naming convention.
    # don't overwrite the dunder method
    def __init__(self,name,age):
        self._name = name #attribute
        self._age = age
        
        # there's no true private variables        
        # _name is the naming convention for private variable

    def run(self): #method
        print('run')

player1 = PlayerCharacter('andy', 100)
player1.run = "Boo"
 # the run() method is overwritten by the definition
 # overwritting breaks the class definition
 # use _name convention as a warning

print(player1.run)