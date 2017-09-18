class RadioButtonRenderer(object):
 """ Provides methods used to render an option button control (also known as a radio button) with or without visual styles. This class cannot be inherited. """
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
 def DrawRadioButton(g,glyphLocation,*__args):
  """
  DrawRadioButton(g: Graphics,glyphLocation: Point,textBounds: Rectangle,radioButtonText: str,font: Font,image: Image,imageBounds: Rectangle,focused: bool,state: RadioButtonState)

   Draws an option button control (also known as a radio button) in the specified state and 

    location,with the specified text and image,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the option button.

   glyphLocation: The System.Drawing.Point to draw the option button glyph at.

   textBounds: The System.Drawing.Rectangle to draw radioButtonText in.

   radioButtonText: The System.String to draw with the option button.

   font: The System.Drawing.Font to apply to radioButtonText.

   image: The System.Drawing.Image to draw with the option button.

   imageBounds: The System.Drawing.Rectangle to draw image in.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

  DrawRadioButton(g: Graphics,glyphLocation: Point,textBounds: Rectangle,radioButtonText: str,font: Font,flags: TextFormatFlags,image: Image,imageBounds: Rectangle,focused: bool,state: RadioButtonState)

   Draws an option button control (also known as a radio button) in the specified state and 

    location; with the specified text,text formatting,and image; and with an optional focus 

    rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the option button.

   glyphLocation: The System.Drawing.Point to draw the option button glyph at.

   textBounds: The System.Drawing.Rectangle to draw radioButtonText in.

   radioButtonText: The System.String to draw with the option button.

   font: The System.Drawing.Font to apply to radioButtonText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   image: The System.Drawing.Image to draw with the option button.

   imageBounds: The System.Drawing.Rectangle to draw image in.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

  DrawRadioButton(g: Graphics,glyphLocation: Point,textBounds: Rectangle,radioButtonText: str,font: Font,flags: TextFormatFlags,focused: bool,state: RadioButtonState)

   Draws an option button control (also known as a radio button) in the specified state and 

    location,with the specified text and text formatting,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the option button.

   glyphLocation: The System.Drawing.Point to draw the option button glyph at.

   textBounds: The System.Drawing.Rectangle to draw radioButtonText in.

   radioButtonText: The System.String to draw with the option button.

   font: The System.Drawing.Font to apply to radioButtonText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

  DrawRadioButton(g: Graphics,glyphLocation: Point,state: RadioButtonState)

   Draws an option button control (also known as a radio button) in the specified state and 

    location.

  

  

   g: The System.Drawing.Graphics used to draw the option button.

   glyphLocation: The System.Drawing.Point to draw the option button glyph at.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

  DrawRadioButton(g: Graphics,glyphLocation: Point,textBounds: Rectangle,radioButtonText: str,font: Font,focused: bool,state: RadioButtonState)

   Draws an option button control (also known as a radio button) in the specified state and 

    location,with the specified text,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the option button.

   glyphLocation: The System.Drawing.Point to draw the option button glyph at.

   textBounds: The System.Drawing.Rectangle to draw radioButtonText in.

   radioButtonText: The System.String to draw with the option button.

   font: The System.Drawing.Font to apply to radioButtonText.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.
  """
  pass
 @staticmethod
 def GetGlyphSize(g,state):
  """
  GetGlyphSize(g: Graphics,state: RadioButtonState) -> Size

  

   Returns the size,in pixels,of the option button (also known as a radio button) glyph.

  

   g: The System.Drawing.Graphics used to draw the option button.

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

   Returns: A System.Drawing.Size that represents the size,in pixels,of the option button glyph.
  """
  pass
 @staticmethod
 def IsBackgroundPartiallyTransparent(state):
  """
  IsBackgroundPartiallyTransparent(state: RadioButtonState) -> bool

  

   Indicates whether the background of the option button (also known as a radio button) has 

    semitransparent or alpha-blended pieces.

  

  

   state: One of the System.Windows.Forms.VisualStyles.RadioButtonState values that specifies the visual 

    state of the option button.

  

   Returns: true if the background of the option button has semitransparent or alpha-blended pieces; 

    otherwise,false.
  """
  pass
 RenderMatchingApplicationState=True

