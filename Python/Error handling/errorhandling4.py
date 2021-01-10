# stop the program from an error: raise
while True:
    try:
        age = int(input('what s your age? '))
        10/age
        # this stops the program
        raise ValueError('hey cut it out')
        # alternative: stop from any type of error
        raise Exception('hey cut it out')
    # remove the except part
    # except ValueError:
    #     print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
    # no thing failed
        print('thank you!')
        break