class ButtonRenderer(object):
 """ Provides methods used to render a button control with or without visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawButton(g,bounds,*__args):
  """
  DrawButton(g: Graphics,bounds: Rectangle,image: Image,imageBounds: Rectangle,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds,with the specified image,and with an 

    optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   image: The System.Drawing.Image to draw on the button.

   imageBounds: The System.Drawing.Rectangle that represents the dimensions of image.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,buttonText: str,font: Font,image: Image,imageBounds: Rectangle,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds,with the specified text and image,and 

    with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   buttonText: The System.String to draw on the button.

   font: The System.Drawing.Font to apply to buttonText.

   image: The System.Drawing.Image to draw on the button.

   imageBounds: The System.Drawing.Rectangle that represents the dimensions of image.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,buttonText: str,font: Font,flags: TextFormatFlags,image: Image,imageBounds: Rectangle,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds; with the specified text,text 

    formatting,and image; and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   buttonText: The System.String to draw on the button.

   font: The System.Drawing.Font to apply to buttonText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values to apply to buttonText.

   image: The System.Drawing.Image to draw on the button.

   imageBounds: The System.Drawing.Rectangle that represents the dimensions of image.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,buttonText: str,font: Font,flags: TextFormatFlags,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds,with the specified text and text 

    formatting,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   buttonText: The System.String to draw on the button.

   font: The System.Drawing.Font to apply to buttonText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values to apply to buttonText.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,state: PushButtonState)

   Draws a button control in the specified state and bounds.

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds,and with an optional focus rectangle.

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

  DrawButton(g: Graphics,bounds: Rectangle,buttonText: str,font: Font,focused: bool,state: PushButtonState)

   Draws a button control in the specified state and bounds,with the specified text,and with an 

    optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the button.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the button.

   buttonText: The System.String to draw on the button.

   font: The System.Drawing.Font to apply to buttonText.

   focused: true to draw a focus rectangle on the button; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.
  """
  pass
 @staticmethod
 def DrawParentBackground(g,bounds,childControl):
  """
  DrawParentBackground(g: Graphics,bounds: Rectangle,childControl: Control)

   Draws the background of a control's parent in the specified area.

  

   g: The System.Drawing.Graphics used to draw the background of the parent of childControl.

   bounds: The System.Drawing.Rectangle in which to draw the parent control's background. This rectangle 

    

   childControl: The control whose parent's background will be drawn.
  """
  pass
 @staticmethod
 def IsBackgroundPartiallyTransparent(state):
  """
  IsBackgroundPartiallyTransparent(state: PushButtonState) -> bool

  

   Indicates whether the background of the button has semitransparent or alpha-blended pieces.

  

   state: One of the System.Windows.Forms.VisualStyles.PushButtonState values that specifies the visual 

    state of the button.

  

   Returns: true if the background of the button has semitransparent or alpha-blended pieces; otherwise,

    false.
  """
  pass
 RenderMatchingApplicationState=True

