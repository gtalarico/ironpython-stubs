class ValueAtPointBase(object, IDisposable):
    """ A base class representing storage of values at a given point. """
    def ClearAllFlags(self):
        """
        ClearAllFlags(self: ValueAtPointBase)
            Sets flags for all measurements to ValueAtPointFlags::None.
        """
        pass

    def ClearFlagsAt(self, measurement):
        """
        ClearFlagsAt(self: ValueAtPointBase, measurement: int)
            Sets flags for the given measurement to ValueAtPointFlags::None.
        
            measurement: Measurement for which to clear flags.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ValueAtPointBase) """
        pass

    def GetFlags(self, measurement):
        """
        GetFlags(self: ValueAtPointBase, measurement: int) -> int
        
            Returns flags for the given measurement.
        
            measurement: Measurement number for which flags are returned.
            Returns: Flags value for the measurement.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ValueAtPointBase, disposing: bool) """
        pass

    def SetFlags(self, flags, measurement=None):
        """
        SetFlags(self: ValueAtPointBase, flags: IList[int])SetFlags(self: ValueAtPointBase, flags: int)
            Sets the flags associated to all measurements to the same value.
        
            flags: Value of flags, uniform for all measurements.
           Flags values are defined in 
             the enumerated class ValueAtPointFlags and are combined into the int value.
        
        SetFlags(self: ValueAtPointBase, flags: int, measurement: int)
            Sets the flags associated to a given measurement.
        
            flags: The value of the flags to set.
           Flags values are defined in the enumerated 
             class ValueAtPointFlags and are combined into the int value.
        
            measurement: Measurement for which to set flags.
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

Get: IsValidObject(self: ValueAtPointBase) -> bool

"""


