class SplitterEventArgs(EventArgs):
 """
 Provides data for System.Windows.Forms.Splitter.SplitterMoving and the System.Windows.Forms.Splitter.SplitterMoved events.

 

 SplitterEventArgs(x: int,y: int,splitX: int,splitY: int)
 """
 @staticmethod
 def __new__(self,x,y,splitX,splitY):
  """ __new__(cls: type,x: int,y: int,splitX: int,splitY: int) """
  pass
 SplitX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the x-coordinate of the upper-left corner of the System.Windows.Forms.Splitter (in client coordinates).



Get: SplitX(self: SplitterEventArgs) -> int



Set: SplitX(self: SplitterEventArgs)=value

"""

 SplitY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the y-coordinate of the upper-left corner of the System.Windows.Forms.Splitter (in client coordinates).



Get: SplitY(self: SplitterEventArgs) -> int



Set: SplitY(self: SplitterEventArgs)=value

"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate of the mouse pointer (in client coordinates).



Get: X(self: SplitterEventArgs) -> int



"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate of the mouse pointer (in client coordinates).



Get: Y(self: SplitterEventArgs) -> int



"""


