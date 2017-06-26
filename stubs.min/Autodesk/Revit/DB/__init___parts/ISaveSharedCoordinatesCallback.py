class ISaveSharedCoordinatesCallback:
    """
    An interface that may be used to control Revit when trying to unload
       or reload a Revit link with changes in shared coordinates.
    """
    def GetSaveModifiedLinksOption(self, link):
        """
        GetSaveModifiedLinksOption(self: ISaveSharedCoordinatesCallback, link: RevitLinkType) -> SaveModifiedLinksOptions
        
            Determines whether Revit should save the link, not save the link,
           or 
             discard shared positioning entirely.
        
        
            link: The Revit link which has modified shared coordinates.
            Returns: The options when saving a linked file which has been modified
           in-memory by 
             shared coordinates operations.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

