class SelectionUIOptions(object, IDisposable):
    """ Provides access to user settings related to how selection will behave in Revit's UI. """
    def Dispose(self):
        """ Dispose(self: SelectionUIOptions) """
        pass

    @staticmethod
    def ElementSelectsAsPinned(document, element):
        """
        ElementSelectsAsPinned(document: Document, element: Element) -> bool
        
            Checks whether the specified element will be treated as pinned for the purposes 
             of selection.
        
        
            document: The document containing the element.
            element: The element to check.
            Returns: True if the specified element should be treated as pinned for selection 
             purposes, false otherwise.
        """
        pass

    @staticmethod
    def GetSelectionUIOptions():
        """
        GetSelectionUIOptions() -> SelectionUIOptions
        
            Returns the current user's SelectionOptions.
            Returns: The SelectionOptions for the current user.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SelectionUIOptions, disposing: bool) """
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

    DragOnSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements can be dragged immediately when they are selected.

Get: DragOnSelection(self: SelectionUIOptions) -> bool

Set: DragOnSelection(self: SelectionUIOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SelectionUIOptions) -> bool

"""

    SelectFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements can be selected by clicking on the interior of a face.

Get: SelectFaces(self: SelectionUIOptions) -> bool

Set: SelectFaces(self: SelectionUIOptions) = value
"""

    SelectLinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether Revit and CAD link instances can be selected.

Get: SelectLinks(self: SelectionUIOptions) -> bool

Set: SelectLinks(self: SelectionUIOptions) = value
"""

    SelectPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether pinned elements can be selected.

Get: SelectPinned(self: SelectionUIOptions) -> bool

Set: SelectPinned(self: SelectionUIOptions) = value
"""

    SelectUnderlay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether elements that are displayed as underlay can be selected.

Get: SelectUnderlay(self: SelectionUIOptions) -> bool

Set: SelectUnderlay(self: SelectionUIOptions) = value
"""


