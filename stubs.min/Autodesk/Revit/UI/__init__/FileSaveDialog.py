class FileSaveDialog(FileDialog, IDisposable):
    """
    This class allows an add-in to prompt the user with the Revit dialog used to navigate to and select an existing
       or new file path.  This dialog is typically used to enter a file name for saving or exporting.
    
    FileSaveDialog(filter: str)
    """
    def Dispose(self):
        """ Dispose(self: FileDialog, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FileDialog, disposing: bool) """
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
    def __new__(self, filter):
        """ __new__(cls: type, filter: str) """
        pass

    InitialFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The initial file name to be shown for this save operation.

Get: InitialFileName(self: FileSaveDialog) -> str

Set: InitialFileName(self: FileSaveDialog) = value
"""


