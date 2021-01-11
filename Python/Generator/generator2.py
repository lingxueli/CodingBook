# generator is an subset of iterable
# generator is function
# held one item at a time
def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(5)
print(next(g)) # 0
print(next(g)) # 2
print(next(g)) # 4
print(next(g)) # 6
# print(next(g)) # 8
# then StopIteration