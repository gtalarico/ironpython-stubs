class UICuesEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.ChangeUICues event.

 

 UICuesEventArgs(uicues: UICues)
 """
 @staticmethod
 def __new__(self,uicues):
  """ __new__(cls: type,uicues: UICues) """
  pass
 Changed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bitwise combination of the System.Windows.Forms.UICues values.



Get: Changed(self: UICuesEventArgs) -> UICues



"""

 ChangeFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the state of the focus cues has changed.



Get: ChangeFocus(self: UICuesEventArgs) -> bool



"""

 ChangeKeyboard=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the state of the keyboard cues has changed.



Get: ChangeKeyboard(self: UICuesEventArgs) -> bool



"""

 ShowFocus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether focus rectangles are shown after the change.



Get: ShowFocus(self: UICuesEventArgs) -> bool



"""

 ShowKeyboard=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether keyboard cues are underlined after the change.



Get: ShowKeyboard(self: UICuesEventArgs) -> bool



"""


