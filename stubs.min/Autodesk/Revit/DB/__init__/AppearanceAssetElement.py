class AppearanceAssetElement(Element, IDisposable):
    """ An element that represents an appearance asset for use in composing material definitions. """
    @staticmethod
    def Create(document, name, asset):
        """
        Create(document: Document, name: str, asset: Asset) -> AppearanceAssetElement
        
            Creates a new AppearancAssetElement.
        
            document: The document in which to create the AppearanceAssetElement.
            name: The name of the AppearanceAssetElement.
            asset: The rendering asset of the element.
            Returns: The new AppearanceAssetElement.
           Note that document will own this pointer, 
             you should access it without owning it.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    @staticmethod
    def GetAppearanceAssetElementByName(doc, name):
        """
        GetAppearanceAssetElementByName(doc: Document, name: str) -> AppearanceAssetElement
        
            Gets an AppearanceAssetElement by name.
        
            doc: Document containing the AppearanceAssetElement.
            name: Name of the AppearanceAssetElement.
        """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetRenderingAsset(self):
        """
        GetRenderingAsset(self: AppearanceAssetElement) -> Asset
        
            Gets the rendering asset for the appearance asset element.
            Returns: The rendering asset held by this appearance asset element.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetRenderingAsset(self, asset):
        """
        SetRenderingAsset(self: AppearanceAssetElement, asset: Asset)
            Sets the rendering asset for the appearance asset element.
        
            asset: The new rendering asset.It should be an appearance asset.
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

