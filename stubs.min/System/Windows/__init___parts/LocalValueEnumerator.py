class LocalValueEnumerator(object, IEnumerator):
    """ Provides enumeration support for the local values of any dependency properties that exist on a System.Windows.DependencyObject. """
    def Equals(self, obj):
        """
        Equals(self: LocalValueEnumerator, obj: object) -> bool
        
            Determines whether the provided System.Windows.LocalValueEnumerator is equivalent to this System.Windows.LocalValueEnumerator.
        
            obj: The System.Windows.LocalValueEnumerator to compare with the current System.Windows.LocalValueEnumerator.
            Returns: true if the specified System.Windows.LocalValueEnumerator is equal to the current System.Windows.LocalValueEnumerator; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: LocalValueEnumerator) -> int
        
            Returns a hash code for the current System.Windows.LocalValueEnumerator.
            Returns: A 32-bit integer hash code.
        """
        pass

    def MoveNext(self):
        """
        MoveNext(self: LocalValueEnumerator) -> bool
        
            Advances the enumerator to the next element of the collection.
            Returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """
        Reset(self: LocalValueEnumerator)
            Sets the enumerator to its initial position, which is before the first element in the collection.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items that are represented in the collection.

Get: Count(self: LocalValueEnumerator) -> int

"""

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the current element in the collection.

Get: Current(self: LocalValueEnumerator) -> LocalValueEntry

"""


