class InkCanvasStrokesReplacedEventArgs(EventArgs):
 """ Provides data for the System.Windows.Controls.InkCanvas.StrokesReplaced event. """
 NewStrokes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new strokes of the System.Windows.Controls.InkCanvas.



Get: NewStrokes(self: InkCanvasStrokesReplacedEventArgs) -> StrokeCollection



"""

 PreviousStrokes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous strokes of the System.Windows.Controls.InkCanvas.



Get: PreviousStrokes(self: InkCanvasStrokesReplacedEventArgs) -> StrokeCollection



"""


