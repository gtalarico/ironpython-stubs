class PreviewKeyDownEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.PreviewKeyDown event.

 

 PreviewKeyDownEventArgs(keyData: Keys)
 """
 @staticmethod
 def __new__(self,keyData):
  """ __new__(cls: type,keyData: Keys) """
  pass
 Alt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the ALT key was pressed.



Get: Alt(self: PreviewKeyDownEventArgs) -> bool



"""

 Control=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the CTRL key was pressed.



Get: Control(self: PreviewKeyDownEventArgs) -> bool



"""

 IsInputKey=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether a key is a regular input key.



Get: IsInputKey(self: PreviewKeyDownEventArgs) -> bool



Set: IsInputKey(self: PreviewKeyDownEventArgs)=value

"""

 KeyCode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard code for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyCode(self: PreviewKeyDownEventArgs) -> Keys



"""

 KeyData=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the key data for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyData(self: PreviewKeyDownEventArgs) -> Keys



"""

 KeyValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the keyboard value for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: KeyValue(self: PreviewKeyDownEventArgs) -> int



"""

 Modifiers=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the modifier flags for a System.Windows.Forms.Control.KeyDown or System.Windows.Forms.Control.KeyUp event.



Get: Modifiers(self: PreviewKeyDownEventArgs) -> Keys



"""

 Shift=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the SHIFT key was pressed.



Get: Shift(self: PreviewKeyDownEventArgs) -> bool



"""


