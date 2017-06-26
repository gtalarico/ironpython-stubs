class WorksharingSaveAsOptions(object, IDisposable):
    """
    This class contains options specific to worksharing SaveAs.
    
    WorksharingSaveAsOptions()
    """
    def Dispose(self):
        """ Dispose(self: WorksharingSaveAsOptions) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: WorksharingSaveAsOptions, disposing: bool) """
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

    ClearTransmitted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For a transmitted model opened with DetachAndPreserveWorksets,
   clear its transmitted flag in the Save/SaveAs operation.

Get: ClearTransmitted(self: WorksharingSaveAsOptions) -> bool

Set: ClearTransmitted(self: WorksharingSaveAsOptions) = value
"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: WorksharingSaveAsOptions) -> bool

"""

    OpenWorksetsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default set of user-worksets to open when opening the model in the UI.
   Default is AskUserToSpecify.

Get: OpenWorksetsDefault(self: WorksharingSaveAsOptions) -> SimpleWorksetConfiguration

Set: OpenWorksetsDefault(self: WorksharingSaveAsOptions) = value
"""

    SaveAsCentral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to save the new model as a central instead of local model.
   True: save as a central model.
   Default is false: save as a local model.

Get: SaveAsCentral(self: WorksharingSaveAsOptions) -> bool

Set: SaveAsCentral(self: WorksharingSaveAsOptions) = value
"""


