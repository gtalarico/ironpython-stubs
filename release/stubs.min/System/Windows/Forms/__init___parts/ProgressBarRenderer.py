class ProgressBarRenderer(object):
 """ Provides methods used to render a progress bar control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawHorizontalBar(g,bounds):
  """
  DrawHorizontalBar(g: Graphics,bounds: Rectangle)

   Draws an empty progress bar control that fills in horizontally.

  

   g: The System.Drawing.Graphics used to draw the progress bar.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the progress bar.
  """
  pass
 @staticmethod
 def DrawHorizontalChunks(g,bounds):
  """
  DrawHorizontalChunks(g: Graphics,bounds: Rectangle)

   Draws a set of progress bar pieces that fill a horizontal progress bar.

  

   g: The System.Drawing.Graphics used to draw the progress bar.

   bounds: The System.Drawing.Rectangle that specifies the bounds to be filled by progress bar pieces.
  """
  pass
 @staticmethod
 def DrawVerticalBar(g,bounds):
  """
  DrawVerticalBar(g: Graphics,bounds: Rectangle)

   Draws an empty progress bar control that fills in vertically.

  

   g: The System.Drawing.Graphics used to draw the progress bar.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the progress bar.
  """
  pass
 @staticmethod
 def DrawVerticalChunks(g,bounds):
  """
  DrawVerticalChunks(g: Graphics,bounds: Rectangle)

   Draws a set of progress bar pieces that fill a vertical progress bar.

  

   g: The System.Drawing.Graphics used to draw the progress bar.

   bounds: The System.Drawing.Rectangle that specifies the bounds to be filled by progress bar pieces.
  """
  pass
 ChunkSpaceThickness=0
 ChunkThickness=6
 IsSupported=True

