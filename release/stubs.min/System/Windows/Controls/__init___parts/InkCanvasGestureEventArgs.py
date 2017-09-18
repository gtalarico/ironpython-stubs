class InkCanvasGestureEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Controls.InkCanvas.Gesture event.

 

 InkCanvasGestureEventArgs(strokes: StrokeCollection,gestureRecognitionResults: IEnumerable[GestureRecognitionResult])
 """
 def GetGestureRecognitionResults(self):
  """
  GetGestureRecognitionResults(self: InkCanvasGestureEventArgs) -> ReadOnlyCollection[GestureRecognitionResult]

  

   Returns results from the gesture recognizer.

   Returns: A collection of possible application gestures that the 

    System.Windows.Controls.InkCanvasGestureEventArgs.Strokes might be.
  """
  pass
 @staticmethod
 def __new__(self,strokes,gestureRecognitionResults):
  """ __new__(cls: type,strokes: StrokeCollection,gestureRecognitionResults: IEnumerable[GestureRecognitionResult]) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a Boolean value that indicates whether strokes should be considered a gesture.



Get: Cancel(self: InkCanvasGestureEventArgs) -> bool



Set: Cancel(self: InkCanvasGestureEventArgs)=value

"""

 Strokes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the strokes that represent the possible gesture.



Get: Strokes(self: InkCanvasGestureEventArgs) -> StrokeCollection



"""


