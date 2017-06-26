class ElementFilter(object, IDisposable):
    """ A base class for a type of filter that accepts or rejects elements based upon criteria. """
    def Dispose(self):
        """ Dispose(self: ElementFilter) """
        pass

    def PassesFilter(self, *__args):
        """
        PassesFilter(self: ElementFilter, element: Element) -> bool
        
            Applies the filter to a given element.
        
            element: The element.
            Returns: True if the element is accepted by the filter.  False if the element is 
             rejected.
        
        PassesFilter(self: ElementFilter, document: Document, id: ElementId) -> bool
        
            Applies the filter to a given element.
        
            document: The document.
            id: The element id.
            Returns: True if the element is accepted by the filter.  False if the element is 
             rejected.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ElementFilter, disposing: bool) """
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

    Inverted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the results of the filter are inverted; elements that would normally be accepted by this filter will be rejected,
   and elements that would normally be rejected will be accepted.

Get: Inverted(self: ElementFilter) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ElementFilter) -> bool

"""


