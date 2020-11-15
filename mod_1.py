import numpy as np


class AD:
    
    # initialize with input value
    def __init__(self, val=1, der=1):
        self.val = val
        self.der = der

    # addition
    def __add__(self, other):
        try:
            val_add = self.val + other.val
            der_add = self.der + other.der
        except AttributeError:
            val_add = self.val + other
            der_add = self.der

        return AD(val_add, der_add)

    # multiplication
    def __mul__(self, other):
        try:
            val_add = self.val * other.val
            der_add = self.der * other.val + other.der * self.val
        except AttributeError:
            val_add = self.val * other
            der_add = self.der * other

        return AD(val_add, der_add)

    # subtraction
    def __sub__(self, other):
        try:
            val_sub = self.val - other.val
            der_sub = self.der - other.der
        except AttributeError:
            val_sub = self.val - other
            der_sub = self.der

        return AD(val_sub, der_sub)

    # division
    def __truediv__(self, other):
        try:
            val_div = self.val / other.val
            der_div = self.der / other.val + (-self.val/other.val**2)*other.der
        except AttributeError:
            val_div = self.val / other
            der_div = self.der / other
        
        return AD(val_div, der_div)

    # exponential
    def __pow__(self, other):
        try:
            if other.der > 0:
                val_div = self.val ** other.val
                der_div = other.val * self.val**(other.val-1) * self.der + np.log(self.val) * self.val**other.val * other.der
            else:
                val_div = self.val ** other.val
                der_div = other.val * self.val**(other.val-1) * self.der
        except AttributeError:
            val_div = self.val ** other
            der_div = other*self.val**(other-1)*self.der
        
        return AD(val_div, der_div)
        
    # reverse exponential
    def __rpow__(self, other):
        try:
            val_div = other.val ** self.val
            der_div = self.val * other.val**(self.val-1) * other.der + np.log(other.val) * other.val**self.val * self.der
        except AttributeError:
            val_div = other ** self.val
            der_div = np.log(other) * other**self.val * self.der

        return AD(val_div, der_div)

    # reverse addition
    def __radd__(self, other):
        return self.__add__(other)

    # reverse multiplication
    def __rmul__(self, other):
        return self.__mul__(other)

    # reverse subtraction
    def __rsub__(self,other):
        try:
            val_sub = other.val - self.val
            der_sub = other.der - self.der
        except AttributeError:
            val_sub =  other - self.val
            der_sub = -self.der

        return AD(val_sub, der_sub)

    # reverse division
    def __rtruediv__(self, other):
        try:
            val_div = other.val / self.val
            # der_div = other.der / self.der
            der_div = other.val * (-1 * (self.val ** (-2)) * self.der) + other.der * (1 / self.val)

        except AttributeError:
            val_div = other / self.val
            der_div = (-other/self.val**2)*self.der
    
        return AD(val_div, der_div)

    def get_value(self):
        return self.val
    
    def get_derivative(self):
        return self.der

    def get_eval(self):
        return self.var, self.der
        
    # sin
    def sin(self):
        try:
            val = np.sin(self.val)
            der = np.cos(self.val) * self.der
        except AttributeError:
            val = np.sin(self)
            der = 0
        return AD(val, der)

    # cos
    def cos(self):
        try:
            val = np.cos(self.val)
            der = -np.sin(self.val) * self.der
        except AttributeError:
            val = np.cos(self)
            der = 0
        return AD(val, der)

    # tangent
    def tan(self):
        try:
            val = np.tan(self.val)
            der = (1/np.cos(self.val)) ** 2 * self.der
        except AttributeError:
            val = np.tan(self)
            der = 0
        return AD(val, der)

    # exponential
    def exp(self):
        try:
            val = np.exp(self.val)
            der = np.exp(self.val) * self.der
        except AttributeError:
            val = np.exp(self)
            der = 0
        return AD(val, der)

    def __neg__(self):
        try:
            val = -1 * self.val
            der = -1 * self.der
        except AttributeError:
            val = -1 * self
            der = 0
        return AD(val, der)

    def __repr__(self):
        return 'AD({}, {})'.format(self.val, self.der)

    def __str__(self):
        return 'AD({}, {})'.format(self.val, self.der)