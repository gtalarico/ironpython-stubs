class IContentHost:
    """ This interface is implemented by layouts which host System.Windows.ContentElement. """
    def GetRectangles(self, child):
        """
        GetRectangles(self: IContentHost, child: ContentElement) -> ReadOnlyCollection[Rect]
        
            Returns a collection of bounding rectangles for a child element.
        
            child: The child element that the bounding rectangles are returned for.
            Returns: A collection of bounding rectangles for a child element.
        """
        pass

    def InputHitTest(self, point):
        """
        InputHitTest(self: IContentHost, point: Point) -> IInputElement
        
            Performs hit-testing for child elements.
        
            point: Mouse coordinates relative to the ContentHost.
            Returns: A descendant of System.Windows.IInputElement, or NULL if no such element exists.
        """
        pass

    def OnChildDesiredSizeChanged(self, child):
        """
        OnChildDesiredSizeChanged(self: IContentHost, child: UIElement)
            Called when a System.Windows.UIElement-derived class which is hosted by a System.Windows.IContentHost changes its System.Windows.UIElement.DesiredSize.
        
            child: Child element whose System.Windows.UIElement.DesiredSize has changed
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    HostedElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumeration containing all descendant System.Windows.ContentElement-derived classes, as well as all System.Windows.UIElement-derived classes that are a direct descendant of the System.Windows.IContentHost or one of its descendant System.Windows.ContentElement classes.

Get: HostedElements(self: IContentHost) -> IEnumerator[IInputElement]

"""


