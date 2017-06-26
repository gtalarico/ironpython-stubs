class RebarConstrainedHandle(object, IDisposable):
    """
    A class representing a handle on a Rebar that can be joined to a reference, such
       as a host Element's surface or cover, or another Rebar's handle.
    """
    def Dispose(self):
        """ Dispose(self: RebarConstrainedHandle) """
        pass

    def GetEdgeNumber(self):
        """
        GetEdgeNumber(self: RebarConstrainedHandle) -> int
        
            If the RebarConstrainedHandle's RebarHandleType is 'Edge,'
           then this 
             function will return the number of the edge that is
           driven by the handle.
        """
        pass

    def GetHandleType(self):
        """
        GetHandleType(self: RebarConstrainedHandle) -> RebarHandleType
        
            Returns the RebarHandleType of a RebarConstrainedHandle.
            Returns: The RebarHandleType of the specified RebarConstrainedHandle.
        """
        pass

    def IsEdgeHandle(self):
        """
        IsEdgeHandle(self: RebarConstrainedHandle) -> bool
        
            Returns true if the RebarHandleType of the RebarConstrainedHandle is 'Edge.'
        """
        pass

    def IsValid(self):
        """
        IsValid(self: RebarConstrainedHandle) -> bool
        
            Checks that the RebarConstrainedHandle still has access to valid Rebar handle 
             data
           and that its RebarConstraintsManager is still valid.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarConstrainedHandle, disposing: bool) """
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

Get: IsValidObject(self: RebarConstrainedHandle) -> bool

"""


