class ExportDGNSettings(Element, IDisposable):
    """ This element contains DGN export settings which are saved in a Revit document. """
    @staticmethod
    def Create(document, name, options=None):
        """
        Create(document: Document, name: str) -> ExportDGNSettings
        
            Create a DGN export settings with default values.
        
            document: Document where created settings is saved.
            name: The name specified to this settings.
            Returns: The new DGN export settings instance.
        Create(document: Document, name: str, options: DGNExportOptions) -> ExportDGNSettings
        
            Create DGN export settings with specified values in DGNExportOptions.
        
            document: Document where created settings is saved.
            name: The name specified to this settings.
            options: The options which will be stored in these settings.
            Returns: The new DGN export settings instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetDGNExportOptions(self):
        """
        GetDGNExportOptions(self: ExportDGNSettings) -> DGNExportOptions
        
            Gets the options stored in the these settings.
            Returns: The options.
        """
        pass

    @staticmethod
    def ListNames(aDoc):
        """
        ListNames(aDoc: Document) -> IList[str]
        
            Returns a list of names of dgn export settings.
        
            aDoc: A Revit document to retrieve names from
            Returns: An array of strings representing names of predefined setups.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def SetDGNExportOptions(self, options):
        """
        SetDGNExportOptions(self: ExportDGNSettings, options: DGNExportOptions)
            Sets the options stored in these settings.
        
            options: The options.
        """
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

