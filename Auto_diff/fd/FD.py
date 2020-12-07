import numpy as np


class FD:
    
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

        return FD(val_add, der_add)

    # multiplication
    def __mul__(self, other):
        try:
            val_add = self.val * other.val
            der_add = self.der * other.val + other.der * self.val
        except AttributeError:
            val_add = self.val * other
            der_add = self.der * other

        return FD(val_add, der_add)

    # subtraction
    def __sub__(self, other):
        try:
            val_sub = self.val - other.val
            der_sub = self.der - other.der
        except AttributeError:
            val_sub = self.val - other
            der_sub = self.der

        return FD(val_sub, der_sub)

    # division
    def __truediv__(self, other):
        try:
            val_div = self.val / other.val
            der_div = self.der / other.val + (-self.val/other.val**2)*other.der
        except AttributeError:
            val_div = self.val / other
            der_div = self.der / other
        
        return FD(val_div, der_div)

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
        
        return FD(val_div, der_div)
        
    # reverse exponential
    def __rpow__(self, other):
        val_div = other ** self.val
        der_div = np.log(other) * other**self.val * self.der

        return FD(val_div, der_div)

    # reverse addition
    def __radd__(self, other):
        return self.__add__(other)

    # reverse multiplication
    def __rmul__(self, other):
        return self.__mul__(other)

    # reverse subtraction
    def __rsub__(self,other):
        val_sub =  other - self.val
        der_sub = -self.der

        return FD(val_sub, der_sub)

    # reverse division
    def __rtruediv__(self, other):
        val_div = other / self.val
        der_div = (-other/self.val**2)*self.der
    
        return FD(val_div, der_div)

    def get_value(self):
        return self.val
    
    def get_derivative(self):
            return self.der

    @staticmethod
    def get_derivatives(args):
        if type(args[0]) is not list and type(args[0]) is not np.array and type(args[0]) is not np.ndarray:
            args = [args]
        ders = []
        for arg in args:
            arg_der = []
            for ad in arg:
                arg_der.append(ad.der)
            ders.append(arg_der)

        return np.array(ders)

    @staticmethod
    def get_values(args):
        if type(args[0]) is not list and type(args[0]) is not np.array and type(args[0]) is not np.ndarray:
            args = [args]
        ders = []
        for arg in args:
            arg_der = []
            for ad in arg:
                arg_der.append(ad.val)
            ders.append(arg_der)

        return np.array(ders)
        
    # sin
    def sin(self):
        val = np.sin(self.val)
        der = np.cos(self.val) * self.der
        return FD(val, der)

    # cos
    def cos(self):
        val = np.cos(self.val)
        der = -np.sin(self.val) * self.der
        return FD(val, der)

    # tangent
    def tan(self):
        val = np.tan(self.val)
        der = (1/np.cos(self.val)) ** 2 * self.der
        return FD(val, der)

    # hyperbolic sine
    def sinh(self):
        val = np.sinh(self.val)
        der = np.cosh(self.val) * self.der
        return FD(val, der)

    # hyperbolic cosine
    def cosh(self):
        val = np.cosh(self.val)
        der = np.sinh(self.val) * self.der
        return FD(val, der)

    # hyperbolic tangent
    def tanh(self):
        val = np.tanh(self.val)
        der = 1/np.cosh(self.val)**2 * self.der
        return FD(val, der)
    
    # exponential
    def exp(self):
        val = np.exp(self.val)
        der = np.exp(self.val) * self.der
        return FD(val, der)

    def __neg__(self):
        val = -1 * self.val
        der = -1 * self.der
        return FD(val, der)

    def __repr__(self):
        return 'FD({}, {})'.format(self.val, self.der)

    def __str__(self):
        return 'FD({}, {})'.format(self.val, self.der)