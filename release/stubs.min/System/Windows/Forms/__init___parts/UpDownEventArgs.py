class UpDownEventArgs(EventArgs):
 """
 Provides data for controls that derive from the System.Windows.Forms.UpDownBase control.

 

 UpDownEventArgs(buttonPushed: int)
 """
 @staticmethod
 def __new__(self,buttonPushed):
  """ __new__(cls: type,buttonPushed: int) """
  pass
 ButtonID=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that represents which button the user clicked.



Get: ButtonID(self: UpDownEventArgs) -> int



"""


