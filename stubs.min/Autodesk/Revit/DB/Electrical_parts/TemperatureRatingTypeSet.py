class TemperatureRatingTypeSet(APIObject, IDisposable, IEnumerable):
    """
    A set that contains TemperatureRating types.
    
    TemperatureRatingTypeSet()
    """
    def Clear(self):
        """
        Clear(self: TemperatureRatingTypeSet)
            Removes every TemperatureRating type from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> bool
        
            Tests for the existence of a TemperatureRating type within the set.
        
            item: The TemperatureRating type to be searched for.
            Returns: The Contains method returns True if the TemperatureRating type is within the 
             set, otherwise False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: TemperatureRatingTypeSet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> int
        
            Removes a specified TemperatureRating type from the set.
        
            item: The TemperatureRating type to be erased.
            Returns: The number of TemperatureRating types that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: TemperatureRatingTypeSet) -> TemperatureRatingTypeSetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: TemperatureRatingTypeSet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: TemperatureRatingTypeSet, item: TemperatureRatingType) -> bool
        
            Insert the specified TemperatureRating type into the set.
        
            item: The TemperatureRating type to be inserted into the set.
            Returns: Returns whether the TemperatureRating type was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TemperatureRatingTypeSet) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: TemperatureRatingTypeSet) -> TemperatureRatingTypeSetIterator
        
            Retrieve a backward moving iterator to the set.
            Returns: Returns a backward moving iterator to the set.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the set is empty.

Get: IsEmpty(self: TemperatureRatingTypeSet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of TemperatureRating types that are in the set.

Get: Size(self: TemperatureRatingTypeSet) -> int

"""


