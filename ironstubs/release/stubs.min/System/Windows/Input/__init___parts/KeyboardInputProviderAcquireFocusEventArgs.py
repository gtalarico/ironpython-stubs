class KeyboardInputProviderAcquireFocusEventArgs(KeyboardEventArgs):
 """
 Provides data for the System.Windows.Input.Keyboard.KeyboardInputProviderAcquireFocus event.
 
 KeyboardInputProviderAcquireFocusEventArgs(keyboard: KeyboardDevice,timestamp: int,focusAcquired: bool)
 """
 @staticmethod
 def __new__(self,keyboard,timestamp,focusAcquired):
  """ __new__(cls: type,keyboard: KeyboardDevice,timestamp: int,focusAcquired: bool) """
  pass
 FocusAcquired=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether interoperation focus was acquired.

Get: FocusAcquired(self: KeyboardInputProviderAcquireFocusEventArgs) -> bool

"""


