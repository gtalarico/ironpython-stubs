class FragmentNavigationEventArgs(EventArgs):
    """ Provides data for the FragmentNavigation event. """
    Fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the uniform resource identifier (URI) fragment.

Get: Fragment(self: FragmentNavigationEventArgs) -> str

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the fragment navigation has been handled.

Get: Handled(self: FragmentNavigationEventArgs) -> bool

Set: Handled(self: FragmentNavigationEventArgs) = value
"""

    Navigator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The navigator that raised the System.Windows.Navigation.NavigationService.FragmentNavigation event.

Get: Navigator(self: FragmentNavigationEventArgs) -> object

"""


