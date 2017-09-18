class ExecutedRoutedEventArgs(RoutedEventArgs):
 """ Provides data for the System.Windows.Input.CommandManager.Executed and System.Windows.Input.CommandManager.PreviewExecuted�routed events. """
 Command=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the command that was invoked.

Get: Command(self: ExecutedRoutedEventArgs) -> ICommand

"""

 Parameter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets data parameter of the command.

Get: Parameter(self: ExecutedRoutedEventArgs) -> object

"""


