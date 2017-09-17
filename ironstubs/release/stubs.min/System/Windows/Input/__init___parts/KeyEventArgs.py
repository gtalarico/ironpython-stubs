class KeyEventArgs(KeyboardEventArgs):
 """
 Provides data for the System.Windows.UIElement.KeyUp and System.Windows.UIElement.KeyDown�routed events,as well as related attached and Preview events.
 
 KeyEventArgs(keyboard: KeyboardDevice,inputSource: PresentationSource,timestamp: int,key: Key)
 """
 @staticmethod
 def __new__(self,keyboard,inputSource,timestamp,key):
  """ __new__(cls: type,keyboard: KeyboardDevice,inputSource: PresentationSource,timestamp: int,key: Key) """
  pass
 DeadCharProcessedKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the key that is part of dead key composition to create a single combined character.

Get: DeadCharProcessedKey(self: KeyEventArgs) -> Key

"""

 ImeProcessedKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard key referenced by the event,if the key will be processed by an Input Method Editor (IME).

Get: ImeProcessedKey(self: KeyEventArgs) -> Key

"""

 InputSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the input source that provided this input.

Get: InputSource(self: KeyEventArgs) -> PresentationSource

"""

 IsDown=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the key referenced by the event is in the down state.

Get: IsDown(self: KeyEventArgs) -> bool

"""

 IsRepeat=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the keyboard key referenced by the event is a repeated key.

Get: IsRepeat(self: KeyEventArgs) -> bool

"""

 IsToggled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the key referenced by the event is in the toggled state.

Get: IsToggled(self: KeyEventArgs) -> bool

"""

 IsUp=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the key referenced by the event is in the up state.

Get: IsUp(self: KeyEventArgs) -> bool

"""

 Key=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard key associated with the event.

Get: Key(self: KeyEventArgs) -> Key

"""

 KeyStates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the keyboard key associated with this event.

Get: KeyStates(self: KeyEventArgs) -> KeyStates

"""

 SystemKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard key referenced by the event,if the key will be processed by the system.

Get: SystemKey(self: KeyEventArgs) -> Key

"""


