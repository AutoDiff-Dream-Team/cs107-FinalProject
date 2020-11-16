from mod_1 import AD
import numpy as np

from mod_1 import AD
x = AD(3, 1)
y = AD(2, 0)


def test_comp_1():
  
    try: 
        derivative = 2*(x + y)
        print(f"Value of 2*(x + y) is {derivative.val}. \nDerivative of 2*(x + y) is {derivative.der}.")
    except Exception as e:
        print(e)

def test_comp_2():
  
    try: 
        derivative = AD.sin(x) - y ** 2
        print(f"Value of sin(x) - y ** 2 is {derivative.val}. \nDerivative of sin(x) - y ** 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_comp_3():
  
    try: 
        derivative = AD.cos(x/y)
        print(f"Value of cos(x/y) is {derivative.val}. \nDerivative of cos(x/y) is {derivative.der}.")
    except Exception as e:
        print(e)

def test_comp_4():
  
    try: 
        derivative = AD.tan(y) / x / 2
        print(f"Value of tan(y) / x / 2 is {derivative.val}. \nDerivative of tan(y) / x / 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_comp_5():
  
    try: 
        derivative = AD.exp(x) * y
        print(f"Value of exp(x) * y is {derivative.val}. \nDerivative of exp(x) * y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_comp_6():
  
    try: 
        derivative = 2 ** (-x) - y
        print(f"Value of 2 ** (-x) - y is {derivative.val}. \nDerivative of 2 ** (-x) - y is {derivative.der}.")
    except Exception as e:
        print(e)
