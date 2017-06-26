class TransactWithCentralOptions(object, IDisposable):
    """
    Options to customize Revit behavior when accessing the central model.
    
    TransactWithCentralOptions()
    """
    def Dispose(self):
        """ Dispose(self: TransactWithCentralOptions) """
        pass

    def GetLockCallback(self):
        """
        GetLockCallback(self: TransactWithCentralOptions) -> ICentralLockedCallback
        
            Gets the callback object that changes Revit's default behavior of endlessly 
             waiting and repeatedly trying to lock a central model.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TransactWithCentralOptions, disposing: bool) """
        pass

    def SetLockCallback(self, lockCallback):
        """
        SetLockCallback(self: TransactWithCentralOptions, lockCallback: ICentralLockedCallback)
            Sets or resets a callback object that would allow an external application to 
             change Revit's default behavior of endlessly waiting and repeatedly trying to 
             lock a central model.
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

Get: IsValidObject(self: TransactWithCentralOptions) -> bool

"""


