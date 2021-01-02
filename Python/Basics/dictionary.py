dictionary = {
    'a' : [1,2,3],
    'b' : 'hello',
    'c' : True
    }

print(dictionary['a'][1])

# valid data type of keys: immutable data types
dictionary = {
    True : 'hello',
    123 : [1,2,3]
    # [100] : True # invalid
}

print(dictionary[True])
print(dictionary[123])

# avoid key error
user = {'basket': [1,2,3],
        'greet': 'hello'}

# print(user['age']) # key error

print(user.get('age')) # no key error, return None
print(user.get('age', 55)) # return default value if key doesn't exist

# another way to create dictionary
user2 = dict(name='John')
print(user2)

# in
print('i' in ['i'])
print('i' in 'hi')
print('basket' in user)
print('size' in user)

# keys(), values(), items()
print('basket' in user.keys())
print('hello' in user.values())
print(user.items())

# copy(), clear()
user2 = user.copy()
print(user2)

user.clear()
print(user)
print(user2)

user = {'basket': [1,2,3],
        'greet': 'hello'}

# pop()
print(user.pop('greet')) # pop() removes the value, returns 'hello'
print(user) # key: greet doesn't exist anymore

# popitem()
print(user.popitem()) # the last item on the dictionary gets removed
# because dict is unordered, it removed the random item

user = {'basket': [1,2,3],
        'greet': 'hello'}

# update()
print(user.update({'age': 55}))
print(user)
