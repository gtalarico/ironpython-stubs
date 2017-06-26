class StartingViewSettings(Element, IDisposable):
    """
    The initial view settings for a document dictate which view will initially be open when this model
       is opened.  These settings are available for all Revit project documents.
    """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    @staticmethod
    def GetStartingViewSettings(doc):
        """
        GetStartingViewSettings(doc: Document) -> StartingViewSettings
        
            Returns the starting view settings for the specified document.
        
            doc: The document to get the settings from, which must be a project document.
            Returns: The starting view settings for the document.
        """
        pass

    def IsAcceptableStartingView(self, viewId):
        """
        IsAcceptableStartingView(self: StartingViewSettings, viewId: ElementId) -> bool
        
            Checks whether the given Id is an acceptable starting view.  InvalidElementId 
             corresponds to "Last Viewed" and is therefore also acceptable.
        
        
            viewId: The Id of the element to check.
            Returns: True if the view is acceptable, False if it is not.
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

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates the specific view that will be opened when the model is loaded.  InvalidElementId indicates
   that no view has been specified.  In that case, Revit will open the last views that were open at the
   time the file was saved.

Get: ViewId(self: StartingViewSettings) -> ElementId

Set: ViewId(self: StartingViewSettings) = value
"""


