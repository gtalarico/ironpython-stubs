class ElementArray(APIObject, IDisposable, IEnumerable):
    """
    An array that contains element objects.
    
    ElementArray()
    """
    def Append(self, item):
        """
        Append(self: ElementArray, item: Element)
            Add the element to the end of the array.
        
            item: The element to be added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ElementArray)
            Removes every element from the array, rendering it empty.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ElementArray, A_0: bool) """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: ElementArray) -> ElementArrayIterator
        
            Retrieve a forward moving iterator to the array.
            Returns: Returns a forward moving iterator to the array.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ElementArray) -> IEnumerator
        
            Retrieve a forward moving iterator to the array.
            Returns: Returns a forward moving iterator to the array.
        """
        pass

    def Insert(self, item, index):
        """
        Insert(self: ElementArray, item: Element, index: int)
            Insert the specified element into the array.
        
            item: The element to be inserted into the array.
            index: The element will be inserted before this index.
            Returns: Returns whether the element was inserted into the array.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementArray) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: ElementArray) -> ElementArrayIterator
        
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

Get: IsEmpty(self: ElementArray) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of elements that are in the array.

Get: Size(self: ElementArray) -> int

"""


