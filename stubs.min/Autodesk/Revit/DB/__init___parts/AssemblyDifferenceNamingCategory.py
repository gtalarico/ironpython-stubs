class AssemblyDifferenceNamingCategory(AssemblyDifference, IDisposable):
    """ The two assemblies being compared have different naming categories """
    def Dispose(self):
        """ Dispose(self: AssemblyDifference, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssemblyDifference, disposing: bool) """
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

    NamingCategoryId1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Naming category id of the first assembly

Get: NamingCategoryId1(self: AssemblyDifferenceNamingCategory) -> ElementId

"""

    NamingCategoryId2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Naming category id of the second assembly

Get: NamingCategoryId2(self: AssemblyDifferenceNamingCategory) -> ElementId

"""


