import os

print('getcwd: ', os.getcwd())
print('__file__', __file__)

# getcwd:  C:\Users\lingx\OneDrive\Documents\CodingBook\Python
# __file__ C:/Users/lingx/OneDrive/Documents/CodingBook/Python/file_path.py

print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))

# basename:     file_path.py
# dirname:      C:/Users/lingx/OneDrive/Documents/CodingBook/Python

print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))

# abspath:      C:\Users\lingx\OneDrive\Documents\CodingBook\Python\file_path.py
# abs dirname:  C:\Users\lingx\OneDrive\Documents\CodingBook\Python

print('[set target path 1]')
target_path_1 = os.path.join(os.path.dirname(__file__), 'target_1.txt')

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())

# [set target path 1]
# target_path_1:  C:/Users/lingx/OneDrive/Documents/CodingBook/Python\target_1.txt
# read target file:
# test

# The upper directory is represented by ../
print('[set target path 2]')
target_path_2 = os.path.join(os.path.dirname(__file__), '../dst/target_2.txt')

print('target_path_2: ', target_path_2)
print('normalize    : ', os.path.normpath(target_path_2))

print('read target file:')
with open(target_path_2) as f:
    print(f.read())

# target_path_2:  C:/Users/lingx/OneDrive/Documents/CodingBook/Python\../dst/target_2.txt
# normalize    :  C:\Users\lingx\OneDrive\Documents\CodingBook\dst\target_2.txt
# read target file:
# test2

print('[change directory]')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('getcwd:      ', os.getcwd())

# [change directory]
# getcwd:       C:\Users\lingx\OneDrive\Documents\CodingBook\Python

print('[set target path 1 (after chdir)]')
target_path_1 = 'target_1.txt'

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())

print()
print('[set target path 2 (after chdir)]')
target_path_2 = '../dst/target_2.txt'

print('target_path_2: ', target_path_2)

print('read target file:')
with open(target_path_2) as f:
    print(f.read())

##[set target path 1 (after chdir)]
##target_path_1:  target_1.txt
##read target file:
##test
##
##[set target path 2 (after chdir)]
##target_path_2:  ../dst/target_2.txt
##read target file:
##test2
