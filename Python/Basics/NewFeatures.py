# what's new in python 3.8
# read summary

# walrus operator
# :=

a = 'helloooooooo'

if ((n := len(a)) > 10):
    # print(f"too long {len(a)} elements")
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1] # remove the last character
