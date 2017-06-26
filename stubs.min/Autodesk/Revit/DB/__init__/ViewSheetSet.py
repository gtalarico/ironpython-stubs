class ViewSheetSet(Element, IDisposable, IViewSheetSet):
    """
    Represents ViewSheetSets stored in a document.
    ViewSheetSets can be stored so that the same printing task can be executed multiple times.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
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

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The view sheet set name.

Get: Name(self: ViewSheetSet) -> str

Set: Name(self: ViewSheetSet) = value
"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The views.

Get: Views(self: ViewSheetSet) -> ViewSet

Set: Views(self: ViewSheetSet) = value
"""


