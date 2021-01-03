# is vs ==

# == checks for equality

print(True == 1) # true
# convert 1 to bool(1)

print('' == 1) # false
# covert '' to bool

print('1' == 1) # false

print([] == 1) # false

print(10 == 10.0) # true

print([] == []) # true

a = [1,2,3]
b = [1,2,3]
print(a == b) # true
 
# is checkes if the locations in the memory are the same

print(True is True) # true
print('1' is '1') # ture
# int and bool are simple data types that are in memeroy but in one location

print([] is  []) # false
# two [] are created

print(10 is 10.0) # false

print([1,2,3] is [1,2,3]) # false
