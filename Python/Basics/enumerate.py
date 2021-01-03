# enumerate takes an iterable objects, it returns an index counter and the item
for i, char in enumerate('hello'):
    print(i, char)
    if char == 'e':
        print(f'index of e is: {i}')
