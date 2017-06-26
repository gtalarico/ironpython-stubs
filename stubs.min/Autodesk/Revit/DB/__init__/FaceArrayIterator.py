class FaceArrayIterator(APIObject, IDisposable, IEnumerator):
    """
    An iterator to a face array.
    
    FaceArrayIterator()
    """
    def Dispose(self):
        """ Dispose(self: FaceArrayIterator, A_0: bool) """
        pass

    def MoveNext(self):
        """
        MoveNext(self: FaceArrayIterator) -> bool
        
            Move the iterator one item forward.
            Returns: Returns True if the iterator was successfully moved forward one item and the 
             Current
                    property will return a valid item. False will be returned 
             it the iterator has reached the end of
                    the array.
        """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FaceArrayIterator) """
        pass

    def Reset(self):
        """
        Reset(self: FaceArrayIterator)
            Bring the iterator back to the start of the array.
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
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves the item that is the current focus of the iterator.

Get: Current(self: FaceArrayIterator) -> object

"""


