from mod_1 import AD
import numpy as np

from mod_1 import AD
x = AD(3, 1)
y = AD(2, 0)
 
def test_basic_addition_v():
    derivative = x + y
    assert (float(derivative.get_value()) == 5.0) & (float(derivative.get_derivative()) == 1.0), Exception(f'test_basic_addition_c() has error.')
    
def test_basic_addition_c():
    derivative = x + 2
    assert (float(derivative.val) == 5.0) & (float(derivative.der) == 1.0), Exception(f'test_basic_addition_c() has error.')

def test_basic_subtraction_v():
    derivative = x - y
    assert ((float(derivative.val)) == 1.0) & (float(derivative.der) == 1.0), Exception(f'test_basic_subtraction_v() has error.')

def test_basic_subtraction_c():
    derivative = x - 2
    assert ((float(derivative.val)) == 1.0) & (float(derivative.der) == 1.0), Exception(f'test_basic_subtraction_c() has error.')

def test_basic_multiplication_v():
    derivative = x * y
    assert ((float(derivative.val) == 6.0) & (float(derivative.der) == 2.0)), Exception(f'test_basic_multiplication_v() has error.')

def test_basic_multiplication_c():
    derivative = x * 2
    assert ((float(derivative.val) == 6.0)  & (float(derivative.der) == 2.0)), Exception(f'test_basic_multiplication_c() has error.')

def test_basic_div_v():
    derivative = x / y
    assert ((float(derivative.val) == 1.50)  & (float(derivative.der) == 0.5)), Exception(f'test_basic_div_v() has error.')

def test_basic_div_c():
    derivative = x / 2
    assert ((float(derivative.val) == 1.50) & (float(derivative.der) == 0.5)), Exception(f'test_basic_div_c() has error.')

def test_basic_power_v():
    derivative = x ** y
    assert ((float(derivative.val) == 9.0) & (float(derivative.der) == 6.0)), Exception(f'test_basic_power_v() has error.')

def test_basic_power_c():
    derivative = x ** 2
    assert ((float(derivative.val) == 9.0) & (float(derivative.der) == 6.0)), Exception(f'test_basic_power_c() has error.')

def test_basic_exponential_v():
    derivative = np.exp(x)
    assert ((float(derivative.val) == np.exp(3)) & (float(derivative.der) == np.exp(3))), Exception(f'test_basic_exponential_v() has error.')

def test_basic_exponential_c():
    derivative = AD.exp(2)
    assert ((float(derivative.val) == np.exp(2)) & (float(derivative.der) == 0.0)), Exception(f'test_basic_exponential_c() has error.')

def test_basic_radd_v():
    derivative = y + x
    assert ((float(derivative.val) == 5.0) & (float(derivative.der) == 1.0)), Exception(f'test_basic_radd_v() has error.')

def test_basic_radd_c():
    derivative = 2 + x
    assert ((float(derivative.val)) == 5.0)  & (float(derivative.der) == 1.0), Exception(f'test_basic_radd_c() has error.')

def test_basic_rmul_v():
    derivative = y * x
    assert ((float(derivative.val) == 6.0) & (float(derivative.der) == 2.0)), Exception(f'test_basic_rmul_v() has error.')

def test_basic_rmul_c():
    derivative = 2 * x
    assert ((float(derivative.val) == 6.0) & (float(derivative.der) == 2.0)), Exception(f'test_basic_rmul_c() has error.')

def test_basic_rsub_v():
    derivative = y-x
    assert ((float(derivative.val) == -1.0) & (float(derivative.der) == -1.0)), Exception(f'test_basic_rsub_v() has error.')

def test_basic_rsub_c():
    derivative = 2-x
    assert (float(derivative.val) == -1.0) & (float(derivative.der) == -1.0), Exception(f'test_basic_rsub_c() has error.')

def test_basic_rdiv_c(): # Account for when the divisor is 0
    derivative = 2/x
    assert (float(derivative.val) == (2/3)) & (float(derivative.der) == -(2/9)), Exception(f'test_basic_rdiv_c() has error.')

def test_basic_rpow_c(): 
    derivative = 2 ** x
    assert (float(derivative.val) == 8.0) & (float(derivative.der) == 8*np.log(2)), Exception(f'test_basic_rpow_c() has error.')

def test_basic_neg_v(): 
    derivative = -x
    assert (float(derivative.val) == -3.0) & (float(derivative.der) == -1.0), Exception(f'test_basic_neg_v() has error.')

def test_basic_sin_v(): 
    derivative = AD.sin(x)
    assert (float(derivative.val) == np.sin(3)) & (float(derivative.der) == np.cos(3)), Exception(f'test_basic_sin_v() has error.')


def test_basic_sin_c(): 
    derivative = AD.sin(2)
    assert (float(derivative.val) == np.sin(2)) & (float(derivative.der) == 0.0), Exception(f'test_basic_sin_c() has error.')


def test_basic_cos_v(): 
    derivative = AD.cos(x)
    assert (float(derivative.val) == np.cos(3)) & (float(derivative.der) == -np.sin(3)), Exception(f'test_basic_cos_v() has error.')

def test_basic_cos_c(): 
    derivative = AD.cos(2)
    assert (float(derivative.val) == np.cos(2)) & (float(derivative.der) == 0.0), Exception(f'test_basic_cos_c() has error.')

def test_basic_tan_v():
    derivative = AD.tan(x)
    assert (float(derivative.val) == np.tan(3)) & (float(derivative.der) == 1/(np.cos(3))**2), Exception(f'test_basic_tan_v() has error.')

def test_basic_tan_c():
    derivative = AD.tan(2)
    assert (float(derivative.val) == np.tan(2)) & (float(derivative.der) == 0.0), Exception(f'test_basic_tan_c() has error.')

def test_basic_repr():
    assert repr(x) == 'AD(3, 1)'

def test_basic_str():
    assert str(x) == 'AD(3, 1)'