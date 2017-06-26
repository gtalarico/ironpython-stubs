class TextCompositionEventArgs(InputEventArgs):
 """
 Contains arguments associated with changes to a System.Windows.Input.TextComposition.
 
 TextCompositionEventArgs(inputDevice: InputDevice,composition: TextComposition)
 """
 @staticmethod
 def __new__(self,inputDevice,composition):
  """ __new__(cls: type,inputDevice: InputDevice,composition: TextComposition) """
  pass
 ControlText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets control text associated with a System.Windows.Input.TextComposition event.

Get: ControlText(self: TextCompositionEventArgs) -> str

"""

 SystemText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets system text associated with a System.Windows.Input.TextComposition event.

Get: SystemText(self: TextCompositionEventArgs) -> str

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets input text associated with a System.Windows.Input.TextComposition event.

Get: Text(self: TextCompositionEventArgs) -> str

"""

 TextComposition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Input.TextComposition associated with a System.Windows.Input.TextComposition event.

Get: TextComposition(self: TextCompositionEventArgs) -> TextComposition

"""


