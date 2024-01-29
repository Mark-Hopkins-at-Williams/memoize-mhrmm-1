import unittest
from memoize import fib, Fibonacci, pascal, Pascal

class Q1(unittest.TestCase):

    def test_fib(self):
        assert fib(10) == 55, 'fib test failed!'
    
    def test_memofib(self):
        memofib = Fibonacci()
        assert memofib(10) == 55, 'memofib test failed!'

    def test_pascal(self):
        assert pascal(10, 3) == 120, 'pascal test failed!'
    
    def test_memopascal(self):
        memopascal = Pascal()
        assert memopascal(10, 3) == 120, 'memopascal test failed!'

            
if __name__ == "__main__":
    unittest.main() # run all tests