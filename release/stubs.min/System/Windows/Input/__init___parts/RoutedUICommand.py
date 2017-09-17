class RoutedUICommand(RoutedCommand,ICommand):
 """
 Defines an System.Windows.Input.ICommand that is routed through the element tree and contains a text property.
 
 RoutedUICommand()
 RoutedUICommand(text: str,name: str,ownerType: Type)
 RoutedUICommand(text: str,name: str,ownerType: Type,inputGestures: InputGestureCollection)
 """
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,text=None,name=None,ownerType=None,inputGestures=None):
  """
  __new__(cls: type)
  __new__(cls: type,text: str,name: str,ownerType: Type)
  __new__(cls: type,text: str,name: str,ownerType: Type,inputGestures: InputGestureCollection)
  """
  pass
 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the text that describes this command.

Get: Text(self: RoutedUICommand) -> str

Set: Text(self: RoutedUICommand)=value
"""


