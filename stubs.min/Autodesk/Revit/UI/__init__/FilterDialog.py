class FilterDialog(object, IDisposable):
    """
    Allows display of the dialog used to create and edit FilterElements in Autodesk Revit.
    
    FilterDialog(doc: Document, name: str)
    FilterDialog(doc: Document, filterToSelect: ElementId)
    """
    def Dispose(self):
        """ Dispose(self: FilterDialog) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilterDialog, disposing: bool) """
        pass

    def Show(self):
        """
        Show(self: FilterDialog)
            Shows the FilterDialog editing dialog to the user.
        """
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
    def __new__(self, doc, *__args):
        """
        __new__(cls: type, doc: Document, name: str)
        __new__(cls: type, doc: Document, filterToSelect: ElementId)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    FilterToSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filter element to be selected once Show is invoked.

Get: FilterToSelect(self: FilterDialog) -> ElementId

Set: FilterToSelect(self: FilterDialog) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilterDialog) -> bool

"""

    NewFilterId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElementId of the new filter created.
   The value is populated after Show method is executed.

Get: NewFilterId(self: FilterDialog) -> ElementId

"""

    NewFilterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the new ParameterFilterElement to be created and selected once Show is invoked.

Get: NewFilterName(self: FilterDialog) -> str

Set: NewFilterName(self: FilterDialog) = value
"""


