class AssemblyMemberDifferentCategory(AssemblyMemberDifference, IDisposable):
    """ The two assembly members being compared have different category """
    def Dispose(self):
        """ Dispose(self: AssemblyMemberDifference, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: AssemblyMemberDifference, disposing: bool) """
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

    CategoryId1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Category id of the first assembly member

Get: CategoryId1(self: AssemblyMemberDifferentCategory) -> ElementId

"""

    CategoryId2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Category id of the second assembly member

Get: CategoryId2(self: AssemblyMemberDifferentCategory) -> ElementId

"""


