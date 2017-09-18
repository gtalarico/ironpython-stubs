class ScrollBarRenderer(object):
 """ Provides methods used to render a scroll bar control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawArrowButton(g,bounds,state):
  """
  DrawArrowButton(g: Graphics,bounds: Rectangle,state: ScrollBarArrowButtonState)

   Draws a scroll arrow with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll arrow.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll arrow.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarArrowButtonState values that specifies the 

    visual state of the scroll arrow.
  """
  pass
 @staticmethod
 def DrawHorizontalThumb(g,bounds,state):
  """
  DrawHorizontalThumb(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a horizontal scroll box (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll box.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll box.
  """
  pass
 @staticmethod
 def DrawHorizontalThumbGrip(g,bounds,state):
  """
  DrawHorizontalThumbGrip(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a grip on a horizontal scroll box (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll box grip.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll box grip.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll box grip.
  """
  pass
 @staticmethod
 def DrawLeftHorizontalTrack(g,bounds,state):
  """
  DrawLeftHorizontalTrack(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a horizontal scroll bar track with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll bar track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll bar track.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll bar track.
  """
  pass
 @staticmethod
 def DrawLowerVerticalTrack(g,bounds,state):
  """
  DrawLowerVerticalTrack(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a vertical scroll bar track with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll bar track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll bar track.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll bar track.
  """
  pass
 @staticmethod
 def DrawRightHorizontalTrack(g,bounds,state):
  """
  DrawRightHorizontalTrack(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a horizontal scroll bar track with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll bar track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll bar track.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll bar track.
  """
  pass
 @staticmethod
 def DrawSizeBox(g,bounds,state):
  """
  DrawSizeBox(g: Graphics,bounds: Rectangle,state: ScrollBarSizeBoxState)

   Draws a scroll bar sizing handle with visual styles.

  

   g: The System.Drawing.Graphics used to draw the sizing handle.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the sizing handle.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarSizeBoxState values that specifies the 

    visual state of the sizing handle.
  """
  pass
 @staticmethod
 def DrawUpperVerticalTrack(g,bounds,state):
  """
  DrawUpperVerticalTrack(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a vertical scroll bar track with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll bar track.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll bar track.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll bar track.
  """
  pass
 @staticmethod
 def DrawVerticalThumb(g,bounds,state):
  """
  DrawVerticalThumb(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a vertical scroll box (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll box.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll box.
  """
  pass
 @staticmethod
 def DrawVerticalThumbGrip(g,bounds,state):
  """
  DrawVerticalThumbGrip(g: Graphics,bounds: Rectangle,state: ScrollBarState)

   Draws a grip on a vertical scroll box (also known as the thumb) with visual styles.

  

   g: The System.Drawing.Graphics used to draw the scroll box grip.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the scroll box grip.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll box grip.
  """
  pass
 @staticmethod
 def GetSizeBoxSize(g,state):
  """
  GetSizeBoxSize(g: Graphics,state: ScrollBarState) -> Size

  

   Returns the size of the sizing handle.

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the sizing handle.

  

   Returns: A System.Drawing.Size that specifies the size of the sizing handle.
  """
  pass
 @staticmethod
 def GetThumbGripSize(g,state):
  """
  GetThumbGripSize(g: Graphics,state: ScrollBarState) -> Size

  

   Returns the size of the scroll box grip.

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.ScrollBarState values that specifies the visual 

    state of the scroll box grip.

  

   Returns: A System.Drawing.Size that specifies the size of the scroll box grip.
  """
  pass
 IsSupported=True

