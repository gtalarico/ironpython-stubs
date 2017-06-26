class RebarHookType(ElementType, IDisposable):
    """ A Rebar Hook type object that is used in the generation of Rebar. """
    @staticmethod
    def Create(doc, angle, multiplier):
        """
        Create(doc: Document, angle: float, multiplier: float) -> RebarHookType
        
            Creates a new RebarHookType in a document.
        
            angle: Determine the hook angle of new RebarHookType.
            multiplier: Determine the straight line multiplier of new RebarHookType.
        """
        pass

    @staticmethod
    def CreateDefaultRebarHookType(ADoc):
        """
        CreateDefaultRebarHookType(ADoc: Document) -> ElementId
        
            Creates a new RebarHookType object with a default name.
        
            ADoc: The document.
            Returns: The newly created type id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetDefaultHookExtension(self, barDiameter):
        """
        GetDefaultHookExtension(self: RebarHookType, barDiameter: float) -> float
        
            Computes the default hook length, which is equal to barDiameter * multiplier.
        """
        pass

    def GetHookExtensionLength(self, barType):
        """
        GetHookExtensionLength(self: RebarHookType, barType: RebarBarType) -> float
        
            Computes the hook extension length based on current hook length
        """
        pass

    def IsOffsetLengthRequired(self):
        """
        IsOffsetLengthRequired(self: RebarHookType) -> bool
        
            Check whether hook offset length is required.
           remarks: If hook angle is no 
             more than 90 degree, hook offset length is not meaningful.
           returns: True if 
             hook offset length is required, otherwise false.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    HookAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hook angle, measured in radians. Must be greater than 0 and no more than pi.

Get: HookAngle(self: RebarHookType) -> float

Set: HookAngle(self: RebarHookType) = value
"""

    StraightLineMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Multiplier of bar diameter. Used to compute a default hook length.
   The default hook length can be overridden by the RebarBarType class.

Get: StraightLineMultiplier(self: RebarHookType) -> float

Set: StraightLineMultiplier(self: RebarHookType) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The hook may only be applied to shapes of the specified style.

Get: Style(self: RebarHookType) -> RebarStyle

Set: Style(self: RebarHookType) = value
"""


