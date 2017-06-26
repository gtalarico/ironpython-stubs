class MultiReferenceAnnotationType(ElementType, IDisposable):
    """ The type for MultiReferenceAnnotation. """
    @staticmethod
    def CreateDefault(document):
        """
        CreateDefault(document: Document) -> MultiReferenceAnnotationType
        
            Creates the first MultiReferenceAnnotationType element and adds it to the 
             document.
        
        
            document: The document to be modified.
            Returns: The new MultiReferenceAnnotationType element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAllowedTagCategory(self):
        """
        GetAllowedTagCategory(self: MultiReferenceAnnotationType) -> ElementId
        
            Returns the category ID for the tag types which can be used by this 
             multi-reference annotation type.
        
            Returns: The allowed tag category ID.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def IsAllowedDimensionStyle(self, dimensionStyleId):
        """
        IsAllowedDimensionStyle(self: MultiReferenceAnnotationType, dimensionStyleId: ElementId) -> bool
        
            Checks if the dimension style can be used with multi-reference annotations.
        
            dimensionStyleId: The dimension style to check.
            Returns: True if the dimension style can be used by multi-reference annotations.
        """
        pass

    def IsAllowedReferenceCategory(self, referenceCategoryId):
        """
        IsAllowedReferenceCategory(self: MultiReferenceAnnotationType, referenceCategoryId: ElementId) -> bool
        
            Checks if the reference category can be used with multi-reference annotations.
        
            referenceCategoryId: The reference category to check.
            Returns: True when the reference category can be used by multi-reference annotations.
        """
        pass

    @staticmethod
    def IsAllowedTagCategory(tagCategoryId):
        """
        IsAllowedTagCategory(tagCategoryId: ElementId) -> bool
        
            Returns true if tag types belonging to this category can be used with 
             multi-reference annotation types.
        
        
            tagCategoryId: The tag category to test.
        """
        pass

    def IsAllowedTagType(self, tagTypeId):
        """
        IsAllowedTagType(self: MultiReferenceAnnotationType, tagTypeId: ElementId) -> bool
        
            Checks if the tag type can be assigned to this multi-reference annotation type.
        
            tagTypeId: The tag type to test.
            Returns: True if the tag type exclusively tags elements from the multi-reference 
             annotation's reference category.
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

    DimensionStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The dimension style which will be used by the child dimension of the multi-reference annotation.

Get: DimensionStyleId(self: MultiReferenceAnnotationType) -> ElementId

Set: DimensionStyleId(self: MultiReferenceAnnotationType) = value
"""

    GroupTagHeads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls if parameter values for the annotation's references will be reported in one grouped tag head
   or if every reference will get its own tag head.

Get: GroupTagHeads(self: MultiReferenceAnnotationType) -> bool

Set: GroupTagHeads(self: MultiReferenceAnnotationType) = value
"""

    ReferenceCategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category of elements to which this annotation applies.

Get: ReferenceCategoryId(self: MultiReferenceAnnotationType) -> ElementId

"""

    ShowDimensionText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls if text from the multi-reference annotation's dimension will be shown.

Get: ShowDimensionText(self: MultiReferenceAnnotationType) -> bool

Set: ShowDimensionText(self: MultiReferenceAnnotationType) = value
"""

    TagTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The tag type which will be used by the child tag the multi-reference annotation.

Get: TagTypeId(self: MultiReferenceAnnotationType) -> ElementId

Set: TagTypeId(self: MultiReferenceAnnotationType) = value
"""


