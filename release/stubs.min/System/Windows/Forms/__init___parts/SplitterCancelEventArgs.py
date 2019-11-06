class SplitterCancelEventArgs(CancelEventArgs):
 """
 Provides data for splitter events.
 
 SplitterCancelEventArgs(mouseCursorX: int,mouseCursorY: int,splitX: int,splitY: int)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return SplitterCancelEventArgs()

 @staticmethod
 def __new__(self,mouseCursorX,mouseCursorY,splitX,splitY):
  """ __new__(cls: type,mouseCursorX: int,mouseCursorY: int,splitX: int,splitY: int) """
  pass
 MouseCursorX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the X coordinate of the mouse pointer in client coordinates.

Get: MouseCursorX(self: SplitterCancelEventArgs) -> int

"""

 MouseCursorY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Y coordinate of the mouse pointer in client coordinates.

Get: MouseCursorY(self: SplitterCancelEventArgs) -> int

"""

 SplitX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the X coordinate of the upper left corner of the System.Windows.Forms.SplitContainer in client coordinates.

Get: SplitX(self: SplitterCancelEventArgs) -> int

Set: SplitX(self: SplitterCancelEventArgs)=value
"""

 SplitY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the Y coordinate of the upper left corner of the System.Windows.Forms.SplitContainer in client coordinates.

Get: SplitY(self: SplitterCancelEventArgs) -> int

Set: SplitY(self: SplitterCancelEventArgs)=value
"""


