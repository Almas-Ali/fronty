'''
The main test module for the fronty package.
Here we will call this module from the command line to run all the tests at once.

Usage:
    python -m tests
        
'''

import unittest


def main():
    '''Runs all the tests at once.'''
    suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
