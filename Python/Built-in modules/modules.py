# python module index
# before we write any code, check if there's module doing the heavy lifting

# built in module: it's installed with python
# you'll import it when use it

# packages from 3rd party developers: PyPI Python Package Index
# pip install
import random
print(random) # module random from PATH: Python\\Python39\\lib\\random.py


help(random) # documentation
print(dir(random)) # all the attributes/methods in teh modules

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)