    
def fib(n):
    """
    The Fibonacci numbers form a sequence such that each number is the sum
    of the two preceding ones, starting from 0 and 1.
    
    That is, fib(0) = 0, fib(1) = 1, and fib(n) = fib(n-1) + fib(n+2).
    
    This function computes the nth Fibonacci number.
    
    """
    fibs = [0, 1]
    while len(fibs) < n+1:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]



class Fibonacci:
    """
    The Fibonacci numbers form a sequence such that each number is the sum
    of the two preceding ones, starting from 0 and 1.
    
    That is, fib(0) = 0, fib(1) = 1, and fib(n) = fib(n-1) + fib(n+2).
    
    This function computes the nth Fibonacci number. Note that it caches
    the previously computed numbers, so subsequent fib(n) calls should be
    constant-time.
    
    """
    
    def __init__(self):
        self.fibs = [0, 1]
    
    def __call__(self, n):        
        while len(self.fibs) < n+1:
            self.fibs.append(self.fibs[-1] + self.fibs[-2])
        return self.fibs[n]
                
    
def pascal(n, k):
    """
    Computes the element in the nth row and kth column of Pascal's triangle.
    
    Note that:
        - pascal(n, n) = pascal(n, 0) = 1
        - otherwise, pascal(n, k) = pascal(n-1, k-1) + pascal(n-1, k)
    
    """
    elements = dict()
    for i in range(n+1):
        for j in range(i+1):
            if i == j or i == 0 or j == 0:
                elements[(i,j)] = 1
            else:
                elements[(i,j)] = elements[(i-1, j-1)] + elements[(i-1, j)]
    return elements[(n,k)]
    

class Pascal:
    """
    Computes the element in the nth row and kth column of Pascal's triangle.
    
    Note that:
        - pascal(n, n) = pascal(n, 0) = 1
        - otherwise, pascal(n, k) = pascal(n-1, k-1) + pascal(n-1, k)
    
    This function caches previously computed elements, so subsequent 
    pascal(n,k) calls should be constant-time.
    
    """
    def __init__(self):
        raise NotImplementedError("Q1")
