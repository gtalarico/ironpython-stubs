class VisualStateChangedEventArgs(EventArgs):
    """ Provides data for the System.Windows.VisualStateGroup.CurrentStateChanging and System.Windows.VisualStateGroup.CurrentStateChanged events. """
    Control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the element that is transitioning states.

Get: Control(self: VisualStateChangedEventArgs) -> FrameworkElement

"""

    NewState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state that the element is transitioning to or has transitioned to.

Get: NewState(self: VisualStateChangedEventArgs) -> VisualState

"""

    OldState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the state that the element is transitioning to or has transitioned from.

Get: OldState(self: VisualStateChangedEventArgs) -> VisualState

"""

    StateGroupsRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root element that contains the System.Windows.VisualStateManager.

Get: StateGroupsRoot(self: VisualStateChangedEventArgs) -> FrameworkElement

"""


