class KeynoteEntry(KeyBasedTreeEntry, IDisposable):
    """
    Represents an entry in the keynote table, containing the key value, keynote text, and parent key (if applicable).
    
    KeynoteEntry(key: str, text: str)
    KeynoteEntry(key: str, parentKey: str, text: str)
    """
    def Dispose(self):
        """ Dispose(self: KeyBasedTreeEntry, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: KeyBasedTreeEntry, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, key, *__args):
        """
        __new__(cls: type, key: str, text: str)
        __new__(cls: type, key: str, parentKey: str, text: str)
        """
        pass

    KeynoteText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The text associated with this KeynoteEntry.

Get: KeynoteText(self: KeynoteEntry) -> str

"""


