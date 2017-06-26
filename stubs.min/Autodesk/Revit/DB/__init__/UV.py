class UV(object):
    """
    Object representing coordinates in 2-dimensional space.
    
    UV(u: float, v: float)
    UV()
    """
    def Add(self, source):
        """
        Add(self: UV, source: UV) -> UV
        
            Adds the specified 2-D vector to this 2-D vector and returns the result.
        
            source: The vector to add to this vector.
            Returns: The 2-D vector equal to the sum of the two vectors.
        """
        pass

    def AngleTo(self, source):
        """
        AngleTo(self: UV, source: UV) -> float
        
            Returns the angle between this vector and the specified vector.
        
            source: The specified vector.
            Returns: The real number between 0 and 2*PI equal to the angle between the two vectors 
             in radians.
        """
        pass

    def CrossProduct(self, source):
        """
        CrossProduct(self: UV, source: UV) -> float
        
            The cross product of this 2-D vector and the specified 2-D vector.
        
            source: The vector to multiply with this vector.
            Returns: The real number equal to the cross product.
        """
        pass

    def DistanceTo(self, source):
        """
        DistanceTo(self: UV, source: UV) -> float
        
            Returns the distance from this 2-D point to the specified 2-D point.
        
            source: The specified point.
            Returns: The real number equal to the distance between the two points.
        """
        pass

    def Divide(self, value):
        """
        Divide(self: UV, value: float) -> UV
        
            Divides this 2-D vector by the specified value and returns the result.
        
            value: The value to divide this vector by.
            Returns: The divided 2-D vector.
        """
        pass

    def DotProduct(self, source):
        """
        DotProduct(self: UV, source: UV) -> float
        
            The dot product of this 2-D vector and the specified 2-D vector.
        
            source: The vector to multiply with this vector.
            Returns: The real number equal to the dot product.
        """
        pass

    def GetLength(self):
        """
        GetLength(self: UV) -> float
        
            The length of this 2-D vector.
        """
        pass

    def IsAlmostEqualTo(self, source, tolerance=None):
        """
        IsAlmostEqualTo(self: UV, source: UV) -> bool
        
            Determines whether this 2-D vector and the specified 2-D vector are the same 
             within the tolerance (1.0e-09).
        
        
            source: The vector to compare with this vector.
            Returns: True if the vectors are the same; otherwise, false.
        IsAlmostEqualTo(self: UV, source: UV, tolerance: float) -> bool
        
            Determines whether this 2-D vector and the specified 2-D vector are the same 
             within a specified tolerance.
        
        
            source: The vector to compare with this vector.
            tolerance: The tolerance for equality check.
            Returns: True if the vectors are the same; otherwise, false.
        """
        pass

    def IsUnitLength(self):
        """
        IsUnitLength(self: UV) -> bool
        
            The boolean value indicates whether this 2-D vector is of unit length.
        """
        pass

    def IsZeroLength(self):
        """
        IsZeroLength(self: UV) -> bool
        
            The boolean value indicates whether this 2-D vector is a zero vector.
        """
        pass

    def Multiply(self, value):
        """
        Multiply(self: UV, value: float) -> UV
        
            Multiplies this 2-D vector by the specified value and returns the result.
        
            value: The value to multiply with this vector.
            Returns: The multiplied 2-D vector.
        """
        pass

    def Negate(self):
        """
        Negate(self: UV) -> UV
        
            Negates this 2-D vector.
            Returns: The 2-D vector opposite to this vector.
        """
        pass

    def Normalize(self):
        """
        Normalize(self: UV) -> UV
        
            Returns a new UV whose coordinates are the normalized values from this vector.
            Returns: The normalized UV or zero if the vector is almost Zero.
        """
        pass

    def Subtract(self, source):
        """
        Subtract(self: UV, source: UV) -> UV
        
            Subtracts the specified 2-D vector from this 2-D vector and returns the result.
        
            source: The vector to subtract from this vector.
            Returns: The 2-D vector equal to the difference between the two vectors.
        """
        pass

    def ToString(self):
        """
        ToString(self: UV) -> str
        
            Gets formatted string showing (U, V) with values formatted to 9 decimal places.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, u=None, v=None):
        """
        __new__(cls: type, u: float, v: float)
        __new__(cls: type)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(left: UV, right: UV) -> UV
        
            Adds the two specified 2-D vectors and returns the result.
        
            left: The first vector.
            right: The second vector.
            Returns: The 2-D vector equal to the sum of the two source vectors.
        """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(value: float, right: UV) -> UV
        
            The product of the specified number and the specified 2-D vector.
        
            value: The value to multiply with the specified vector.
            right: The vector to multiply with the value.
            Returns: The multiplied 2-D vector.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: UV, right: UV) -> UV
        
            Subtracts the two specified 2-D vectors and returns the result.
        
            left: The first vector.
            right: The second vector.
            Returns: The 2-D vector equal to the difference between the two source vectors.
        """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first coordinate.

Get: U(self: UV) -> float

"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the second coordinate.

Get: V(self: UV) -> float

"""


    BasisU = None
    BasisV = None
    Zero = None

