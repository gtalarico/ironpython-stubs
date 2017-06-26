class CategorySet(APIObject, IDisposable, IEnumerable):
    """
    A set that can contains Category objects.
    
    CategorySet()
    """
    def Clear(self):
        """
        Clear(self: CategorySet)
            Removes every item from the set, rendering it empty.
        """
        pass

    def Contains(self, item):
        """
        Contains(self: CategorySet, item: Category) -> bool
        
            Tests for the existence of a category within the set.
        
            item: The category to be searched for.
            Returns: The Contains method returns True if the category is within the set, otherwise 
             False.
        """
        pass

    def Dispose(self):
        """ Dispose(self: CategorySet, A_0: bool) """
        pass

    def Erase(self, item):
        """
        Erase(self: CategorySet, item: Category) -> int
        
            Removes a specified category from the set.
        
            item: The category to be erased.
            Returns: The number of items that were erased from the set.
        """
        pass

    def ForwardIterator(self):
        """
        ForwardIterator(self: CategorySet) -> CategorySetIterator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CategorySet) -> IEnumerator
        
            Retrieve a forward moving iterator to the set.
            Returns: Returns a forward moving iterator to the set.
        """
        pass

    def Insert(self, item):
        """
        Insert(self: CategorySet, item: Category) -> bool
        
            Insert the specified category into the set.
        
            item: The item to be inserted into the set.
            Returns: Returns whether the item was inserted into the set.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
        pass

    def ReverseIterator(self):
        """
        ReverseIterator(self: CategorySet) -> CategorySetIterator
        
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

Get: IsEmpty(self: CategorySet) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of categories that are in the set.

Get: Size(self: CategorySet) -> int

"""


