class CookieCollection(object, ICollection, IEnumerable):
    """
    Provides a collection container for instances of the System.Net.Cookie class.
    
    CookieCollection()
    """
    def Add(self, *__args):
        """
        Add(self: CookieCollection, cookies: CookieCollection)
            Adds the contents of a System.Net.CookieCollection to the current instance.
        
            cookies: The System.Net.CookieCollection to be added.
        Add(self: CookieCollection, cookie: Cookie)
            Adds a System.Net.Cookie to a System.Net.CookieCollection.
        
            cookie: The System.Net.Cookie to be added to a System.Net.CookieCollection.
        """
        pass

    def CopyTo(self, array, index):
        """
        CopyTo(self: CookieCollection, array: Array[Cookie], index: int)
            Copies the elements of this System.Net.CookieCollection to a System.Net.Cookie array starting at the specified index of the target array.
        
            array: The target System.Net.Cookie array to which the System.Net.CookieCollection will be copied.
            index: The zero-based index in the target System.Array where copying begins.
        CopyTo(self: CookieCollection, array: Array, index: int)
            Copies the elements of a System.Net.CookieCollection to an instance of the System.Array class, starting at a particular index.
        
            array: The target System.Array to which the System.Net.CookieCollection will be copied.
            index: The zero-based index in the target System.Array where copying begins.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CookieCollection) -> IEnumerator
        
            Gets an enumerator that can iterate through a System.Net.CookieCollection.
            Returns: An instance of an implementation of an System.Collections.IEnumerator interface that can iterate through a System.Net.CookieCollection.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of cookies contained in a System.Net.CookieCollection.

Get: Count(self: CookieCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a System.Net.CookieCollection is read-only.

Get: IsReadOnly(self: CookieCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether access to a System.Net.CookieCollection is thread safe.

Get: IsSynchronized(self: CookieCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an object that you can use to synchronize access to the System.Net.CookieCollection.

Get: SyncRoot(self: CookieCollection) -> object

"""


