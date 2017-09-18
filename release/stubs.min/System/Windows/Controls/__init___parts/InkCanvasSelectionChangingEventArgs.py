class InkCanvasSelectionChangingEventArgs(CancelEventArgs):
 """ Provides data for the System.Windows.Controls.InkCanvas.SelectionChanging. """
 def GetSelectedElements(self):
  """
  GetSelectedElements(self: InkCanvasSelectionChangingEventArgs) -> ReadOnlyCollection[UIElement]

  

   Returns the selected elements.

   Returns: The selected elements.
  """
  pass
 def GetSelectedStrokes(self):
  """
  GetSelectedStrokes(self: InkCanvasSelectionChangingEventArgs) -> StrokeCollection

  

   Returns the selected strokes.

   Returns: The selected strokes.
  """
  pass
 def SetSelectedElements(self,selectedElements):
  """ SetSelectedElements(self: InkCanvasSelectionChangingEventArgs,selectedElements: IEnumerable[UIElement]) """
  pass
 def SetSelectedStrokes(self,selectedStrokes):
  """
  SetSelectedStrokes(self: InkCanvasSelectionChangingEventArgs,selectedStrokes: StrokeCollection)

   Sets the selected strokes.

  

   selectedStrokes: The strokes to select.
  """
  pass
