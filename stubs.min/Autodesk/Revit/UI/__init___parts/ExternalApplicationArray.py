class ExternalApplicationArray(APIObject, IDisposable, IEnumerable):
    """ ExternalApplicationArray() """
    def Append(self, item):
        """ Append(self: ExternalApplicationArray, item: IExternalApplication) """
        pass

    def Clear(self):
        """ Clear(self: ExternalApplicationArray) """
        pass

    def Dispose(self):
        """ Dispose(self: ExternalApplicationArray, A_0: bool) """
        pass

    def ForwardIterator(self):
        """ ForwardIterator(self: ExternalApplicationArray) -> ExternalApplicationArrayIterator """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ExternalApplicationArray) -> IEnumerator """
        pass

    def Insert(self, item, index):
        """ Insert(self: ExternalApplicationArray, item: IExternalApplication, index: int) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExternalApplicationArray) """
        pass

    def ReverseIterator(self):
        """ ReverseIterator(self: ExternalApplicationArray) -> ExternalApplicationArrayIterator """
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
    """Get: IsEmpty(self: ExternalApplicationArray) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: ExternalApplicationArray) -> int

"""


