class CommandManager(object):
 """ Provides command related utility methods that register System.Windows.Input.CommandBinding and System.Windows.Input.InputBinding objects for class owners and commands,add and remove command event handlers,and provides services for querying the status of a command. """
 @staticmethod
 def AddCanExecuteHandler(element,handler):
  """
  AddCanExecuteHandler(element: UIElement,handler: CanExecuteRoutedEventHandler)
   Attaches the specified System.Windows.Input.CanExecuteRoutedEventHandler to the 
    specified element.
  
  
   element: The element to attach handler to.
   handler: The can execute handler.
  """
  pass
 @staticmethod
 def AddExecutedHandler(element,handler):
  """
  AddExecutedHandler(element: UIElement,handler: ExecutedRoutedEventHandler)
   Attaches the specified System.Windows.Input.ExecutedRoutedEventHandler to the 
    specified element.
  
  
   element: The element to attach handler to.
   handler: The executed handler.
  """
  pass
 @staticmethod
 def AddPreviewCanExecuteHandler(element,handler):
  """
  AddPreviewCanExecuteHandler(element: UIElement,handler: CanExecuteRoutedEventHandler)
   Attaches the specified System.Windows.Input.CanExecuteRoutedEventHandler to the 
    specified element.
  
  
   element: The element to attach handler to.
   handler: The can execute handler.
  """
  pass
 @staticmethod
 def AddPreviewExecutedHandler(element,handler):
  """
  AddPreviewExecutedHandler(element: UIElement,handler: ExecutedRoutedEventHandler)
   Attaches the specified System.Windows.Input.ExecutedRoutedEventHandler to the 
    specified element.
  
  
   element: The element to attach handler to.
   handler: The can execute handler.
  """
  pass
 @staticmethod
 def InvalidateRequerySuggested():
  """
  InvalidateRequerySuggested()
   Forces the System.Windows.Input.CommandManager to raise the 
    System.Windows.Input.CommandManager.RequerySuggested event.
  """
  pass
 @staticmethod
 def RegisterClassCommandBinding(type,commandBinding):
  """
  RegisterClassCommandBinding(type: Type,commandBinding: CommandBinding)
   Registers a System.Windows.Input.CommandBinding with the specified type.
  
   type: The class with which to register commandBinding.
   commandBinding: The command binding to register.
  """
  pass
 @staticmethod
 def RegisterClassInputBinding(type,inputBinding):
  """
  RegisterClassInputBinding(type: Type,inputBinding: InputBinding)
   Registers the specified System.Windows.Input.InputBinding with the specified 
    type.
  
  
   type: The type to register inputBinding with.
   inputBinding: The input binding to register.
  """
  pass
 @staticmethod
 def RemoveCanExecuteHandler(element,handler):
  """
  RemoveCanExecuteHandler(element: UIElement,handler: CanExecuteRoutedEventHandler)
   Detaches the specified System.Windows.Input.CanExecuteRoutedEventHandler from 
    the specified element.
  
  
   element: The element to remove handler from.
   handler: The can execute handler.
  """
  pass
 @staticmethod
 def RemoveExecutedHandler(element,handler):
  """
  RemoveExecutedHandler(element: UIElement,handler: ExecutedRoutedEventHandler)
   Detaches the specified System.Windows.Input.ExecutedRoutedEventHandler from the 
    specified element.
  
  
   element: The element to remove handler from.
   handler: The executed handler.
  """
  pass
 @staticmethod
 def RemovePreviewCanExecuteHandler(element,handler):
  """
  RemovePreviewCanExecuteHandler(element: UIElement,handler: CanExecuteRoutedEventHandler)
   Detaches the specified System.Windows.Input.CanExecuteRoutedEventHandler from 
    the specified element.
  
  
   element: The element to remove handler from.
   handler: The can execute handler.
  """
  pass
 @staticmethod
 def RemovePreviewExecutedHandler(element,handler):
  """
  RemovePreviewExecutedHandler(element: UIElement,handler: ExecutedRoutedEventHandler)
   Detaches the specified System.Windows.Input.ExecutedRoutedEventHandler from the 
    specified element.
  
  
   element: The element to remove handler from.
   handler: The executed handler.
  """
  pass
 CanExecuteEvent=None
 ExecutedEvent=None
 PreviewCanExecuteEvent=None
 PreviewExecutedEvent=None
 RequerySuggested=None

