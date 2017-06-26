class DocumentPage(object, IDisposable):
    """
    Represents a document page produced by a paginator.
    
    DocumentPage(visual: Visual)
    DocumentPage(visual: Visual, pageSize: Size, bleedBox: Rect, contentBox: Rect)
    """
    def Dispose(self):
        """
        Dispose(self: DocumentPage)
            Releases all resources used by the System.Windows.Documents.DocumentPage.
        """
        pass

    def OnPageDestroyed(self, *args): #cannot find CLR method
        """
        OnPageDestroyed(self: DocumentPage, e: EventArgs)
            Raises the System.Windows.Documents.DocumentPage.PageDestroyed event.
        
            e: An System.EventArgs that contains the event data.
        """
        pass

    def SetBleedBox(self, *args): #cannot find CLR method
        """
        SetBleedBox(self: DocumentPage, bleedBox: Rect)
            Sets the dimensions and location of the System.Windows.Documents.DocumentPage.BleedBox.
        
            bleedBox: An object that specifies the size and location of a rectangle.
        """
        pass

    def SetContentBox(self, *args): #cannot find CLR method
        """
        SetContentBox(self: DocumentPage, contentBox: Rect)
            Sets the dimension and location of the System.Windows.Documents.DocumentPage.ContentBox.
        
            contentBox: An object that specifies the size and location of a rectangle.
        """
        pass

    def SetSize(self, *args): #cannot find CLR method
        """
        SetSize(self: DocumentPage, size: Size)
            Sets the System.Windows.Documents.DocumentPage.Size of the physical page as it will be after any cropping.
        
            size: The size of the page.
        """
        pass

    def SetVisual(self, *args): #cannot find CLR method
        """
        SetVisual(self: DocumentPage, visual: Visual)
            Sets the System.Windows.Documents.DocumentPage.Visual that depicts the page.
        
            visual: The visual representation of the page.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visual, pageSize=None, bleedBox=None, contentBox=None):
        """
        __new__(cls: type, visual: Visual)
        __new__(cls: type, visual: Visual, pageSize: Size, bleedBox: Rect, contentBox: Rect)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BleedBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the area for print production-related bleeds, registration marks, and crop marks that may appear on the physical sheet outside the logical page boundaries.

Get: BleedBox(self: DocumentPage) -> Rect

"""

    ContentBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the area of the page within the margins.

Get: ContentBox(self: DocumentPage) -> Rect

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the actual size of a page as it will be following any cropping.

Get: Size(self: DocumentPage) -> Size

"""

    Visual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """When overridden in a derived class, gets the visual representation of the page.

Get: Visual(self: DocumentPage) -> Visual

"""


    Missing = None
    PageDestroyed = None

