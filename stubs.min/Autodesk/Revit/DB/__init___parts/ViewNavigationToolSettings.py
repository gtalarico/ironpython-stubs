class ViewNavigationToolSettings(Element, IDisposable):
    """ Represents the settings contained in the document associated to the View Navigation tools (such as the View Cube). """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetHomeCamera(self):
        """
        GetHomeCamera(self: ViewNavigationToolSettings) -> HomeCamera
        
            Gets a copy of the structure containing information about the store Home view 
             orientation.
        
            Returns: A copy of the structure containing information about the store Home view 
             orientation, or
           ll if there is no home view set for this document.
        """
        pass

    @staticmethod
    def GetViewNavigationToolSettings(pADoc):
        """
        GetViewNavigationToolSettings(pADoc: Document) -> ViewNavigationToolSettings
        
            Gets the instance of the settings for the given document.
        
            pADoc: The document.
            Returns: The instance of the settings for the given document.
        """
        pass

    def IsHomeCameraSet(self):
        """
        IsHomeCameraSet(self: ViewNavigationToolSettings) -> bool
        
            Checks if the home view is set in the settings.
            Returns: Returns true if home view is set, otherwise false.
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

