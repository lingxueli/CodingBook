import random

# wrap this in a function for unit test
def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                return True
            else:
                return False
        else:
            print('hey bozo, i said 1~10')
            return False
    except TypeError:
        print('please enter a number')
        return False

answer = random.randint(1,10)

# only run this if this is the main file being run
if __name__ == '__main__':
    while True:
        try:
            guess = int(input('guess a number 1 - 10: '))
            if (run_guess(guess, answer)):
                break

        except ValueError:
            print('please enter a number')
            continue