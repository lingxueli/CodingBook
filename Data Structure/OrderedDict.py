#how to iterate from end to beginning over an OrderedDict ?

#Either:

z = OrderedDict( ... )
for item in z.items()[::-1]:
   # operate on item
#Or:

z = OrderedDict( ... )
for item in reversed(z.items()):
   # operate on item
