# error as an object
def sum_err(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')

print(sum_err(1,'2'))

# handling multiple error at the same time
def divide_err(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)

print(divide_err(1,'2'))
print(divide_err(1,0))