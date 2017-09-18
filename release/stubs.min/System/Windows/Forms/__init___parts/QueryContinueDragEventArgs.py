class QueryContinueDragEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.QueryContinueDrag event.

 

 QueryContinueDragEventArgs(keyState: int,escapePressed: bool,action: DragAction)
 """
 @staticmethod
 def __new__(self,keyState,escapePressed,action):
  """ __new__(cls: type,keyState: int,escapePressed: bool,action: DragAction) """
  pass
 Action=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the status of a drag-and-drop operation.



Get: Action(self: QueryContinueDragEventArgs) -> DragAction



Set: Action(self: QueryContinueDragEventArgs)=value

"""

 EscapePressed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets whether the user pressed the ESC key.



Get: EscapePressed(self: QueryContinueDragEventArgs) -> bool



"""

 KeyState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the SHIFT,CTRL,and ALT keys.



Get: KeyState(self: QueryContinueDragEventArgs) -> int



"""


