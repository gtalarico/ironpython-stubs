class ImportInstance(Instance, IDisposable):
    """ An element created during either import or link operation in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetVisibility(self):
        """
        GetVisibility(self: ImportInstance) -> FamilyElementVisibility
        
            Gets the visibility for the import instance in a family document.
            Returns: A copy of visibility settings for the import instance in a family document.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetVisibility(self, visibility):
        """
        SetVisibility(self: ImportInstance, visibility: FamilyElementVisibility)
            Sets the visibility for the import instance in a family document.
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

    IsLinked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies whether this instance is a linked object rather than imported one.

Get: IsLinked(self: ImportInstance) -> bool

"""


