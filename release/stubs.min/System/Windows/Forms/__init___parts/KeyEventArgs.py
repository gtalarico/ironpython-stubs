class KeyEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.

 

 KeyEventArgs(keyData: Keys)
 """
 @staticmethod
 def __new__(self,keyData):
  """ __new__(cls: type,keyData: Keys) """
  pass
 Alt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the ALT key was pressed.



Get: Alt(self: KeyEventArgs) -> bool



"""

 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the CTRL key was pressed.



Get: Control(self: KeyEventArgs) -> bool



"""

 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the event was handled.



Get: Handled(self: KeyEventArgs) -> bool



Set: Handled(self: KeyEventArgs)=value

"""

 KeyCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard code for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyCode(self: KeyEventArgs) -> Keys



"""

 KeyData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the key data for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyData(self: KeyEventArgs) -> Keys



"""

 KeyValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard value for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyValue(self: KeyEventArgs) -> int



"""

 Modifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the modifier flags for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event. The flags indicate which combination of CTRL,SHIFT,and ALT keys was pressed.



Get: Modifiers(self: KeyEventArgs) -> Keys



"""

 Shift=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the SHIFT key was pressed.



Get: Shift(self: KeyEventArgs) -> bool



"""

 SuppressKeyPress=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the key event should be passed on to the underlying control.



Get: SuppressKeyPress(self: KeyEventArgs) -> bool



Set: SuppressKeyPress(self: KeyEventArgs)=value

"""


