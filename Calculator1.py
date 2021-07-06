from itertools import count

from BasicArithmitic import *
class Calculator:

    count = 0
    def __init__(self):
        self._result = 0
        self.count = self.count + 1
        pass

    def add(self, a, b):
        return addition(a, b)
    def sub(self, a, b):
        return subtract(a, b)
    def div(self, a, b):
        return divide(a, b)
    def mul(self, a, b):
        return multiply(a, b)
    def square(self, a):
        return square(a)
    def squRoot(self, a):
        return squareRoot(a)
