class Int32(object):
    """ Represents a 32-bit signed integer. """
    def bit_length(self, *args): #cannot find CLR method
        """ bit_length(value: int) -> int """
        pass

    def conjugate(self, *args): #cannot find CLR method
        """ conjugate(x: int) -> int """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: int, y: int) -> int """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __coerce__(self, *args): #cannot find CLR method
        """ __coerce__(x: int, o: object) -> object """
        pass

    def __divmod__(self, *args): #cannot find CLR method
        """
        __divmod__(x: int, y: object) -> object
        __divmod__(x: int, y: int) -> tuple
        """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __float__(self: int) -> float """
        pass

    def __floordiv__(self, *args): #cannot find CLR method
        """ x.__floordiv__(y) <==> x//y """
        pass

    def __getnewargs__(self, *args): #cannot find CLR method
        """ __getnewargs__(self: int) -> object """
        pass

    def __hex__(self, *args): #cannot find CLR method
        """ __hex__(x: int) -> str """
        pass

    def __index__(self, *args): #cannot find CLR method
        """ __index__(x: int) -> int """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(self: int) -> int """
        pass

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: int) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __long__(self: int) -> long """
        pass

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        pass

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, s: IList[Byte]) -> object
        __new__(cls: type, x: object) -> object
        __new__(cls: type) -> object
        __new__(o: object) -> object
        __new__(cls: type, o: Extensible[float]) -> object
        __new__(cls: type, s: str, base: int) -> object
        """
        pass

    def __nonzero__(self, *args): #cannot find CLR method
        """ __nonzero__(x: int) -> bool """
        pass

    def __oct__(self, *args): #cannot find CLR method
        """ __oct__(x: int) -> str """
        pass

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: int, y: int) -> int """
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(x: int) -> int """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: int, y: int) -> object """
        pass

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: int, y: int) -> int """
        pass

    def __rdivmod__(self, *args): #cannot find CLR method
        """ __rdivmod__(x: int, y: int) -> object """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: int, y: int) -> object """
        pass

    def __rfloordiv__(self, *args): #cannot find CLR method
        """ __rfloordiv__(x: int, y: int) -> object """
        pass

    def __rlshift__(self, *args): #cannot find CLR method
        """ __rlshift__(x: int, y: int) -> object """
        pass

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: int, y: int) -> int """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: int, y: int) -> object """
        pass

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: int, y: int) -> int """
        pass

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(x: int, power: int, qmod: Nullable[int]) -> object
        __rpow__(x: int, power: int) -> object
        __rpow__(x: int, power: long, qmod: long) -> object
        __rpow__(x: int, power: float, qmod: float) -> object
        """
        pass

    def __rrshift__(self, *args): #cannot find CLR method
        """ __rrshift__(x: int, y: int) -> int """
        pass

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: int, y: int) -> object """
        pass

    def __rtruediv__(self, *args): #cannot find CLR method
        """ __rtruediv__(x: int, y: int) -> float """
        pass

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: int, y: int) -> int """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, *args): #cannot find CLR method
        """ x.__truediv__(y) <==> x/y """
        pass

    def __trunc__(self, *args): #cannot find CLR method
        """ __trunc__(x: int) -> int """
        pass

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: int, y: int) -> int """
        pass

    denominator = None
    imag = None
    numerator = None
    real = None

