class CustomContentState(object):
    """ System.Windows.Navigation.CustomContentState enables the ability to navigate through different states of a single piece of source content without reloading the source content for each subsequent navigation. """
    def Replay(self, navigationService, mode):
        """
        Replay(self: CustomContentState, navigationService: NavigationService, mode: NavigationMode)
            Called to reapply state to a piece of content when navigation occurs.
        
            navigationService: The System.Windows.Navigation.NavigationService owned by the navigator responsible for the content to which this System.Windows.Navigation.CustomContentState is being applied.
            mode: A System.Windows.Navigation.NavigationMode that specifies how the content to which the System.Windows.Navigation.CustomContentState is being applied was navigated to.
        """
        pass

    JournalEntryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name for the content that is stored in navigation history. The value of System.Windows.Navigation.CustomContentState.JournalEntryName is displayed from System.Windows.Navigation.NavigationWindow, System.Windows.Controls.Frame, and Windows Internet Explorer 7 navigation UI.

Get: JournalEntryName(self: CustomContentState) -> str

"""


