# list
li = [1,2,3]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

# list slicing
# similar to string slicing
string = 'hellooo'
print(string[0:2:1])

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0::2])

# modify the list
amazon_cart[0] = 'laptop'
new_cart = amazon_cart # they point to the same memory
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart) # the two statements print out the same list

# copy the list
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] # make a copy, assign it to the new one
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart) # the two statements print out different lists
