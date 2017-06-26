class FilterCategoryRule(FilterRule, IDisposable):
    """
    A filter rule that matches elements of a set of categories.
    
    FilterCategoryRule(categories: ICollection[ElementId])
    """
    @staticmethod
    def AllCategoriesFilterable(categories):
        """ AllCategoriesFilterable(categories: ICollection[ElementId]) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: FilterRule, A_0: bool) """
        pass

    def GetCategories(self):
        """
        GetCategories(self: FilterCategoryRule) -> ICollection[ElementId]
        
            Gets the rule's categories.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterRule, disposing: bool) """
        pass

    def SetCategories(self, categories):
        """ SetCategories(self: FilterCategoryRule, categories: ICollection[ElementId]) -> bool """
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
    def __new__(self, categories):
        """ __new__(cls: type, categories: ICollection[ElementId]) """
        pass

