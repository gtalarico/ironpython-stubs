class ModelCurveArrArray(APIObject, IDisposable, IEnumerable):
    """
    An array that can contain any type of object.
    
    ModelCurveArrArray()
    """
    def Append(self, item):
        """ Append(self: ModelCurveArrArray, item: ModelCurveArray) """
        pass

    def Clear(self):
        """
        Clear(self: ModelCurveArrArray)
            Removes every item from the array, rendering it empty.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ModelCurveArrArray, A_0: bool) """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ModelCurveArrArray) -> ModelCurveArrArrayIterator
        
            Retrieve a forward moving iterator to the array.
            Returns: Returns a forward moving iterator to the array.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ModelCurveArrArray) -> IEnumerator
        
            Retrieve a forward moving iterator to the array.
            Returns: Returns a forward moving iterator to the array.
        """
        pass

    def Insert(self, item, index):
        """ Insert(self: ModelCurveArrArray, item: ModelCurveArray, index: int) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ModelCurveArrArray) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ModelCurveArrArray) -> ModelCurveArrArrayIterator
        
            Retrieve a backward moving iterator to the array.
            Returns: Returns a backward moving iterator to the array.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Test to see if the array is empty.

Get: IsEmpty(self: ModelCurveArrArray) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of objects that are in the array.

Get: Size(self: ModelCurveArrArray) -> int

"""


