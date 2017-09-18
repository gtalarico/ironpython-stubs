class MouseEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.MouseUp,System.Windows.Forms.Control.MouseDown,and System.Windows.Forms.Control.MouseMove events.

 

 MouseEventArgs(button: MouseButtons,clicks: int,x: int,y: int,delta: int)
 """
 @staticmethod
 def __new__(self,button,clicks,x,y,delta):
  """ __new__(cls: type,button: MouseButtons,clicks: int,x: int,y: int,delta: int) """
  pass
 Button=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets which mouse button was pressed.



Get: Button(self: MouseEventArgs) -> MouseButtons



"""

 Clicks=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of times the mouse button was pressed and released.



Get: Clicks(self: MouseEventArgs) -> int



"""

 Delta=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a signed count of the number of detents the mouse wheel has rotated,multiplied by the WHEEL_DELTA constant. A detent is one notch of the mouse wheel.



Get: Delta(self: MouseEventArgs) -> int



"""

 Location=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the location of the mouse during the generating mouse event.



Get: Location(self: MouseEventArgs) -> Point



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate of the mouse during the generating mouse event.



Get: X(self: MouseEventArgs) -> int



"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate of the mouse during the generating mouse event.



Get: Y(self: MouseEventArgs) -> int



"""


