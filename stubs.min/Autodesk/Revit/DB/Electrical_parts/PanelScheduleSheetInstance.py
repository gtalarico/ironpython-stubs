class PanelScheduleSheetInstance(Element, IDisposable):
    """ The class represents an instance of a panel schedule placed on sheet. """
    @staticmethod
    def Create(ADoc, scheduleId, DBView):
        """
        Create(ADoc: Document, scheduleId: ElementId, DBView: View) -> PanelScheduleSheetInstance
        
            Creates a new instance of panel schedule on sheet and adds it to the document.
            Returns: The newly created panel schedule sheet instance element.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetSchedule(self):
        """
        GetSchedule(self: PanelScheduleSheetInstance) -> PanelScheduleView
        
            Gets the panel schedule view.
            Returns: The panel schedule view element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SplitSegment(self, iSeg):
        """
        SplitSegment(self: PanelScheduleSheetInstance, iSeg: int) -> bool
        
            Split the panel schedule into
           Thrown if the index is out of bounds.
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

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sheet instance offset in drawing sheet coordinates.

Get: Origin(self: PanelScheduleSheetInstance) -> XYZ

Set: Origin(self: PanelScheduleSheetInstance) = value
"""

    ScheduleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The panel schedule id.

Get: ScheduleId(self: PanelScheduleSheetInstance) -> ElementId

Set: ScheduleId(self: PanelScheduleSheetInstance) = value
"""


