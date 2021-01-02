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


# adding
basket = [1,2,3,4,5]
new_list= basket.append(1000) # append: modify the list in place
print(basket)
print(new_list) # None


new_list = basket.insert(5,100) # insert: modify the list in place
print(basket)
print(new_list) # None


new_list = basket.extend([100,101]) # extend: modify the list in place
print(basket)
print(new_list) # None

# removing
basket.pop() # pop from the end of the list
print(basket)

basket.pop(0) # pop from an index
print(basket)

new_list = basket.remove(4) # remove the value 4
print(new_list) # remove: modify the list in place

new_list = basket.pop(4) # pop: popped item is returned
print(new_list) # new_list = popped item

new_list = basket.clear()
print(new_list) # None
print(basket) # []

# read
basket = ['a','x','b','c','d','e','d']
print(basket.index('d'))

print(basket.index('d',0,6))

print('a' in basket)

print('f' in basket)

print(basket.count('d'))

# more list methods

# list methond sort(): sort the list in place 
basket.sort()
print(basket) # sorted 

basket = ['a','x','b','c','d','e','d']

# built-in function sorted(): make a sorted copy of the original list
print(sorted(basket)) # sorted
print(basket) # not sorted

# this has the same effect as sorted()
new_basket = basket[:]
new_basket.sort()
print(new_basket) # sorted
print(basket) # not sorted

# list method copy()
new_basket = basket.copy()
new_basket.sort()
print(new_basket) # sorted
print(basket) # not sorted

# list method reverse()
basket.reverse() # not sorting, it reserves the indexes
print(basket)

# range -> list
print(list(range(1,101)))
print(list(range(101)))

# join
sentence = " "
new_sentence = sentence.join(['hi','nice','to','meet','you'])
print(sentence)
print(new_sentence)

# list unpacking
basket = [1,2,3]
a, b, c  = [1,2,3]
print(a)
print(b)
print(c)

a,b,c,*other = [1,2,3,4,5,6,7,8,9]
print(other)

a,b,c,*other,d = [1,2,3,4,5,6,7,8,9]
print(other)
print(d)
