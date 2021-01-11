# what's under the hood when you use for i in range(100)

def special_for(iterable):
    iterator = iter(iterable) # iter() gets an iterator from an object
    while True:
        try:
            print(iterator) # list_iterator object
            print(next(iterator)) # 1, 2, 3
        except StopIteration:
            break

special_for([1,2,3])