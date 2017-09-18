class MSG(object):
 """ Contains message information from a thread's message queue. """
 hwnd=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the window handle (HWND) to the window whose window procedure receives the message.

Get: hwnd(self: MSG) -> IntPtr

Set: hwnd(self: MSG)=value
"""

 lParam=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the lParam value that specifies additional information about the message. The exact meaning depends on the value of the System.Windows.Interop.MSG.message member.

Get: lParam(self: MSG) -> IntPtr

Set: lParam(self: MSG)=value
"""

 message=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the message identifier.

Get: message(self: MSG) -> int

Set: message(self: MSG)=value
"""

 pt_x=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x coordinate of the cursor position on the screen,when the message was posted.

Get: pt_x(self: MSG) -> int

Set: pt_x(self: MSG)=value
"""

 pt_y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y coordinate of the cursor position on the screen,when the message was posted.

Get: pt_y(self: MSG) -> int

Set: pt_y(self: MSG)=value
"""

 time=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the time at which the message was posted.

Get: time(self: MSG) -> int

Set: time(self: MSG)=value
"""

 wParam=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the wParam value for the message,which specifies additional information about the message. The exact meaning depends on the value of the message.

Get: wParam(self: MSG) -> IntPtr

Set: wParam(self: MSG)=value
"""


