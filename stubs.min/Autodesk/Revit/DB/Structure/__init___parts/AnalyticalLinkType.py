class AnalyticalLinkType(ElementType, IDisposable):
    """ An object that specifies the analysis properties for an AnalyticalLink element. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def IsValidAnalyticalFixityState(fixityState):
        """
        IsValidAnalyticalFixityState(fixityState: AnalyticalFixityState) -> bool
        
            Returns whether the input fixity state is valid for Analytical Link Type 
             parameters.
        
        
            fixityState: The fixity state value to check.
            Returns: True if valid.
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

    RotationX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around X.

Get: RotationX(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationX(self: AnalyticalLinkType) = value
"""

    RotationY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around Y.

Get: RotationY(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationY(self: AnalyticalLinkType) = value
"""

    RotationZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of rotation around Z.

Get: RotationZ(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: RotationZ(self: AnalyticalLinkType) = value
"""

    TranslationX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along X.

Get: TranslationX(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationX(self: AnalyticalLinkType) = value
"""

    TranslationY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along Y.

Get: TranslationY(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationY(self: AnalyticalLinkType) = value
"""

    TranslationZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fixity of translation along Z.

Get: TranslationZ(self: AnalyticalLinkType) -> AnalyticalFixityState

Set: TranslationZ(self: AnalyticalLinkType) = value
"""


