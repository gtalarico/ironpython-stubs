class RevisionCloud(Element, IDisposable):
    """ A RevisionCloud is a graphical "cloud" that can be displayed on a view or sheet to indicate where revisions in the model have occurred. """
    @staticmethod
    def Create(document, view, revisionId, curves):
        """ Create(document: Document, view: View, revisionId: ElementId, curves: IList[Curve]) -> RevisionCloud """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetSheetIds(self):
        """
        GetSheetIds(self: RevisionCloud) -> ISet[ElementId]
        
            Returns the ids of the ViewSheets where this RevisionCloud may appear and 
             contribute to the sheet's revision schedule.
        
            Returns: The ids of the ViewSheets where this RevisionCloud may appear.
        """
        pass

    def GetSketchCurves(self):
        """
        GetSketchCurves(self: RevisionCloud) -> IList[Curve]
        
            Returns copies of the Curves that form this RevisionCloud.
            Returns: Copies of the sketched curves that form this RevisionCloud.
        """
        pass

    def IsRevisionIssued(self):
        """
        IsRevisionIssued(self: RevisionCloud) -> bool
        
            Indicates whether the Revision associated with this RevisionCloud has been 
             issued.
        
            Returns: True if the Revision has been issued, False otherwise.
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

    RevisionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Revision associated with this RevisionCloud.

Get: RevisionId(self: RevisionCloud) -> ElementId

Set: RevisionId(self: RevisionCloud) = value
"""


