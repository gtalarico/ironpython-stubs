class ArraySegment(object, IList[T], ICollection[T], IEnumerable[T], IEnumerable, IReadOnlyList[T], IReadOnlyCollection[T]):
    """
    ArraySegment[T](array: Array[T])
    ArraySegment[T](array: Array[T], offset: int, count: int)
    """
    def Equals(self, obj):
        """
        Equals(self: ArraySegment[T], obj: ArraySegment[T]) -> bool
        
            Determines whether the specified System.ArraySegment structure is equal to the current instance.
        
            obj: The System.ArraySegment structure to be compared with the current instance.
            Returns: true if the specified System.ArraySegment structure is equal to the current instance; otherwise, false.
        Equals(self: ArraySegment[T], obj: object) -> bool
        
            Determines whether the specified object is equal to the current instance.
        
            obj: The object to be compared with the current instance.
            Returns: true if the specified object is a System.ArraySegment structure and is equal to the current instance; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ArraySegment[T]) -> int
        
            Returns the hash code for the current instance.
            Returns: A 32-bit signed integer hash code.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[T], item: T) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: true if item is found in the System.Collections.Generic.ICollection; otherwise, false.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, array, offset=None, count=None):
        """
        __new__(cls: type, array: Array[T])
        __new__(cls: type, array: Array[T], offset: int, count: int)
        __new__[ArraySegment`1]() -> ArraySegment[T]
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Array = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the original array containing the range of elements that the array segment delimits.

Get: Array(self: ArraySegment[T]) -> Array[T]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the range delimited by the array segment.

Get: Count(self: ArraySegment[T]) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position of the first element in the range delimited by the array segment, relative to the start of the original array.

Get: Offset(self: ArraySegment[T]) -> int

"""


