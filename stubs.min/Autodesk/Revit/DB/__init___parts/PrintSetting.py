class PrintSetting(Element, IDisposable, IPrintSetting):
    """ Represents the Print Setup (Application Menu->Print->Print Setup) within Autodesk Revit. """
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
    """Returns the Name of Print Setup.

Get: Name(self: PrintSetting) -> str

Set: Name(self: PrintSetting) = value
"""

    PrintParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Parameters of Print Setup.

Get: PrintParameters(self: PrintSetting) -> PrintParameters

"""


