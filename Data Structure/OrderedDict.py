#how to iterate from end to beginning over an OrderedDict ?

#Either:

z = OrderedDict( ... )
for item in z.items()[::-1]:
   # operate on item
#Or:

z = OrderedDict( ... )
for item in reversed(z.items()):
   # operate on item

# delete an item

del dct[key]

# dict.pop and dict.popitem are used to remove an item and return the removed item so that it can be saved for later. If you do not need to save it however, then using these methods is less efficient


# modify key, value in iteration

# The values, for example, can be modified whenever you need, but you’ll need to use the original dictionary and the key that maps the value you want to modify:

>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for k, v in prices.items():
...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
...
>>> prices
{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}

# On the other hand, the keys can be added or removed from a dictionary by converting the view returned by .keys() into a list object:

>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in list(prices.keys()):  # Use a list instead of a view
...     if key == 'orange':
...         del prices[key]  # Delete a key from prices
...
>>> prices
{'apple': 0.4, 'banana': 0.25}

# Finally, if you try to remove a key from prices by using .keys() directly, then Python will raise a RuntimeError telling you that the dictionary’s size has changed during iteration:

>>> # Python 3. dict.keys() returns a view object, not a list
>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for key in prices.keys():
...     if key == 'orange':
...         del prices[key]
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for key in prices.keys():
RuntimeError: dictionary changed size during iteration

