class DragEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.DragDrop,System.Windows.Forms.Control.DragEnter,or System.Windows.Forms.Control.DragOver event.

 

 DragEventArgs(data: IDataObject,keyState: int,x: int,y: int,allowedEffect: DragDropEffects,effect: DragDropEffects)
 """
 @staticmethod
 def __new__(self,data,keyState,x,y,allowedEffect,effect):
  """ __new__(cls: type,data: IDataObject,keyState: int,x: int,y: int,allowedEffect: DragDropEffects,effect: DragDropEffects) """
  pass
 AllowedEffect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets which drag-and-drop operations are allowed by the originator (or source) of the drag event.



Get: AllowedEffect(self: DragEventArgs) -> DragDropEffects



"""

 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.IDataObject that contains the data associated with this event.



Get: Data(self: DragEventArgs) -> IDataObject



"""

 Effect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the target drop effect in a drag-and-drop operation.



Get: Effect(self: DragEventArgs) -> DragDropEffects



Set: Effect(self: DragEventArgs)=value

"""

 KeyState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the SHIFT,CTRL,and ALT keys,as well as the state of the mouse buttons.



Get: KeyState(self: DragEventArgs) -> int



"""

 X=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the x-coordinate of the mouse pointer,in screen coordinates.



Get: X(self: DragEventArgs) -> int



"""

 Y=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the y-coordinate of the mouse pointer,in screen coordinates.



Get: Y(self: DragEventArgs) -> int



"""


