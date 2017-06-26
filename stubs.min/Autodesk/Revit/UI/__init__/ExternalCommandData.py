class ExternalCommandData(APIObject, IDisposable):
    """ A class contains reference to Application and View which are needed by external command. """
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

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the current Application for 
external command.

Get: Application(self: ExternalCommandData) -> UIApplication

Set: Application(self: ExternalCommandData) = value
"""

    JournalData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A data map that can be used to read and write data to the Autodesk Revit journal file.

Get: JournalData(self: ExternalCommandData) -> IDictionary[str, str]

Set: JournalData(self: ExternalCommandData) = value
"""

    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieves an object that represents the View external command work on.

Get: View(self: ExternalCommandData) -> View

Set: View(self: ExternalCommandData) = value
"""


