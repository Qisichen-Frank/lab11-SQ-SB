"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b): b / a   # raise ZeroDivisionError if a == 0 

def logarithm(a, b): loga(b)# use math library/raise ValueError

def exponent(a, b): ab
"""
import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError("a can't be 0")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm arguments.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
        



