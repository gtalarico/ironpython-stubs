class KeyGesture(InputGesture):
 """
 Defines a keyboard combination that can be used to invoke a command.
 
 KeyGesture(key: Key)
 KeyGesture(key: Key,modifiers: ModifierKeys)
 KeyGesture(key: Key,modifiers: ModifierKeys,displayString: str)
 """
 def GetDisplayStringForCulture(self,culture):
  """
  GetDisplayStringForCulture(self: KeyGesture,culture: CultureInfo) -> str
  
   Returns a string that can be used to display the 
    System.Windows.Input.KeyGesture.
  
  
   culture: The culture specific information.
   Returns: The string to display
  """
  pass
 def Matches(self,targetElement,inputEventArgs):
  """
  Matches(self: KeyGesture,targetElement: object,inputEventArgs: InputEventArgs) -> bool
  
   Determines whether this System.Windows.Input.KeyGesture matches the input 
    associated with the specified System.Windows.Input.InputEventArgs object.
  
  
   targetElement: The target.
   inputEventArgs: The input event data to compare this gesture to.
   Returns: true if the event data matches this System.Windows.Input.KeyGesture; otherwise,
    false.
  """
  pass
 @staticmethod
 def __new__(self,key,modifiers=None,displayString=None):
  """
  __new__(cls: type,key: Key)
  __new__(cls: type,key: Key,modifiers: ModifierKeys)
  __new__(cls: type,key: Key,modifiers: ModifierKeys,displayString: str)
  """
  pass
 DisplayString=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string representation of this System.Windows.Input.KeyGesture.

Get: DisplayString(self: KeyGesture) -> str

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the key associated with this System.Windows.Input.KeyGesture.

Get: Key(self: KeyGesture) -> Key

"""

 Modifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the modifier keys associated with this System.Windows.Input.KeyGesture.

Get: Modifiers(self: KeyGesture) -> ModifierKeys

"""


