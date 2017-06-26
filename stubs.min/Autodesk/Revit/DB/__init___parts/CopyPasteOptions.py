class CopyPasteOptions(object, IDisposable):
    """
    Settings to control the behavior of a copy-paste operation.
    
    CopyPasteOptions()
    """
    def Dispose(self):
        """ Dispose(self: CopyPasteOptions) """
        pass

    def GetDuplicateTypeNamesHandler(self):
        """
        GetDuplicateTypeNamesHandler(self: CopyPasteOptions) -> IDuplicateTypeNamesHandler
        
            Returns current duplicate type names handler or ll if none is set.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: CopyPasteOptions, disposing: bool) """
        pass

    def SetDuplicateTypeNamesHandler(self, handler):
        """
        SetDuplicateTypeNamesHandler(self: CopyPasteOptions, handler: IDuplicateTypeNamesHandler)
            Sets a custom duplicate type names handler. If this value is not set, the 
             default handler is used.
           By default, Revit displays a modal dialog with 
             options to either copy new types only, or cancel the operation.
        
        
            handler: The duplicate type names handler.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: CopyPasteOptions) -> bool

"""


