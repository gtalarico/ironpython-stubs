class RevisionSettings(Element, IDisposable):
    """ Provides access to project-wide settings related to revisions. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def GetAlphanumericRevisionSettings(self):
        """
        GetAlphanumericRevisionSettings(self: RevisionSettings) -> AlphanumericRevisionSettings
        
            Returns a copy of the AlphanumericRevisionSettings owned by this 
             RevisionSettings object.
        
            Returns: The copy of the AlphaumericRevisionSettings owned by this RevisionSettings 
             object.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetNumericRevisionSettings(self):
        """
        GetNumericRevisionSettings(self: RevisionSettings) -> NumericRevisionSettings
        
            Returns a copy of the NumericRevisionSettings owned by this RevisionSettings 
             object.
        
            Returns: The copy of the NumericRevisionSettings owned by this RevisionSettings object.
        """
        pass

    @staticmethod
    def GetRevisionSettings(ccda):
        """
        GetRevisionSettings(ccda: Document) -> RevisionSettings
        
            Returns the RevisionSettings for the given project document.
        
            ccda: The document to get the RevisionSettings from.
            Returns: The RevisionSettings for the document.
        """
        pass

    def IsAcceptableRevisionCloudSpacing(self, rawValue):
        """
        IsAcceptableRevisionCloudSpacing(self: RevisionSettings, rawValue: float) -> bool
        
            Rounds the given raw value and checks whether it is an acceptable cloud spacing 
             value after it is rounded.
        
        
            rawValue: The raw value to check.  This value need not be rounded prior to calling this 
             function.
        
            Returns: True if the value will be acceptable after rounding, False otherwise
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    @staticmethod
    def RoundRevisionCloudSpacing(ccda, rawValue):
        """
        RoundRevisionCloudSpacing(ccda: Document, rawValue: float) -> float
        
            Rounds the given revision cloud spacing value according to the document's 
             settings.
        
        
            ccda: The document to use for rounding.
            rawValue: The unrounded value.
            Returns: The rounded revision cloud spacing.
        """
        pass

    def SetAlphanumericRevisionSettings(self, newSettings):
        """
        SetAlphanumericRevisionSettings(self: RevisionSettings, newSettings: AlphanumericRevisionSettings)
            Replaces the current alphanumeric revision numbering settings with the 
             specified AlphanumericRevisionSettings.
        
        
            newSettings: The specified AlphanumericRevisionSettings to be applied to alphanumeric 
             revision numbering.
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetNumericRevisionSettings(self, newSettings):
        """
        SetNumericRevisionSettings(self: RevisionSettings, newSettings: NumericRevisionSettings)
            Replaces the current numeric revision numbering settings with the specified 
             NumericRevisionSettings.
        
        
            newSettings: The specified NumericRevisionSettings to be applied to numeric revision 
             numbering.
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

    RevisionCloudSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines the size in paper space of revision clouds drawn in a project.

Get: RevisionCloudSpacing(self: RevisionSettings) -> float

Set: RevisionCloudSpacing(self: RevisionSettings) = value
"""

    RevisionNumbering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines how the revision number values will display on sheets.

Get: RevisionNumbering(self: RevisionSettings) -> RevisionNumbering

Set: RevisionNumbering(self: RevisionSettings) = value
"""


