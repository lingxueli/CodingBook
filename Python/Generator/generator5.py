# create a generator

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # this allows MyGen.iter, creating an interator
    def __iter__(self):
        return self
    
    # this allows running MyGen.next
    def __next__(self):    
        if  MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)