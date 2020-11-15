from mod_1 import AD
import numpy as np

from mod_1 import AD
x = AD(3, 1)
y = AD(2, 0)
 
def test_basic_addition_v():
  
    try: 
        derivative = x + y
        print(f"Add Val: Value of x + y is {derivative.val}. \nAdd Der: Derivative of x + y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_addition_c():
  
    try: 
        derivative = x + 2
        print(f"Add Val: Value of x + 2 is {derivative.val}. \nAdd Der: Derivative of x + 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_subtraction_v():
    try:
        derivative = x - y
        print(f"Subtract Val: Value of x - y is {derivative.val}. \nSubtract Der: Derivative of x - y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_subtraction_c():

    try: 
        derivative = x - 2
        print(f"Subtract Val: Value of x - 2 is {derivative.val}. \nSubtract Der: Derivative of x - 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_multiplication_v():

    try: 
        derivative = x * y
        print(f"Multiplication Val: Value of x * y is {derivative.val}. \nMultiplication Der: Derivative of x * y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_multiplication_c():

    try: 
        derivative = x * 2
        print(f"Multiplication Val: Value of x * 2 is {derivative.val}. \nMultiplication Der: Derivative of x * 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_div_v():

    try: 
        derivative = x / y
        print(f"Division Val: Value of x / y is {derivative.val}. \nDivision Der: Derivative of x / y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_div_c():

    try: 
        derivative = x / 2
        print(f"Division Val: Value of x / 2 is {derivative.val}. \nDivision Der: Derivative of x / 2 is {derivative.der}.")
    except Exception as e:
        print(e)


def test_basic_power_v():

    try: 
        derivative = x ** y
        print(f"Power Val: Value of x ** y is {derivative.val}. \nPower Der: Derivative of x ** y is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_power_c():

    try: 
        derivative = x ** 2
        print(f"Power Val: Value of x ** 2 is {derivative.val}. \nPower Der: Derivative of x ** 2 is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_exponential():

    try:
        derivative = np.exp(x)
        print(f"Exp Val: Value of e ** x is {derivative.val}. \nExp Der: Derivative of e ** x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_radd_v():
    
    try: 
        derivative = y + x
        print(f"Radd Val: Value of y+x is {derivative.val}. \nRadd Der: Derivative of y+x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_radd_c():
    
    try: 
        derivative = 2 + x
        print(f"Radd Val: Value of 2+x is {derivative.val}. \nRadd Der: Derivative of 2+x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rmul_v():
    
    try: 
        derivative = y * x
        print(f"Rmul Val: Value of y * x is {derivative.val}. \nRmul Der: Derivative of y * x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rmul_c():
    
    try: 
        derivative = 2 * x
        print(f"Rmul Val: Value of 2+x is {derivative.val}. \nRmul Der: Derivative of 2+x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rsub_v():
    try:
        derivative = y-x
        print(f"Rsub Val: Value of y-x is {derivative.val}. \nRsub Der: Derivative of y-x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rsub_c():

    try: 
        derivative = 2-x
        print(f"Rsub Val: Value of 2-x is {derivative.val}. \nRsub Der: Derivative of 2-x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rdiv_v(): # Account for when the divisor is 0
    try:
        derivative = y/x
        print(f"Rdiv Val: Value of y/x is {derivative.val}. \nRdiv Der: Derivative of y/x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rdiv_c(): # Account for when the divisor is 0

    try: 
        derivative = 2/x
        print(f"Rdiv Val: Value of 2/x is {derivative.val}. \nRdiv Der: Derivative of 2/x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_rpow_v(): 
    try: 
        derivative = y ** x
        print(f"Rpow Val: Value of y ** x is {derivative.val}. \nRPow Der: Derivative of y ** x is {derivative.der}.")
    except Exception as e:
        print(e)


def test_basic_rpow_c(): 

    try: 
        derivative = 2 ** x
        print(f"Rpow Val: Value of 2 ** x is {derivative.val}. \nRpow Der: Derivative of 2 ** x is {derivative.der}.")
    except Exception as e:
        print(e)


def test_basic_neg(): 
    try: 
        derivative = -x
        print(f"Neg Val: Value of -x is {derivative.val}. \nNeg Der: Derivative of -x is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_sin(): 

    try: 
        derivative = AD.sin(x)
        print(f"Sin Val: Value of sin(x) is {derivative.val}. \nSin Der: Derivative of sin(x) is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_cos(): 

    try: 
        derivative = AD.cos(x)
        print(f"Cos Val: Value of cos(x) is {derivative.val}. \nCos Der: Derivative of cos(x) is {derivative.der}.")
    except Exception as e:
        print(e)

def test_basic_tan():

    try: 
        derivative = np.tan(x)
        print(f"Tan Val: Value of tan(x) is {derivative.val}. \nTan Der: Derivative of tan(x) is {derivative.der}.")
    except Exception as e:
        print(e)
