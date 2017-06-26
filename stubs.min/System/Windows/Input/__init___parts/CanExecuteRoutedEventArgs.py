class CanExecuteRoutedEventArgs(RoutedEventArgs):
    """ Provides data for the System.Windows.Input.CommandBinding.CanExecute and System.Windows.Input.CommandManager.PreviewCanExecute�routed events. """
    CanExecute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value that indicates whether the System.Windows.Input.RoutedCommand associated with this event can be executed on the command target.

Get: CanExecute(self: CanExecuteRoutedEventArgs) -> bool

Set: CanExecute(self: CanExecuteRoutedEventArgs) = value
"""

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command associated with this event.

Get: Command(self: CanExecuteRoutedEventArgs) -> ICommand

"""

    ContinueRouting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines whether the input routed event that invoked the command should continue to route through the element tree.

Get: ContinueRouting(self: CanExecuteRoutedEventArgs) -> bool

Set: ContinueRouting(self: CanExecuteRoutedEventArgs) = value
"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the command specific data.

Get: Parameter(self: CanExecuteRoutedEventArgs) -> object

"""


