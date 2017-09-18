class CheckBoxRenderer(object):
 """ Provides methods used to render a check box control with or without visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawCheckBox(g,glyphLocation,*__args):
  """
  DrawCheckBox(g: Graphics,glyphLocation: Point,textBounds: Rectangle,checkBoxText: str,font: Font,image: Image,imageBounds: Rectangle,focused: bool,state: CheckBoxState)

   Draws a check box control in the specified state and location,with the specified text and 

    image,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the check box.

   glyphLocation: The System.Drawing.Point to draw the check box glyph at.

   textBounds: The System.Drawing.Rectangle to draw checkBoxText in.

   checkBoxText: The System.String to draw with the check box.

   font: The System.Drawing.Font to apply to checkBoxText.

   image: The System.Drawing.Image to draw with the check box.

   imageBounds: The System.Drawing.Rectangle that represents the dimensions of image.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

  DrawCheckBox(g: Graphics,glyphLocation: Point,textBounds: Rectangle,checkBoxText: str,font: Font,flags: TextFormatFlags,image: Image,imageBounds: Rectangle,focused: bool,state: CheckBoxState)

   Draws a check box control in the specified state and location; with the specified text,text 

    formatting,and image; and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the check box.

   glyphLocation: The System.Drawing.Point to draw the check box glyph at.

   textBounds: The System.Drawing.Rectangle to draw checkBoxText in.

   checkBoxText: The System.String to draw with the check box.

   font: The System.Drawing.Font to apply to checkBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   image: The System.Drawing.Image to draw with the check box.

   imageBounds: The System.Drawing.Rectangle that represents the dimensions of image.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

  DrawCheckBox(g: Graphics,glyphLocation: Point,textBounds: Rectangle,checkBoxText: str,font: Font,flags: TextFormatFlags,focused: bool,state: CheckBoxState)

   Draws a check box control in the specified state and location,with the specified text and text 

    formatting,and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the check box.

   glyphLocation: The System.Drawing.Point to draw the check box glyph at.

   textBounds: The System.Drawing.Rectangle to draw checkBoxText in.

   checkBoxText: The System.String to draw with the check box.

   font: The System.Drawing.Font to apply to checkBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

  DrawCheckBox(g: Graphics,glyphLocation: Point,state: CheckBoxState)

   Draws a check box control in the specified state and location.

  

   g: The System.Drawing.Graphics used to draw the check box.

   glyphLocation: The System.Drawing.Point to draw the check box glyph at.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

  DrawCheckBox(g: Graphics,glyphLocation: Point,textBounds: Rectangle,checkBoxText: str,font: Font,focused: bool,state: CheckBoxState)

   Draws a check box control in the specified state and location,with the specified text,and with 

    an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the check box.

   glyphLocation: The System.Drawing.Point to draw the check box glyph at.

   textBounds: The System.Drawing.Rectangle to draw checkBoxText in.

   checkBoxText: The System.String to draw with the check box.

   font: The System.Drawing.Font to apply to checkBoxText.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.
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
 def GetGlyphSize(g,state):
  """
  GetGlyphSize(g: Graphics,state: CheckBoxState) -> Size

  

   Returns the size of the check box glyph.

  

   g: The System.Drawing.Graphics this operation will use.

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

   Returns: A System.Drawing.Size that represents the size of the check box glyph.
  """
  pass
 @staticmethod
 def IsBackgroundPartiallyTransparent(state):
  """
  IsBackgroundPartiallyTransparent(state: CheckBoxState) -> bool

  

   Indicates whether the background of the check box has semitransparent or alpha-blended pieces.

  

   state: One of the System.Windows.Forms.VisualStyles.CheckBoxState values that specifies the visual 

    state of the check box.

  

   Returns: true if the background of the check box has semitransparent or alpha-blended pieces; otherwise,

    false.
  """
  pass
 RenderMatchingApplicationState=True

