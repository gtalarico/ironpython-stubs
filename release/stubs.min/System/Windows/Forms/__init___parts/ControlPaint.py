class ControlPaint(object):
 """ Provides methods used to paint common Windows controls and their elements. This class cannot be inherited. """
 @staticmethod
 def CreateHBitmap16Bit(bitmap,background):
  """
  CreateHBitmap16Bit(bitmap: Bitmap,background: Color) -> IntPtr

  

   Creates a 16-bit color bitmap.

  

   bitmap: The System.Drawing.Bitmap to create.

   background: The System.Drawing.Color of the background.

   Returns: An System.IntPtr representing the handle to the bitmap.
  """
  pass
 @staticmethod
 def CreateHBitmapColorMask(bitmap,monochromeMask):
  """
  CreateHBitmapColorMask(bitmap: Bitmap,monochromeMask: IntPtr) -> IntPtr

  

   Creates a Win32 HBITMAP out of the image.

  

   bitmap: The System.Drawing.Bitmap to create.

   monochromeMask: A pointer to the monochrome mask.

   Returns: An System.IntPtr representing the handle to the bitmap.
  """
  pass
 @staticmethod
 def CreateHBitmapTransparencyMask(bitmap):
  """
  CreateHBitmapTransparencyMask(bitmap: Bitmap) -> IntPtr

  

   Creates a color mask for the specified bitmap that indicates which color should be displayed as 

    transparent.

  

  

   bitmap: The System.Drawing.Bitmap to create the transparency mask for.

   Returns: The handle to the System.Drawing.Bitmap mask.
  """
  pass
 @staticmethod
 def Dark(baseColor,percOfDarkDark=None):
  """
  Dark(baseColor: Color) -> Color

  

   Creates a new dark color object for the control from the specified color.

  

   baseColor: The System.Drawing.Color to be darkened.

   Returns: A System.Drawing.Color that represents the dark color on the control.

  Dark(baseColor: Color,percOfDarkDark: Single) -> Color

  

   Creates a new dark color object for the control from the specified color and darkens it by the 

    specified percentage.

  

  

   baseColor: The System.Drawing.Color to be darkened.

   percOfDarkDark: The percentage to darken the specified System.Drawing.Color.

   Returns: A System.Drawing.Color that represent the dark color on the control.
  """
  pass
 @staticmethod
 def DarkDark(baseColor):
  """
  DarkDark(baseColor: Color) -> Color

  

   Creates a new dark color object for the control from the specified color.

  

   baseColor: The System.Drawing.Color to be darkened.

   Returns: A System.Drawing.Color that represents the dark color on the control.
  """
  pass
 @staticmethod
 def DrawBorder(graphics,bounds,*__args):
  """
  DrawBorder(graphics: Graphics,bounds: Rectangle,leftColor: Color,leftWidth: int,leftStyle: ButtonBorderStyle,topColor: Color,topWidth: int,topStyle: ButtonBorderStyle,rightColor: Color,rightWidth: int,rightStyle: ButtonBorderStyle,bottomColor: Color,bottomWidth: int,bottomStyle: ButtonBorderStyle)

   Draws a border on a button-style control with the specified styles,colors,and border widths; 

    on the specified graphics surface; and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   bounds: The System.Drawing.Rectangle that represents the dimensions of the border.

   leftColor: The System.Drawing.Color of the left of the border.

   leftWidth: The width of the left border.

   leftStyle: One of the System.Windows.Forms.ButtonBorderStyle values that specifies the style of the left 

    border.

  

   topColor: The System.Drawing.Color of the top of the border.

   topWidth: The width of the top border.

   topStyle: One of the System.Windows.Forms.ButtonBorderStyle values that specifies the style of the top 

    border.

  

   rightColor: The System.Drawing.Color of the right of the border.

   rightWidth: The width of the right border.

   rightStyle: One of the System.Windows.Forms.ButtonBorderStyle values that specifies the style of the right 

    border.

  

   bottomColor: The System.Drawing.Color of the bottom of the border.

   bottomWidth: The width of the bottom border.

   bottomStyle: One of the System.Windows.Forms.ButtonBorderStyle values that specifies the style of the bottom 

    border.

  

  DrawBorder(graphics: Graphics,bounds: Rectangle,color: Color,style: ButtonBorderStyle)

   Draws a border with the specified style and color,on the specified graphics surface,and within 

    the specified bounds on a button-style control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   bounds: The System.Drawing.Rectangle that represents the dimensions of the border.

   color: The System.Drawing.Color of the border.

   style: One of the System.Windows.Forms.ButtonBorderStyle values that specifies the style of the border.
  """
  pass
 @staticmethod
 def DrawBorder3D(graphics,*__args):
  """
  DrawBorder3D(graphics: Graphics,x: int,y: int,width: int,height: int)

   Draws a three-dimensional style border on the specified graphics surface and within the 

    specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the top left of the border rectangle.

   y: The y-coordinate of the top left of the border rectangle.

   width: The width of the border rectangle.

   height: The height of the border rectangle.

  DrawBorder3D(graphics: Graphics,x: int,y: int,width: int,height: int,style: Border3DStyle)

   Draws a three-dimensional style border with the specified style,on the specified graphics 

    surface,and within the specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the top left of the border rectangle.

   y: The y-coordinate of the top left of the border rectangle.

   width: The width of the border rectangle.

   height: The height of the border rectangle.

   style: One of the System.Windows.Forms.Border3DStyle values that specifies the style of the border.

  DrawBorder3D(graphics: Graphics,x: int,y: int,width: int,height: int,style: Border3DStyle,sides: Border3DSide)

   Draws a three-dimensional style border with the specified style,on the specified graphics 

    surface and side,and within the specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the top left of the border rectangle.

   y: The y-coordinate of the top left of the border rectangle.

   width: The width of the border rectangle.

   height: The height of the border rectangle.

   style: One of the System.Windows.Forms.Border3DStyle values that specifies the style of the border.

   sides: The System.Windows.Forms.Border3DSide of the rectangle to draw the border on.

  DrawBorder3D(graphics: Graphics,rectangle: Rectangle)

   Draws a three-dimensional style border on the specified graphics surface and within the 

    specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the border.

  DrawBorder3D(graphics: Graphics,rectangle: Rectangle,style: Border3DStyle)

   Draws a three-dimensional style border with the specified style,on the specified graphics 

    surface,and within the specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the border.

   style: One of the System.Windows.Forms.Border3DStyle values that specifies the style of the border.

  DrawBorder3D(graphics: Graphics,rectangle: Rectangle,style: Border3DStyle,sides: Border3DSide)

   Draws a three-dimensional style border with the specified style,on the specified graphics 

    surface and sides,and within the specified bounds on a control.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the border.

   style: One of the System.Windows.Forms.Border3DStyle values that specifies the style of the border.

   sides: One of the System.Windows.Forms.Border3DSide values that specifies the side of the rectangle to 

    draw the border on.
  """
  pass
 @staticmethod
 def DrawButton(graphics,*__args):
  """
  DrawButton(graphics: Graphics,x: int,y: int,width: int,height: int,state: ButtonState)

   Draws a button control in the specified state,on the specified graphics surface,and within the 

    specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the button.

   height: The height of the button.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the button in.

  

  DrawButton(graphics: Graphics,rectangle: Rectangle,state: ButtonState)

   Draws a button control in the specified state,on the specified graphics surface,and within the 

    specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the button.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the button in.
  """
  pass
 @staticmethod
 def DrawCaptionButton(graphics,*__args):
  """
  DrawCaptionButton(graphics: Graphics,x: int,y: int,width: int,height: int,button: CaptionButton,state: ButtonState)

   Draws the specified caption button control in the specified state,on the specified graphics 

    surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the top left of the drawing rectangle.

   y: The y-coordinate of the top left of the drawing rectangle.

   width: The width of the drawing rectangle.

   height: The height of the drawing rectangle.

   button: One of the System.Windows.Forms.CaptionButton values that specifies the type of caption button 

    to draw.

  

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the button in.

  

  DrawCaptionButton(graphics: Graphics,rectangle: Rectangle,button: CaptionButton,state: ButtonState)

   Draws the specified caption button control in the specified state,on the specified graphics 

    surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the caption button.

   button: One of the System.Windows.Forms.CaptionButton values that specifies the type of caption button 

    to draw.

  

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the button in.
  """
  pass
 @staticmethod
 def DrawCheckBox(graphics,*__args):
  """
  DrawCheckBox(graphics: Graphics,rectangle: Rectangle,state: ButtonState)

   Draws a check box control in the specified state,on the specified graphics surface,and within 

    the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the check box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the check box in.

  

  DrawCheckBox(graphics: Graphics,x: int,y: int,width: int,height: int,state: ButtonState)

   Draws a check box control in the specified state,on the specified graphics surface,and within 

    the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the check box.

   height: The height of the check box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the check box in.
  """
  pass
 @staticmethod
 def DrawComboButton(graphics,*__args):
  """
  DrawComboButton(graphics: Graphics,x: int,y: int,width: int,height: int,state: ButtonState)

   Draws a drop-down button on a combo box control in the specified state,on the specified 

    graphics surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the top left of the border rectangle.

   y: The y-coordinate of the top left of the border rectangle.

   width: The width of the combo box.

   height: The height of the combo box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the combo box in.

  

  DrawComboButton(graphics: Graphics,rectangle: Rectangle,state: ButtonState)

   Draws a drop-down button on a combo box control in the specified state,on the specified 

    graphics surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the combo box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the combo box in.
  """
  pass
 @staticmethod
 def DrawContainerGrabHandle(graphics,bounds):
  """
  DrawContainerGrabHandle(graphics: Graphics,bounds: Rectangle)

   Draws a container control grab handle glyph on the specified graphics surface and within the 

    specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   bounds: The System.Drawing.Rectangle that represents the dimensions of the grab handle glyph.
  """
  pass
 @staticmethod
 def DrawFocusRectangle(graphics,rectangle,foreColor=None,backColor=None):
  """
  DrawFocusRectangle(graphics: Graphics,rectangle: Rectangle,foreColor: Color,backColor: Color)

   Draws a focus rectangle on the specified graphics surface and within the specified bounds.

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the grab handle glyph.

   foreColor: The System.Drawing.Color that is the foreground color of the object to draw the focus rectangle 

    on.

  

   backColor: The System.Drawing.Color that is the background color of the object to draw the focus rectangle 

    on.

  

  DrawFocusRectangle(graphics: Graphics,rectangle: Rectangle)

   Draws a focus rectangle on the specified graphics surface and within the specified bounds.

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the grab handle glyph.
  """
  pass
 @staticmethod
 def DrawGrabHandle(graphics,rectangle,primary,enabled):
  """
  DrawGrabHandle(graphics: Graphics,rectangle: Rectangle,primary: bool,enabled: bool)

   Draws a standard selection grab handle glyph on the specified graphics surface,within the 

    specified bounds,and in the specified state and style.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the grab handle glyph.

   primary: true to draw the handle as a primary grab handle; otherwise,false.

   enabled: true to draw the handle in an enabled state; otherwise,false.
  """
  pass
 @staticmethod
 def DrawGrid(graphics,area,pixelsBetweenDots,backColor):
  """
  DrawGrid(graphics: Graphics,area: Rectangle,pixelsBetweenDots: Size,backColor: Color)

   Draws a grid of one-pixel dots with the specified spacing,within the specified bounds,on the 

    specified graphics surface,and in the specified color.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   area: The System.Drawing.Rectangle that represents the dimensions of the grid.

   pixelsBetweenDots: The System.Drawing.Size that specified the height and width between the dots of the grid.

   backColor: The System.Drawing.Color of the background behind the grid.
  """
  pass
 @staticmethod
 def DrawImageDisabled(graphics,image,x,y,background):
  """
  DrawImageDisabled(graphics: Graphics,image: Image,x: int,y: int,background: Color)

   Draws the specified image in a disabled state.

  

   graphics: The System.Drawing.Graphics to draw on.

   image: The System.Drawing.Image to draw.

   x: The x-coordinate of the top left of the border image.

   y: The y-coordinate of the top left of the border image.

   background: The System.Drawing.Color of the background behind the image.
  """
  pass
 @staticmethod
 def DrawLockedFrame(graphics,rectangle,primary):
  """
  DrawLockedFrame(graphics: Graphics,rectangle: Rectangle,primary: bool)

   Draws a locked selection frame on the screen within the specified bounds and on the specified 

    graphics surface. Specifies whether to draw the frame with the primary selected colors.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the frame.

   primary: true to draw this frame with the colors used for the primary selection; otherwise,false.
  """
  pass
 @staticmethod
 def DrawMenuGlyph(graphics,*__args):
  """
  DrawMenuGlyph(graphics: Graphics,x: int,y: int,width: int,height: int,glyph: MenuGlyph)

   Draws the specified menu glyph on a menu item control with the specified bounds and on the 

    specified surface.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the menu glyph.

   height: The height of the menu glyph.

   glyph: One of the System.Windows.Forms.MenuGlyph values that specifies the image to draw.

  DrawMenuGlyph(graphics: Graphics,x: int,y: int,width: int,height: int,glyph: MenuGlyph,foreColor: Color,backColor: Color)

   Draws the specified menu glyph on a menu item control within the specified coordinates,height,

    and width on the specified surface,replacing System.Drawing.Color.White with the color 

    specified in the backColor parameter and replacing System.Drawing.Color.Black with the color 

    specified in the foreColor parameter.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the menu glyph.

   height: The height of the menu glyph.

   glyph: One of the System.Windows.Forms.MenuGlyph values that specifies the image to draw.

   foreColor: The color that replaces System.Drawing.Color.White as the foreground color.

   backColor: The color that replaces System.Drawing.Color.Black as the background color.

  DrawMenuGlyph(graphics: Graphics,rectangle: Rectangle,glyph: MenuGlyph)

   Draws the specified menu glyph on a menu item control within the specified bounds and on the 

    specified surface.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the glyph.

   glyph: One of the System.Windows.Forms.MenuGlyph values that specifies the image to draw.

  DrawMenuGlyph(graphics: Graphics,rectangle: Rectangle,glyph: MenuGlyph,foreColor: Color,backColor: Color)

   Draws the specified menu glyph on a menu item control within the specified bounds and on the 

    specified surface,replacing System.Drawing.Color.White with the color specified in the 

    backColor parameter and replacing System.Drawing.Color.Black with the color specified in the 

    foreColor parameter.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the glyph.

   glyph: One of the System.Windows.Forms.MenuGlyph values that specifies the image to draw.

   foreColor: The color that replaces System.Drawing.Color.White as the foreground color.

   backColor: The color that replaces System.Drawing.Color.Black as the background color.
  """
  pass
 @staticmethod
 def DrawMixedCheckBox(graphics,*__args):
  """
  DrawMixedCheckBox(graphics: Graphics,x: int,y: int,width: int,height: int,state: ButtonState)

   Draws a three-state check box control in the specified state,on the specified graphics surface,

    and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the check box.

   height: The height of the check box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the check box in.

  

  DrawMixedCheckBox(graphics: Graphics,rectangle: Rectangle,state: ButtonState)

   Draws a three-state check box control in the specified state,on the specified graphics surface,

    and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the check box.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the check box in.
  """
  pass
 @staticmethod
 def DrawRadioButton(graphics,*__args):
  """
  DrawRadioButton(graphics: Graphics,rectangle: Rectangle,state: ButtonState)

   Draws a radio button control in the specified state,on the specified graphics surface,and 

    within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the radio button.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the radio button in.

  

  DrawRadioButton(graphics: Graphics,x: int,y: int,width: int,height: int,state: ButtonState)

   Draws a radio button control in the specified state,on the specified graphics surface,and 

    within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the radio button.

   height: The height of the radio button.

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the radio button in.
  """
  pass
 @staticmethod
 def DrawReversibleFrame(rectangle,backColor,style):
  """
  DrawReversibleFrame(rectangle: Rectangle,backColor: Color,style: FrameStyle)

   Draws a reversible frame on the screen within the specified bounds,with the specified 

    background color,and in the specified state.

  

  

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the rectangle to draw,in screen 

    coordinates.

  

   backColor: The System.Drawing.Color of the background behind the frame.

   style: One of the System.Windows.Forms.FrameStyle values that specifies the style of the frame.
  """
  pass
 @staticmethod
 def DrawReversibleLine(start,end,backColor):
  """
  DrawReversibleLine(start: Point,end: Point,backColor: Color)

   Draws a reversible line on the screen within the specified starting and ending points and with 

    the specified background color.

  

  

   start: The starting System.Drawing.Point of the line,in screen coordinates.

   end: The ending System.Drawing.Point of the line,in screen coordinates.

   backColor: The System.Drawing.Color of the background behind the line.
  """
  pass
 @staticmethod
 def DrawScrollButton(graphics,*__args):
  """
  DrawScrollButton(graphics: Graphics,x: int,y: int,width: int,height: int,button: ScrollButton,state: ButtonState)

   Draws the specified scroll button on a scroll bar control in the specified state,on the 

    specified graphics surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   x: The x-coordinate of the upper left corner of the drawing rectangle.

   y: The y-coordinate of the upper left corner of the drawing rectangle.

   width: The width of the scroll button.

   height: The height of the scroll button.

   button: One of the System.Windows.Forms.ScrollButton values that specifies the type of scroll arrow to 

    draw.

  

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the scroll button in.

  

  DrawScrollButton(graphics: Graphics,rectangle: Rectangle,button: ScrollButton,state: ButtonState)

   Draws the specified scroll button on a scroll bar control in the specified state,on the 

    specified graphics surface,and within the specified bounds.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the glyph.

   button: One of the System.Windows.Forms.ScrollButton values that specifies the type of scroll arrow to 

    draw.

  

   state: A bitwise combination of the System.Windows.Forms.ButtonState values that specifies the state to 

    draw the scroll button in.
  """
  pass
 @staticmethod
 def DrawSelectionFrame(graphics,active,outsideRect,insideRect,backColor):
  """
  DrawSelectionFrame(graphics: Graphics,active: bool,outsideRect: Rectangle,insideRect: Rectangle,backColor: Color)

   Draws a standard selection frame in the specified state,on the specified graphics surface,with 

    the specified inner and outer dimensions,and with the specified background color.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   active: true to draw the selection frame in an active state; otherwise,false.

   outsideRect: The System.Drawing.Rectangle that represents the outer boundary of the selection frame.

   insideRect: The System.Drawing.Rectangle that represents the inner boundary of the selection frame.

   backColor: The System.Drawing.Color of the background behind the frame.
  """
  pass
 @staticmethod
 def DrawSizeGrip(graphics,backColor,*__args):
  """
  DrawSizeGrip(graphics: Graphics,backColor: Color,x: int,y: int,width: int,height: int)

   Draws a size grip on a form with the specified bounds and background color and on the specified 

    graphics surface.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   backColor: The System.Drawing.Color of the background used to determine the colors of the size grip.

   x: The x-coordinate of the upper left corner of the size grip.

   y: The y-coordinate of the upper left corner of the size grip.

   width: The width of the size grip.

   height: The height of the size grip.

  DrawSizeGrip(graphics: Graphics,backColor: Color,bounds: Rectangle)

   Draws a size grip on a form with the specified bounds and background color and on the specified 

    graphics surface.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   backColor: The System.Drawing.Color of the background used to determine the colors of the size grip.

   bounds: The System.Drawing.Rectangle that represents the dimensions of the size grip.
  """
  pass
 @staticmethod
 def DrawStringDisabled(*__args):
  """
  DrawStringDisabled(dc: IDeviceContext,s: str,font: Font,color: Color,layoutRectangle: Rectangle,format: TextFormatFlags)

   Draws the specified string in a disabled state on the specified graphics surface,within the 

    specified bounds,and in the specified font,color,and format,using the specified GDI-based 

    System.Windows.Forms.TextRenderer.

  

  

   dc: The GDI-based System.Windows.Forms.TextRenderer.

   s: The string to draw.

   font: The System.Drawing.Font to draw the string with.

   color: The System.Drawing.Color of the background behind the string.

   layoutRectangle: The System.Drawing.RectangleF that represents the dimensions of the string.

   format: The System.Drawing.StringFormat to apply to the string.

  DrawStringDisabled(graphics: Graphics,s: str,font: Font,color: Color,layoutRectangle: RectangleF,format: StringFormat)

   Draws the specified string in a disabled state on the specified graphics surface; within the 

    specified bounds; and in the specified font,color,and format.

  

  

   graphics: The System.Drawing.Graphics to draw on.

   s: The string to draw.

   font: The System.Drawing.Font to draw the string with.

   color: The System.Drawing.Color of the background behind the string.

   layoutRectangle: The System.Drawing.RectangleF that represents the dimensions of the string.

   format: The System.Drawing.StringFormat to apply to the string.
  """
  pass
 @staticmethod
 def DrawVisualStyleBorder(graphics,bounds):
  """
  DrawVisualStyleBorder(graphics: Graphics,bounds: Rectangle)

   Draws a border in the style appropriate for disabled items.

  

   graphics: The System.Drawing.Graphics to draw on.

   bounds: The System.Drawing.Rectangle that represents the dimensions of the border.
  """
  pass
 @staticmethod
 def FillReversibleRectangle(rectangle,backColor):
  """
  FillReversibleRectangle(rectangle: Rectangle,backColor: Color)

   Draws a filled,reversible rectangle on the screen.

  

   rectangle: The System.Drawing.Rectangle that represents the dimensions of the rectangle to fill,in screen 

    coordinates.

  

   backColor: The System.Drawing.Color of the background behind the fill.
  """
  pass
 @staticmethod
 def Light(baseColor,percOfLightLight=None):
  """
  Light(baseColor: Color) -> Color

  

   Creates a new light color object for the control from the specified color.

  

   baseColor: The System.Drawing.Color to be lightened.

   Returns: A System.Drawing.Color that represents the light color on the control.

  Light(baseColor: Color,percOfLightLight: Single) -> Color

  

   Creates a new light color object for the control from the specified color and lightens it by the 

    specified percentage.

  

  

   baseColor: The System.Drawing.Color to be lightened.

   percOfLightLight: The percentage to lighten the specified System.Drawing.Color.

   Returns: A System.Drawing.Color that represents the light color on the control.
  """
  pass
 @staticmethod
 def LightLight(baseColor):
  """
  LightLight(baseColor: Color) -> Color

  

   Creates a new light color object for the control from the specified color.

  

   baseColor: The System.Drawing.Color to be lightened.

   Returns: A System.Drawing.Color that represents the light color on the control.
  """
  pass
 ContrastControlDark=None

