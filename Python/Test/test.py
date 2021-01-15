import unittest

import main

class testmain(unittest.TestCase):
    def setUp(self):
        print('begin test')

    def test_run_guess(self):
        answer = 5
        guess = 5
        result = main.run_guess(guess, answer)
        self.assertTrue(result)

    def test_run_guess_wrong_guess(self):
        answer = 5
        guess = 1
        result = main.run_guess(guess, answer)
        self.assertFalse(result)

    def test_run_guess_outOfRange(self):
        answer = 5
        guess = 11
        result = main.run_guess(guess, answer)
        self.assertFalse(result)


    def test_run_guess_wrong_type(self):
        answer = 5
        guess = '11'
        result = main.run_guess(guess, answer)
        self.assertFalse(result)


    def tearDown(self):
        print('finished test')

# only run test if this is the main file being run
if __name__ == '__main__':
    unittest.main()


# python -m unittest -v