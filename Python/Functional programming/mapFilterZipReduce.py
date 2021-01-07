# map, filter, zip and reduce

from functools import reduce

# map()
# map(action, iterable)

def multiply_by2(item):
    return item * 2

my_list = [1,2,3]

print(map(multiply_by2, my_list)) # map object

print(list(map(multiply_by2, my_list))) # [2,4,6]

print(my_list) # [1,2,3] 


# filter()
# filter(boolean_function, iterable)

def only_odd(item):
    return item % 2 != 0

print(filter(only_odd, my_list)) # filter object

print(list(filter(only_odd, my_list)))

print(my_list) # [1,2,3] 

# zip()
# zip(iterables)

your_list = (10,20,30)
their_list = [5,4,3]

print(list(zip(my_list, your_list, their_list)))
# [(1,10,5),(2,20,4),(3,30,3)]

# reduce()
# reduce(function, sequence[,initial])

def accumulator(a, b):
    print(a,b)
    return a + b

print(reduce(accumulator, my_list, 0)) # 0 + 1 + 2 + 3
print(reduce(accumulator, my_list, 10)) # 10 + 1 + 2 + 3