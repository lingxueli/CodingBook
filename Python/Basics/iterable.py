#iterable = list, dictionary, tuple, set, string

user = {
    'name': 'Golden',
    'age': 1,
    'can_swim': True }

for item in user.items():
    print(item)
    # tuple unpack
    key, value = item
    print(key, value)
    
# alternatives
for key, value in user.items():
    print(key, value)
    
for item in user.values():
    print(item)

for item in user.keys():
    print(item)
