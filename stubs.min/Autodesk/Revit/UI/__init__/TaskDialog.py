class TaskDialog(APIObject, IDisposable):
    """
    A task dialog is a dialog box that can be used to display information and receive simple input from the user. It has a common set of controls  
    that are arranged in a standard order to assure consistent look and feel.
    
    TaskDialog(title: str)
    """
    def AddCommandLink(self, id, mainContent, supportingContent=None):
        """
        AddCommandLink(self: TaskDialog, id: TaskDialogCommandLinkId, mainContent: str, supportingContent: str)
            Adds a CommandLink associated to the given id, displaying the indicating main 
             and supporting content.
        
        
            id: The id of the CommandLink. This corresponds to the value returned by Show() 
             when the link is chosen by the user.
        
            mainContent: The main content of the CommandLink.
            supportingContent: The main content of the CommandLink.
        AddCommandLink(self: TaskDialog, id: TaskDialogCommandLinkId, mainContent: str)
            Adds a CommandLink associated to the given id, displaying the indicating main 
             content.
        
        
            id: The id of the CommandLink. This corresponds to the value returned by Show() 
             when the link is chosen by the user.
        
            mainContent: The main content of the CommandLink.
        """
        pass

    def Dispose(self):
        """ Dispose(self: APIObject, A_0: bool) """
        pass

    def ReleaseManagedResources(self, *args): #cannot find CLR method
        """ ReleaseManagedResources(self: APIObject) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: APIObject) """
        pass

    @staticmethod
    def Show(title=None, mainInstruction=None, buttons=None, defaultButton=None):
        """
        Show(title: str, mainInstruction: str) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction and a Close button.
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            Returns: The user's response to the task dialog.
        Show(self: TaskDialog) -> TaskDialogResult
        
            Shows the task dialog.
            Returns: The user's response to the task dialog.
        Show(title: str, mainInstruction: str, buttons: TaskDialogCommonButtons, defaultButton: TaskDialogResult) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction, common buttons and default 
             buttons.
        
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            buttons: The common buttons to be shown the task dialog.
            defaultButton: The default button of the task dialog.
            Returns: The user's response to the task dialog.
        Show(title: str, mainInstruction: str, buttons: TaskDialogCommonButtons) -> TaskDialogResult
        
            Shows a task dialog with title, main instruction and common buttons.
        
            title: The title of the task dialog.
            mainInstruction: The main instruction of the task dialog.
            buttons: The common buttons to be shown the task dialog.
            Returns: The user's response to the task dialog.
        """
        pass

    def WasExtraCheckBoxChecked(self):
        """
        WasExtraCheckBoxChecked(self: TaskDialog) -> bool
        
            Gets the status of the extra checkbox.
            Returns: Whether the extra checkbox is checked.
        """
        pass

    def WasVerificationChecked(self):
        """
        WasVerificationChecked(self: TaskDialog) -> bool
        
            Gets the status of the verification checkbox.
            Returns: Whether the verification checkbox is checked.
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
    def __new__(self, title):
        """ __new__(cls: type, title: str) """
        pass

    AllowCancellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the task dialog can be cancelled if no cancel button is specified.

Get: AllowCancellation(self: TaskDialog) -> bool

Set: AllowCancellation(self: TaskDialog) = value
"""

    CommonButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The push buttons displayed in the task dialog.

Get: CommonButtons(self: TaskDialog) -> TaskDialogCommonButtons

Set: CommonButtons(self: TaskDialog) = value
"""

    DefaultButton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The default button for the dialog.

Get: DefaultButton(self: TaskDialog) -> TaskDialogResult

Set: DefaultButton(self: TaskDialog) = value
"""

    ExpandedContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ExpandedContent is hidden by default and will display at the bottom of the task dialog when the "Show details" button is pressed.

Get: ExpandedContent(self: TaskDialog) -> str

Set: ExpandedContent(self: TaskDialog) = value
"""

    ExtraCheckBoxText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ExtraCheckBoxText is used to label the extra checkbox.

Get: ExtraCheckBoxText(self: TaskDialog) -> str

Set: ExtraCheckBoxText(self: TaskDialog) = value
"""

    FooterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """FooterText is used in the footer area of the task dialog.

Get: FooterText(self: TaskDialog) -> str

Set: FooterText(self: TaskDialog) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Id of the task dialog.

Get: Id(self: TaskDialog) -> str

Set: Id(self: TaskDialog) = value
"""

    MainContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """MainContent is the smaller text that appears just below the main instructions.

Get: MainContent(self: TaskDialog) -> str

Set: MainContent(self: TaskDialog) = value
"""

    MainIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The icon shown in the task dialog.

Get: MainIcon(self: TaskDialog) -> TaskDialogIcon

Set: MainIcon(self: TaskDialog) = value
"""

    MainInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The large primary text that appears at the top of a task dialog.

Get: MainInstruction(self: TaskDialog) -> str

Set: MainInstruction(self: TaskDialog) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Title of the task dialog.

Get: Title(self: TaskDialog) -> str

Set: Title(self: TaskDialog) = value
"""

    TitleAutoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the TaskDialog's title will automatically have the add-in name added as a prefix.

Get: TitleAutoPrefix(self: TaskDialog) -> bool

Set: TitleAutoPrefix(self: TaskDialog) = value
"""

    VerificationText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """VerificationText is used to label the verification checkbox.

Get: VerificationText(self: TaskDialog) -> str

Set: VerificationText(self: TaskDialog) = value
"""


