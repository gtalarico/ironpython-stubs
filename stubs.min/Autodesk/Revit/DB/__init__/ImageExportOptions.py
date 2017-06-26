class ImageExportOptions(object, IDisposable):
    """
    This class defines options for exporting views and sheets as an image.
    
    ImageExportOptions()
    """
    def Dispose(self):
        """ Dispose(self: ImageExportOptions) """
        pass

    @staticmethod
    def GetFileName(aDoc, dbViewId):
        """
        GetFileName(aDoc: Document, dbViewId: ElementId) -> str
        
            Gets the file name that will be produced when exporting a view to an image.
        
            aDoc: The document that owns the view.
            dbViewId: View which is to be exported as image.
            Returns: The generated exported image file name.
        """
        pass

    def GetViewsAndSheets(self):
        """
        GetViewsAndSheets(self: ImageExportOptions) -> IList[ElementId]
        
            Gets a list of views and sheets to be exported.  Used only when ExportRange is 
             SetOfViews.
        
            Returns: The ids of the views and sheets.
        """
        pass

    @staticmethod
    def IsValidFileName(filePath):
        """
        IsValidFileName(filePath: str) -> bool
        
            Verify if File name is valid
        
            filePath: File path to be tested for valid file name
            Returns: True if File name is valid; false otherwise
        """
        pass

    @staticmethod
    def IsValidForSaveToProjectAsImage(options, doc):
        """
        IsValidForSaveToProjectAsImage(options: ImageExportOptions, doc: Document) -> bool
        
            Verify if ImageExportOptions object is valid for calling saveToProjectAsImage
        
            options: ImageExportOptions object to be validated
            doc: Document for view name verification
            Returns: True if ImageExportOptions object is valid for calling saveToProjectAsImage; 
             false otherwise
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ImageExportOptions, disposing: bool) """
        pass

    def SetViewsAndSheets(self, viewsAndSheets):
        """ SetViewsAndSheets(self: ImageExportOptions, viewsAndSheets: IList[ElementId]) """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ExportRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The export range defining which view(s) will be exported.

Get: ExportRange(self: ImageExportOptions) -> ExportRange

Set: ExportRange(self: ImageExportOptions) = value
"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file name and path for the exported file.

Get: FilePath(self: ImageExportOptions) -> str

Set: FilePath(self: ImageExportOptions) = value
"""

    FitDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fit direction.  Used only if ZoomType is FitToPage.

Get: FitDirection(self: ImageExportOptions) -> FitDirectionType

Set: FitDirection(self: ImageExportOptions) = value
"""

    HLRandWFViewsFileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File type for exported HLR and wireframe views.

Get: HLRandWFViewsFileType(self: ImageExportOptions) -> ImageFileType

Set: HLRandWFViewsFileType(self: ImageExportOptions) = value
"""

    ImageResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image resolution in dots per inch.

Get: ImageResolution(self: ImageExportOptions) -> ImageResolution

Set: ImageResolution(self: ImageExportOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ImageExportOptions) -> bool

"""

    PixelSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pixel size of an image in one direction.  Used only if ZoomType is FitToPage.

Get: PixelSize(self: ImageExportOptions) -> int

Set: PixelSize(self: ImageExportOptions) = value
"""

    ShadowViewsFileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file type for exported shadow views.

Get: ShadowViewsFileType(self: ImageExportOptions) -> ImageFileType

Set: ShadowViewsFileType(self: ImageExportOptions) = value
"""

    ShouldCreateWebSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether or not to create a web site with a page for each export.  Used only when ExportRange is SetOfViews.

Get: ShouldCreateWebSite(self: ImageExportOptions) -> bool

Set: ShouldCreateWebSite(self: ImageExportOptions) = value
"""

    ViewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the view to be created.

Get: ViewName(self: ImageExportOptions) -> str

Set: ViewName(self: ImageExportOptions) = value
"""

    Zoom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value for Zoom (as a percentage).   Used only when ZoomType is Zoom.

Get: Zoom(self: ImageExportOptions) -> int

Set: Zoom(self: ImageExportOptions) = value
"""

    ZoomType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The zoom type, which defines how the image size is determined.

Get: ZoomType(self: ImageExportOptions) -> ZoomFitType

Set: ZoomType(self: ImageExportOptions) = value
"""


