my_tuple = (1,2,3,4,5)

# tuple is the immutable version of list
# my_tuple[1] = 'z'
# it won't work

print(my_tuple[1])

print(5 in my_tuple)

# you cannot sort, reverse the list
# tuple is faster than list

# dictionary items()
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
    }

print(user.items()) # items() returns dict_items which contains tuples

# tuple could be the key of dictionary because it's immutable
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20,
    (1,2): [1,2,3]
    }
print(user[(1,2)])

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]

print(new_tuple) # (2,) tuple with single item has an extra ,

new_tuple = my_tuple[1:4]
print(new_tuple) # (2,3,4,5)


# unpacking
x,y,z, *other = (1,2,3,4,5)

print(z)
print(other)

# count()
print(my_tuple.count(5)) # 1, return the # of 5s in tuple

# index()
print(my_tuple.index(4)) # return 3, the index of value 4
