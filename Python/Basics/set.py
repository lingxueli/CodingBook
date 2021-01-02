my_set = {1,2,3,4,5,5}

# set only contains unique values
print(my_set) # {1,2,3,4,5}

# add()
my_set.add(100)
my_set.add(2)

print(my_set)

# set()
my_list=[1,2,3,4,5,5]
print(set(my_list))

# doesn't support indexing
# my_set[0] won't work

# in
print(1 in my_set)

# list()
print(list(my_set))

# copy() clear()
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

# set methods
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# difference()
print(my_set.difference(your_set)) # {1,2,3}

# discard()
print(my_set.discard(5)) # None
print(my_set) # 5 is removed from my_set

# difference_update()
# remove the overlap
print(my_set.difference_update(your_set)) #None
print(my_set) # {1,2,3} 

my_set = {1,2,3,4,5}

# intersection()
print(my_set.intersection(your_set)) #{4,5}

# &
# same as intersection()
print(my_set & your_set)

# isdisjoint()
# do they have nothing in common?
print(my_set.isdisjoint(your_set)) # False

# union()
print(my_set.union(your_set)) #{1,2,3,4,5,6,7,8,9,10}

# |
# same as union() 
print(my_set | your_set)

my_set = {4,5}
# issubset()
print(my_set.issubset(your_set)) #true

# issuperset()
print(your_set.issuperset(your_set)) # true
