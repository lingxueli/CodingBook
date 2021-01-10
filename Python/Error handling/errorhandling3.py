# python built in error
while True:
    try:
        age = int(input('what s your age? '))
        10/age
    except ValueError:
        print('please enter a number')
        continue # after this execute finally, line 18 will not be executed
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break # after this execute finally, line 18 will not be executed
    else:
    # no thing failed
        print('thank you!')
        break # after this execute finally, line 18 will not be executed
    finally:
        print('ok, i m finally done')
    print('can you hear me') 