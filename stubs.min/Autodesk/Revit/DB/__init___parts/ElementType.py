class ElementType(Element, IDisposable):
    """ Base class for all Types within Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def Duplicate(self, name):
        """
        Duplicate(self: ElementType, name: str) -> ElementType
        
            Duplicates an existing element type and assigns it a new name.
        
            name: The new name of the element type.
            Returns: The duplicated element type.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetPreviewImage(self, size):
        """
        GetPreviewImage(self: ElementType, size: Size) -> Bitmap
        
            Get the preview image of an element. This image is similar to what is seen in 
             the Revit UI when selecting the type of an element.
        
        
            size: The width and height of the preview image in pixels.
            Returns: System::Drawing::Bitmap represents the preview image. ll if there is no preview 
             image.
        """
        pass

    def GetSimilarTypes(self):
        """
        GetSimilarTypes(self: ElementType) -> ICollection[ElementId]
        
            Obtains a set of types that are similar to this type.
            Returns: A set of element IDs of types that are similar to this type.
        """
        pass

    def IsSimilarType(self, typeId):
        """
        IsSimilarType(self: ElementType, typeId: ElementId) -> bool
        
            Checks if given type is similar to this type.
        
            typeId: ElementId of the type to check.
            Returns: True if given type is similar to this type, false otherwise.
        """
        pass

    def IsValidDefaultFamilyType(self, familyCategoryId):
        """
        IsValidDefaultFamilyType(self: ElementType, familyCategoryId: ElementId) -> bool
        
            Identifies if this type is a valid default family type for the given family 
             category id.
        
        
            familyCategoryId: The family category id.
            Returns: True if this type is a valid default family type for the given family category 
             id.
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

    CanBeCopied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine if this ElementType can create a copy

Get: CanBeCopied(self: ElementType) -> bool

"""

    CanBeDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine if this ElementType can be deleted

Get: CanBeDeleted(self: ElementType) -> bool

"""

    CanBeRenamed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine if this ElementType can be renamed

Get: CanBeRenamed(self: ElementType) -> bool

"""

    FamilyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the family name of this element type.

Get: FamilyName(self: ElementType) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set the name for the ElementType.

Set: Name(self: ElementType) = value
"""


