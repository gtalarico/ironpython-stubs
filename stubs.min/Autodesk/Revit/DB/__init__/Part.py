class Part(Element, IDisposable):
    """ This element represents a part of another element. """
    def CanOffsetFace(self, face):
        """
        CanOffsetFace(self: Part, face: Face) -> bool
        
            Checks if it is possible to offset the given face.
        
            face: face to be checked.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetSourceElementIds(self):
        """
        GetSourceElementIds(self: Part) -> ICollection[LinkElementId]
        
            Gets a collection of elements from which this Part is created by the PartMaker.
             
           May return more than one source only if there is merge involved somewhere 
             in the history of this Part.
        
            Returns: The collection of elements
        """
        pass

    def GetSourceElementOriginalCategoryIds(self):
        """
        GetSourceElementOriginalCategoryIds(self: Part) -> ICollection[ElementId]
        
            Gets the category ids of the source elements which were used to form this part.
            Returns: The category ids.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def ResetPartShape(self):
        """
        ResetPartShape(self: Part)
            Resets all face offsets applied to part faces.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetFaceOffset(self, face, offset):
        """
        SetFaceOffset(self: Part, face: Face, offset: float)
            Offsets the given part face in the direction that points out of the solid shape 
             with the specified amount.
           Negative value will offset the face into the 
             solid shape.
        
        
            face: The face to offset.
            offset: The magnitude of the offset.
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

    Excluded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the part is excluded, false otherwise

Get: Excluded(self: Part) -> bool

Set: Excluded(self: Part) = value
"""

    OriginalCategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category Id of the original element corresponding to this Part.

Get: OriginalCategoryId(self: Part) -> ElementId

Set: OriginalCategoryId(self: Part) = value
"""

    PartMaker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PartMaker that created this Part.

Get: PartMaker(self: Part) -> PartMaker

"""


