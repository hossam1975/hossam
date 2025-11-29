import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Function: الضرب
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b
def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

# Function: ترجع Null (None)
def return_null():
    return None
def power(a, b):    
    return a ** b
def modulus(a, b):    
    return a % b
def floor_divide(a, b):    
    if b == 0:
        return "Error: division by zero"
    return a // b
def square_root(a):    
    if a < 0:
        return "Error: negative input"
    return a ** 0.5
def cube_root(a):    
    if a < 0:
        return -(-a) ** (1/3)
    return a ** (1/3)
