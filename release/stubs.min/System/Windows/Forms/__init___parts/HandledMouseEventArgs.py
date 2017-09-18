class HandledMouseEventArgs(MouseEventArgs):
 """
 Allows a custom control to prevent the System.Windows.Forms.Control.MouseWheel event from being sent to its parent container.

 

 HandledMouseEventArgs(button: MouseButtons,clicks: int,x: int,y: int,delta: int)

 HandledMouseEventArgs(button: MouseButtons,clicks: int,x: int,y: int,delta: int,defaultHandledValue: bool)
 """
 @staticmethod
 def __new__(self,button,clicks,x,y,delta,defaultHandledValue=None):
  """
  __new__(cls: type,button: MouseButtons,clicks: int,x: int,y: int,delta: int)

  __new__(cls: type,button: MouseButtons,clicks: int,x: int,y: int,delta: int,defaultHandledValue: bool)
  """
  pass
 Handled=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether this event should be forwarded to the control's parent container.



Get: Handled(self: HandledMouseEventArgs) -> bool



Set: Handled(self: HandledMouseEventArgs)=value

"""


