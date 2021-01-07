# *args, **kwargs

def super_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total

print(super_func(1,2,3,4,5,a=5,b=10))