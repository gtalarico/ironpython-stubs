class InkCanvasSelectionEditingEventArgs(CancelEventArgs):
 """ Provides data for the System.Windows.Controls.InkCanvas.SelectionMoving and System.Windows.Controls.InkCanvas.SelectionResizing events. """
 NewRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the bounds of the selection after it is moved or resized.



Get: NewRectangle(self: InkCanvasSelectionEditingEventArgs) -> Rect



Set: NewRectangle(self: InkCanvasSelectionEditingEventArgs)=value

"""

 OldRectangle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the bounds of the selection before the user moved or resized it.



Get: OldRectangle(self: InkCanvasSelectionEditingEventArgs) -> Rect



"""


