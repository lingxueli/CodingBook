# docstring: '''...''' in the beginning of the function definition
def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)

test('!!!')

# read docstring
help(test)
print(test.__doc__)
