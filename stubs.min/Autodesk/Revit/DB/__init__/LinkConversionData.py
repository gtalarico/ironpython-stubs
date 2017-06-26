class LinkConversionData(object, IDisposable):
    """
    This class contains the information necessary to re-create a Revit document
       from an external source.
    """
    def Dispose(self):
        """ Dispose(self: LinkConversionData) """
        pass

    def GetOptions(self):
        """
        GetOptions(self: LinkConversionData) -> IDictionary[str, str]
        
            Extra information used during the creation of the Revit document.
            Returns: The extra information used during the creation of the Revit document.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: LinkConversionData, disposing: bool) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: LinkConversionData) -> bool

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the source data used to generate the model.

Get: Path(self: LinkConversionData) -> str

"""

    ServerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The service responsible for converting the data into a Revit file.

Get: ServerId(self: LinkConversionData) -> Guid

"""


