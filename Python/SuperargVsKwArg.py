# *args **kwargs
# arbitrary # of argument / keyword argument
def super_func(*args, **kwargs):
    print(args)
    print(*args)
    
    print(kwargs)
    print(*kwargs)

    total = 0
    for item in kwargs.values():
        total += item
        
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

# Rule: params, *args, default parameters, **kwargs
def super_func(name, *args, i = 'hi', **kwargs):
    print(args)
    print(*args)
    
    print(kwargs)
    print(*kwargs)

    total = 0
    for item in kwargs.values():
        total += item
        
    return sum(args) + total

print(super_func('Andy', 1,2,3,4,5, num1 = 5, num2 = 10))

