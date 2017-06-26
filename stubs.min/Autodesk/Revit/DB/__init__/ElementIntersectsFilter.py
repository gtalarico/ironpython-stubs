class ElementIntersectsFilter(ElementSlowFilter, IDisposable):
    """ A base class for filters used to match elements which intersect with geometry. """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    @staticmethod
    def IsCategorySupported(element):
        """
        IsCategorySupported(element: Element) -> bool
        
            Identifies if the input element is of a category supported by element 
             intersection filters.
        
        
            element: The element.
            Returns: True if the element category is supported, false otherwise.
        """
        pass

    @staticmethod
    def IsElementSupported(element):
        """
        IsElementSupported(element: Element) -> bool
        
            Identifies if the input element is supported by element intersection filters.
        
            element: The element.
            Returns: True if the element is supported, false otherwise.
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

