from utility import multiply, divide
from shopping.more_shopping import shopping_cart
# best practice
# import as specific as possible to avoid the conflict such as utility.max
# import only what we need
print(shopping_cart.buy('apple'))
print(divide(5,2))

print(__name__) # __main__
# __main__ is default module name given to the main file we run

if __name__ == '__main__':
    print('please run this')