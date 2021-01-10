# python built in error
while True:
    try:
        age = int(input('what s your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
    # no thing failed
        print('thank you!')
        break