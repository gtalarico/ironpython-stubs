class TemporaryViewModes(APIObject, IDisposable):
    """ A data structure containing data related to temporary view modes. """
    def DeactivateAllModes(self):
        """
        DeactivateAllModes(self: TemporaryViewModes)
            Deactivates all temporary modes that are currently active.
        """
        pass

    def DeactivateMode(self, mode):
        """
        DeactivateMode(self: TemporaryViewModes, mode: TemporaryViewMode)
            Deactivates the given temporary mode.
        
            mode: The mode to deactivate
        """
        pass

    def Dispose(self):
        """ Dispose(self: TemporaryViewModes, A_0: bool) """
        pass

    def GetCaption(self, mode):
        """
        GetCaption(self: TemporaryViewModes, mode: TemporaryViewMode) -> str
        
            A text caption to use for the given mode.
        
            mode: The mode to get a caption for.
            Returns: Text of the caption. The text is localized.
        """
        pass

    def IsModeActive(self, mode):
        """
        IsModeActive(self: TemporaryViewModes, mode: TemporaryViewMode) -> bool
        
            Tests whether a given mode is currently active or not.
        
            mode: The mode being tested
        """
        pass

    def IsModeAvailable(self, mode):
        """
        IsModeAvailable(self: TemporaryViewModes, mode: TemporaryViewMode) -> bool
        
            Tests whether a temporary view mode is currently available in the associated 
             view.
        
        
            mode: The mode to evaluate
            Returns: True of the temporary mode is currently available in the associated view.
        """
        pass

    def IsModeEnabled(self, mode):
        """
        IsModeEnabled(self: TemporaryViewModes, mode: TemporaryViewMode) -> bool
        
            Tests whether a temporary view mode is currently enabled in the associated view.
        
            mode: The mode to evaluate
            Returns: True if the requested mode is available and enabled in the associated view; 
             False otherwise.
        """
        pass

    def IsValidState(self, state):
        """
        IsValidState(self: TemporaryViewModes, state: PreviewFamilyVisibilityMode) -> bool
        
            Tests whether the given state is valid for the associated view and the context 
             the view is currently in.
        
        
            state: A state of the PreviewFamilyVisibilityMode
            Returns: Returns True if the state is applicable for the view; False otherwise.
        """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: TemporaryViewModes, disposing: bool)ReleaseUnmanagedResources(self: APIObject) """
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

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: TemporaryViewModes) -> bool

"""

    PreviewFamilyVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state of the PreviewFamilyVisibility mode in the associated view.

Get: PreviewFamilyVisibility(self: TemporaryViewModes) -> PreviewFamilyVisibilityMode

Set: PreviewFamilyVisibility(self: TemporaryViewModes) = value
"""

    RevealConstraints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state of the RevealConstraints mode in the associated view.

Get: RevealConstraints(self: TemporaryViewModes) -> bool

Set: RevealConstraints(self: TemporaryViewModes) = value
"""

    RevealHiddenElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state of the RevealHiddenElements mode in the associated view.

Get: RevealHiddenElements(self: TemporaryViewModes) -> bool

Set: RevealHiddenElements(self: TemporaryViewModes) = value
"""

    WorksharingDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current state of the WorksharingDisplay mode in the associated view.

Get: WorksharingDisplay(self: TemporaryViewModes) -> WorksharingDisplayMode

Set: WorksharingDisplay(self: TemporaryViewModes) = value
"""


    PreviewFamilyVisibilityDefaultOnState = False
    PreviewFamilyVisibilityDefaultUncutState = False

