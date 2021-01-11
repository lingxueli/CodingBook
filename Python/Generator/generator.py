# generate a sequence of value over time
# range(100000000)
# generator: create them one by one


# list(range(100000000)) 
# generate the whole list in memory
# it's not accessible until the work creating the whole list is done

# generator is an subset of iterable
# generator is function
# held one item at a time

# to create a generator, you will define a generator function like this
def generator_function(num):
    for i in range(num):
        yield i


for item in generator_function(1000):
    print(item)