class ElementMulticategoryFilter(ElementQuickFilter, IDisposable):
    """
    A filter used to find elements whose category matches any of a given set of categories.
    
    ElementMulticategoryFilter(categories: ICollection[BuiltInCategory], inverted: bool)
    ElementMulticategoryFilter(categories: ICollection[BuiltInCategory])
    ElementMulticategoryFilter(categoryIds: ICollection[ElementId], inverted: bool)
    ElementMulticategoryFilter(categoryIds: ICollection[ElementId])
    """
    def Dispose(self):
        """ Dispose(self: ElementFilter, A_0: bool) """
        pass

    def GetCategoryIds(self):
        """
        GetCategoryIds(self: ElementMulticategoryFilter) -> ICollection[ElementId]
        
            Gets the category ids assigned to this filter.
            Returns: The category ids.
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, categories: ICollection[BuiltInCategory], inverted: bool)
        __new__(cls: type, categories: ICollection[BuiltInCategory])
        __new__(cls: type, categoryIds: ICollection[ElementId], inverted: bool)
        __new__(cls: type, categoryIds: ICollection[ElementId])
        """
        pass

