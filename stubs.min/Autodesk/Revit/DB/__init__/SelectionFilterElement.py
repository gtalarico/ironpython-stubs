class SelectionFilterElement(FilterElement, IDisposable):
    """
    A filter element that stores an explicit list of ElementIds.
       Only elements whose ElementIds are in this list will pass the filter.
    """
    def AddSet(self, ids):
        """ AddSet(self: SelectionFilterElement, ids: ICollection[ElementId]) """
        pass

    def AddSingle(self, id):
        """
        AddSingle(self: SelectionFilterElement, id: ElementId)
            Adds a single ElementId to the filter's set.
        
            id: The ElementId to add.
        """
        pass

    def Clear(self):
        """
        Clear(self: SelectionFilterElement)
            Removes all ElementIds from the filter.
        """
        pass

    def Contains(self, id):
        """
        Contains(self: SelectionFilterElement, id: ElementId) -> bool
        
            Returns true if the given ElementId is a member of this filter's set.
        
            id: The ElementId to look for.
            Returns: True if the given ElementId is a member of the filter, otherwise false.
        """
        pass

    @staticmethod
    def Create(document, name):
        """
        Create(document: Document, name: str) -> SelectionFilterElement
        
            Creates a new SelectionFilterElement in the given document.
        
            document: The document in which to create the SelectionFilterElement.
            name: The name for the new SelectionFilterElement.
            Returns: The new SelectionFilterElement.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetElementIds(self):
        """
        GetElementIds(self: SelectionFilterElement) -> ICollection[ElementId]
        
            Returns the set of ElementIds contained by this filter.
            Returns: The set of ElementIds.
        """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: SelectionFilterElement) -> bool
        
            Determines whether this filter's set is empty or not.
            Returns: True if the set is empty, otherwise false.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveSet(self, ids):
        """ RemoveSet(self: SelectionFilterElement, ids: ICollection[ElementId]) -> int """
        pass

    def RemoveSingle(self, id):
        """
        RemoveSingle(self: SelectionFilterElement, id: ElementId)
            Removes a single ElementId from the filter's set.
        
            id: The ElementId to remove.
        """
        pass

    def SetElementIds(self, ids):
        """ SetElementIds(self: SelectionFilterElement, ids: ICollection[ElementId]) """
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

