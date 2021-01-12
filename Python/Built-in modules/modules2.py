import sys
print(sys)

print(sys.argv) # access arguments from command line
# python3 modules2.py 1 2

filename = sys.argv[0] # filename: modules2.py
first_arg = sys.argv[1] # 1
second_arg = sys.argv[2] # 2

print(filename)
print(first_arg)
print(second_arg)