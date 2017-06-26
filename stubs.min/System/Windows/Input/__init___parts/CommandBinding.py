class CommandBinding(object):
 """
 Binds a System.Windows.Input.RoutedCommand to the event handlers that implement the command.
 
 CommandBinding()
 CommandBinding(command: ICommand)
 CommandBinding(command: ICommand,executed: ExecutedRoutedEventHandler)
 CommandBinding(command: ICommand,executed: ExecutedRoutedEventHandler,canExecute: CanExecuteRoutedEventHandler)
 """
 @staticmethod
 def __new__(self,command=None,executed=None,canExecute=None):
  """
  __new__(cls: type)
  __new__(cls: type,command: ICommand)
  __new__(cls: type,command: ICommand,executed: ExecutedRoutedEventHandler)
  __new__(cls: type,command: ICommand,executed: ExecutedRoutedEventHandler,canExecute: CanExecuteRoutedEventHandler)
  """
  pass
 Command=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Input.ICommand associated with this System.Windows.Input.CommandBinding.

Get: Command(self: CommandBinding) -> ICommand

Set: Command(self: CommandBinding)=value
"""


 CanExecute=None
 Executed=None
 PreviewCanExecute=None
 PreviewExecuted=None

