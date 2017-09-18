class GiveFeedbackEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.Control.GiveFeedback event,which occurs during a drag operation.

 

 GiveFeedbackEventArgs(effect: DragDropEffects,useDefaultCursors: bool)
 """
 @staticmethod
 def __new__(self,effect,useDefaultCursors):
  """ __new__(cls: type,effect: DragDropEffects,useDefaultCursors: bool) """
  pass
 Effect=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the drag-and-drop operation feedback that is displayed.



Get: Effect(self: GiveFeedbackEventArgs) -> DragDropEffects



"""

 UseDefaultCursors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets whether drag operation should use the default cursors that are associated with drag-drop effects.



Get: UseDefaultCursors(self: GiveFeedbackEventArgs) -> bool



Set: UseDefaultCursors(self: GiveFeedbackEventArgs)=value

"""


