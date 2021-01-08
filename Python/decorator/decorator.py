def hello():
    print('helloooooo')

greet = hello()
print(greet) # hello

greet = hello
print(greet) # function object

del hello
# hello is the pointer to the function
# this deletes the pointer not the function itself

greet() # still executed


# @decorator
# def hello():
#    pass
# decorator add extra features to a function

# higher order function
# a function that accepts another function as a parameter
def greet(func):
    func

# a function that returns another function
def greet2():
    def func():
        return 5
    return func

# example: map, reduce, filter

# wrap another funciton, enhance it
def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print("hello")

@my_decorator
def bye():
    print("see ya")

hello()
bye()

# this has the same effect
def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

def hello():
    print("hello")

def bye():
    print("see ya")


hello2 = my_decorator(hello) # pointer to wrap_func, where func == hello
hello2() # call wrap_func

# alternative
my_decorator(hello)()
