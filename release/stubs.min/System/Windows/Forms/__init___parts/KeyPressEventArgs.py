class KeyPressEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.KeyPress event.

 

 KeyPressEventArgs(keyChar: Char)
 """
 @staticmethod
 def __new__(self,keyChar):
  """ __new__(cls: type,keyChar: Char) """
  pass
 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.Control.KeyPress event was handled.



Get: Handled(self: KeyPressEventArgs) -> bool



Set: Handled(self: KeyPressEventArgs)=value

"""

 KeyChar=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the character corresponding to the key pressed.



Get: KeyChar(self: KeyPressEventArgs) -> Char



Set: KeyChar(self: KeyPressEventArgs)=value

"""


