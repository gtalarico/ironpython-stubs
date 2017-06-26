class ElementCategoryFilter(ElementQuickFilter, IDisposable):
    """
    A filter used to match elements by their category.
    
    ElementCategoryFilter(category: BuiltInCategory, inverted: bool)
    ElementCategoryFilter(category: BuiltInCategory)
    ElementCategoryFilter(categoryId: ElementId, inverted: bool)
    ElementCategoryFilter(categoryId: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, category: BuiltInCategory, inverted: bool)
        __new__(cls: type, category: BuiltInCategory)
        __new__(cls: type, categoryId: ElementId, inverted: bool)
        __new__(cls: type, categoryId: ElementId)
        """
        pass

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The category id.

Get: CategoryId(self: ElementCategoryFilter) -> ElementId

"""


