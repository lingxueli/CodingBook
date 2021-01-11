# generator has much better performance then list
# it takes a lot less memory

from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        time1 = time()
        fn(*args, *kwargs)
        time2 = time()
        print(time2 - time1)
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10000000):
        i * 5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i * 5

long_time()
long_time2()