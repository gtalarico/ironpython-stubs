class Settings(APIObject, IDisposable):
    """
    The settings object provides access to general components of the Autodesk Revit
    application, such as Categories.
    """
    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
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

    Categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that provides access to all the categories contained in the Autodesk
Revit application and project.

Get: Categories(self: Settings) -> Categories

"""

    ElectricalSetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that provides access to all the electrical settings include voltage type, distribution system type,
demand factor, wire type in the Autodesk Revit application and project.

Get: ElectricalSetting(self: Settings) -> ElectricalSetting

"""

    TilePatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that provides access to the TilePattern objects in
the document.

Get: TilePatterns(self: Settings) -> TilePatterns

"""


