class BasicFileInfo(object, IDisposable):
    """ Encapsulates basic information about a Revit file, including worksharing status, Revit version, username and central path. """
    def Dispose(self):
        """ Dispose(self: BasicFileInfo) """
        pass

    @staticmethod
    def Extract(file):
        """
        Extract(file: str) -> BasicFileInfo
        
            Returns an instance of BasicFileInfo filled with basic information about a 
             Revit file located at the given file-path
        
        
            file: The full path to the file to be queried, including project (.rvt) and family 
             (.rfa) files.
        
            Returns: If successful, basic file data.
        """
        pass

    def GetDocumentVersion(self):
        """
        GetDocumentVersion(self: BasicFileInfo) -> DocumentVersion
        
            Gets the DocumentVersion for the file.
            Returns: The DocumentVersion for the file.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: BasicFileInfo, disposing: bool) """
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

    AllLocalChangesSavedToCentral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Are all local changes saved to the central file?

Get: AllLocalChangesSavedToCentral(self: BasicFileInfo) -> bool

"""

    CentralPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the central model path.

Get: CentralPath(self: BasicFileInfo) -> str

"""

    IsCentral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is workshared and Central.

Get: IsCentral(self: BasicFileInfo) -> bool

"""

    IsCreatedLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is created local.

Get: IsCreatedLocal(self: BasicFileInfo) -> bool

"""

    IsInProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is workshared and is in process of becoming Central.

Get: IsInProgress(self: BasicFileInfo) -> bool

"""

    IsLocal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is workshared and Local.

Get: IsLocal(self: BasicFileInfo) -> bool

"""

    IsSavedInCurrentVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is saved in the current version.

Get: IsSavedInCurrentVersion(self: BasicFileInfo) -> bool

"""

    IsSavedInLaterVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is saved in a later version of Revit than the running Revit.

Get: IsSavedInLaterVersion(self: BasicFileInfo) -> bool

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: BasicFileInfo) -> bool

"""

    IsWorkshared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the file is workshared.

Get: IsWorkshared(self: BasicFileInfo) -> bool

"""

    LanguageWhenSaved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the language active for the last save

Get: LanguageWhenSaved(self: BasicFileInfo) -> LanguageType

"""

    LatestCentralEpisodeGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is the central model's episode GUID corresponding to the last reload latest
   done for this model.

Get: LatestCentralEpisodeGUID(self: BasicFileInfo) -> Guid

"""

    LatestCentralVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This is the central model's version number corresponding to the last reload latest
   done for this model.

Get: LatestCentralVersion(self: BasicFileInfo) -> int

"""

    SavedInVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the version in which file is saved.

Get: SavedInVersion(self: BasicFileInfo) -> str

"""

    Username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the username.

Get: Username(self: BasicFileInfo) -> str

"""


