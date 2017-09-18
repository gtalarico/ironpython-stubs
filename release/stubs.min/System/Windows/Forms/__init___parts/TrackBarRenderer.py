class TrackBarRenderer(object):
 """ Provides methods used to render a track bar control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawBottomPointingThumb(g,bounds,state):
  """
  DrawBottomPointingThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws a downward-pointing track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawHorizontalThumb(g,bounds,state):
  """
  DrawHorizontalThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws a horizontal track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawHorizontalTicks(g,bounds,numTicks,edgeStyle):
  """
  DrawHorizontalTicks(g: Graphics,bounds: Rectangle,numTicks: int,edgeStyle: EdgeStyle)

   Draws the specified number of horizontal track bar ticks with visual styles.

  

   g: The System.Drawing.Graphics used to draw the ticks.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the ticks.

   numTicks: The number of ticks to draw.

   edgeStyle: One of the System.Windows.Forms.VisualStyles.EdgeStyle values.
  """
  pass
 @staticmethod
 def DrawHorizontalTrack(g,bounds):
  """
  DrawHorizontalTrack(g: Graphics,bounds: Rectangle)

   Draws the track for a horizontal track bar with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track.
  """
  pass
 @staticmethod
 def DrawLeftPointingThumb(g,bounds,state):
  """
  DrawLeftPointingThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws a left-pointing track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawRightPointingThumb(g,bounds,state):
  """
  DrawRightPointingThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws a right-pointing track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawTopPointingThumb(g,bounds,state):
  """
  DrawTopPointingThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws an upward-pointing track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawVerticalThumb(g,bounds,state):
  """
  DrawVerticalThumb(g: Graphics,bounds: Rectangle,state: TrackBarThumbState)

   Draws a vertical track bar slider (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track bar slider.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track bar slider.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.
  """
  pass
 @staticmethod
 def DrawVerticalTicks(g,bounds,numTicks,edgeStyle):
  """
  DrawVerticalTicks(g: Graphics,bounds: Rectangle,numTicks: int,edgeStyle: EdgeStyle)

   Draws the specified number of vertical track bar ticks with visual styles.

  

   g: The System.Drawing.Graphics used to draw the ticks.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the ticks.

   numTicks: The number of ticks to draw.

   edgeStyle: One of the System.Windows.Forms.VisualStyles.EdgeStyle values.
  """
  pass
 @staticmethod
 def DrawVerticalTrack(g,bounds):
  """
  DrawVerticalTrack(g: Graphics,bounds: Rectangle)

   Draws the track for a vertical track bar with visual styles.

  

   g: The System.Drawing.Graphics used to draw the track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the track.
  """
  pass
 @staticmethod
 def GetBottomPointingThumbSize(g,state):
  """
  GetBottomPointingThumbSize(g: Graphics,state: TrackBarThumbState) -> Size

  

   Returns the size,in pixels,of the track bar slider (also known as the thumb) that points down.

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the track bar slider.

  

   Returns: A System.Drawing.Size that specifies the size,in pixels,of the slider.
  """
  pass
 @staticmethod
 def GetLeftPointingThumbSize(g,state):
  """
  GetLeftPointingThumbSize(g: Graphics,state: TrackBarThumbState) -> Size

  

   Returns the size,in pixels,of the track bar slider (also known as the thumb) that points to 

    the left.

  

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the slider.

  

   Returns: A System.Drawing.Size that specifies the size,in pixels,of the slider.
  """
  pass
 @staticmethod
 def GetRightPointingThumbSize(g,state):
  """
  GetRightPointingThumbSize(g: Graphics,state: TrackBarThumbState) -> Size

  

   Returns the size,in pixels,of the track bar slider (also known as the thumb) that points to 

    the right.

  

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the slider.

  

   Returns: A System.Drawing.Size that specifies the size,in pixels,of the slider.
  """
  pass
 @staticmethod
 def GetTopPointingThumbSize(g,state):
  """
  GetTopPointingThumbSize(g: Graphics,state: TrackBarThumbState) -> Size

  

   Returns the size,in pixels,of the track bar slider (also known as the thumb) that points up.

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.TrackBarThumbState values that specifies the visual 

    state of the slider.

  

   Returns: A System.Drawing.Size that specifies the size,in pixels,of the slider.
  """
  pass
 IsSupported=True

