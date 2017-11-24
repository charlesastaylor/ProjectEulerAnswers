"""Common classes and functions used in project euler problems"""

from functools import partial
from math import sqrt


def is_prime(x):
    """Tests if x is a prime number."""
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_primes(n):
    """Return set of all primes <= n."""
    if n <= 1:
        raise ValueError("get_primes: no primes <= 1")
    L = [True] * (n + 1)
    for i in range(2, int(sqrt(n) + 1)):
        if L[i]:
            for j in range(i**2, n + 1, i):
                L[j] = False
    return {i for i, prime in enumerate(L) if i > 1 and prime}

class Memoized(object):
    '''Decorator. Caches a function's return value each time it is called.

    If called later with the same arguments, the cached value is returned,
    not reevaluated.
    Source: https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        # if not isinstance(args, collections.Hashable):
        #     # uncacheable. a list, for instance.
        #     # better to not cache than blow up.
        #     return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return partial(self.__call__, obj)
