import re

string = 'search this inside this string please'
a = re.search('this', string) # match object

print(a.span()) # index range
print(a.start())
print(a.end())

print(a.group()) # this

a = re.search('This', string) # None

# pattern as an object
pattern = re.compile('this')

a = pattern.search(string) 
# match object with span = [7,11]
b = pattern.findall(string) 
# [this, this]
c = pattern.fullmatch(string) 
# exact match pattern == string
# none
d = pattern.match(string) 
# match with pattern from the beginning of the string
# none

print(a)
print(b)
print(c)
print(d)