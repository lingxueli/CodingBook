import re

# code generator on regex101.com
# quick reference on regex101.com

# raw string: r"[a]". ignore the sepcial meaning interpreted by python interpreter

string = 'search this inside this string please'

# pattern as an object
pattern = re.compile(r"([a-zA-Z]).([a])")

a = pattern.search(string)
print(a.group()) # sea
print(a.group(1)) # ([a-zA-Z]): s
print(a.group(2)) # ([a]): a