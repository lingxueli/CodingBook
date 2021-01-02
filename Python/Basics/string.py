# escape sequence

weather = '\t It\'s sunny. \nCool!'
# treat what's after \ as a normal string
# \t = tab, it is a special squence
# \n = new line

print(weather)

# formatted strings
name = 'Johnny'
age = 20

# this works in python 3 only
print(f'hi {name}. You are {age} years old')
# f: f string, i.e. formatted string
# {}: variable

# this works in both python 2 and 3
print('hi {}. You are {} years old'.format(name, age))
# specify an order
print('hi {1}. You are {0} years old'.format(name, age))
# specify the order
print('hi {name}. You are {age} years old'.format(name='sally', age=21))


# string indexing/slicing
# [start:stop:stepover]
test = '01234567'
print(test[0:8:2])

print(test[1:])

print(test[:5])

print(test[::1])

print(test[::-1])

print(test[0:8:-1])

print(test[0:8:-2])

print(test[::-2])

print(test[-1])

print(test[-2])

# string is immutable
# test[1] = '8' won't work
# test = test + '8' will work because it creates a new string


