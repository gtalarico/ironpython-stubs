class InkCanvasStrokeCollectedEventArgs(RoutedEventArgs):
    """
    Provides data for the System.Windows.Controls.InkCanvas.StrokeCollected event.
    
    InkCanvasStrokeCollectedEventArgs(stroke: Stroke)
    """
    @staticmethod # known case of __new__
    def __new__(self, stroke):
        """ __new__(cls: type, stroke: Stroke) """
        pass

    Stroke = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stroke that was added to the System.Windows.Controls.InkCanvas.

Get: Stroke(self: InkCanvasStrokeCollectedEventArgs) -> Stroke

"""


