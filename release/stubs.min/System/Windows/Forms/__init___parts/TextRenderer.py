class TextRenderer(object):
 """ Provides methods used to measure and render text. This class cannot be inherited. """
 @staticmethod
 def DrawText(dc,text,font,*__args):
  """
  DrawText(dc: IDeviceContext,text: str,font: Font,bounds: Rectangle,foreColor: Color,backColor: Color)

   Draws the specified text within the specified bounds using the specified device context,font,

    color,and back color.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   bounds: The System.Drawing.Rectangle that represents the bounds of the text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

   backColor: The System.Drawing.Color to apply to the area represented by bounds.

  DrawText(dc: IDeviceContext,text: str,font: Font,bounds: Rectangle,foreColor: Color)

   Draws the specified text within the specified bounds,using the specified device context,font,

    and color.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   bounds: The System.Drawing.Rectangle that represents the bounds of the text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

  DrawText(dc: IDeviceContext,text: str,font: Font,bounds: Rectangle,foreColor: Color,backColor: Color,flags: TextFormatFlags)

   Draws the specified text within the specified bounds using the specified device context,font,

    color,back color,and formatting instructions.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   bounds: The System.Drawing.Rectangle that represents the bounds of the text.

   foreColor: The System.Drawing.Color to apply to the text.

   backColor: The System.Drawing.Color to apply to the area represented by bounds.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

  DrawText(dc: IDeviceContext,text: str,font: Font,bounds: Rectangle,foreColor: Color,flags: TextFormatFlags)

   Draws the specified text within the specified bounds using the specified device context,font,

    color,and formatting instructions.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   bounds: The System.Drawing.Rectangle that represents the bounds of the text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

  DrawText(dc: IDeviceContext,text: str,font: Font,pt: Point,foreColor: Color,backColor: Color)

   Draws the specified text at the specified location,using the specified device context,font,

    color,and back color.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   pt: The System.Drawing.Point that represents the upper-left corner of the drawn text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

   backColor: The System.Drawing.Color to apply to the background area of the drawn text.

  DrawText(dc: IDeviceContext,text: str,font: Font,pt: Point,foreColor: Color)

   Draws the specified text at the specified location using the specified device context,font,and 

    color.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   pt: The System.Drawing.Point that represents the upper-left corner of the drawn text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

  DrawText(dc: IDeviceContext,text: str,font: Font,pt: Point,foreColor: Color,backColor: Color,flags: TextFormatFlags)

   Draws the specified text at the specified location using the specified device context,font,

    color,back color,and formatting instructions

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   pt: The System.Drawing.Point that represents the upper-left corner of the drawn text.

   foreColor: The System.Drawing.Color to apply to the text.

   backColor: The System.Drawing.Color to apply to the background area of the drawn text.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

  DrawText(dc: IDeviceContext,text: str,font: Font,pt: Point,foreColor: Color,flags: TextFormatFlags)

   Draws the specified text at the specified location using the specified device context,font,

    color,and formatting instructions.

  

  

   dc: The device context in which to draw the text.

   text: The text to draw.

   font: The System.Drawing.Font to apply to the drawn text.

   pt: The System.Drawing.Point that represents the upper-left corner of the drawn text.

   foreColor: The System.Drawing.Color to apply to the drawn text.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.
  """
  pass
 @staticmethod
 def MeasureText(*__args):
  """
  MeasureText(dc: IDeviceContext,text: str,font: Font) -> Size

  

   Provides the size,in pixels,of the specified text drawn with the specified font in the 

    specified device context.

  

  

   dc: The device context in which to measure the text.

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   Returns: The System.Drawing.Size,in pixels,of text drawn in a single line with the specified font in 

    the specified device context.

  

  MeasureText(dc: IDeviceContext,text: str,font: Font,proposedSize: Size) -> Size

  

   Provides the size,in pixels,of the specified text when drawn with the specified font in the 

    specified device context,using the specified size to create an initial bounding rectangle for 

    the text.

  

  

   dc: The device context in which to measure the text.

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   proposedSize: The System.Drawing.Size of the initial bounding rectangle.

   Returns: The System.Drawing.Size,in pixels,of text drawn with the specified font.

  MeasureText(dc: IDeviceContext,text: str,font: Font,proposedSize: Size,flags: TextFormatFlags) -> Size

  

   Provides the size,in pixels,of the specified text when drawn with the specified device 

    context,font,and formatting instructions,using the specified size to create the initial 

    bounding rectangle for the text.

  

  

   dc: The device context in which to measure the text.

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   proposedSize: The System.Drawing.Size of the initial bounding rectangle.

   flags: The formatting instructions to apply to the measured text.

   Returns: The System.Drawing.Size,in pixels,of text drawn with the specified font and format.

  MeasureText(text: str,font: Font) -> Size

  

   Provides the size,in pixels,of the specified text when drawn with the specified font.

  

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   Returns: The System.Drawing.Size,in pixels,of text drawn on a single line with the specified font. You 

    can manipulate how the text is drawn by using one of the 

    System.Windows.Forms.TextRenderer.DrawText(System.Drawing.IDeviceContext,System.String,System.Dra

    wing.Font,System.Drawing.Rectangle,System.Drawing.Color,System.Windows.Forms.TextFormatFlags) 

    overloads that takes a System.Windows.Forms.TextFormatFlags parameter. For example,the default 

    behavior of the System.Windows.Forms.TextRenderer is to add padding to the bounding rectangle of 

    the drawn text to accommodate overhanging glyphs. If you need to draw a line of text without 

    these extra spaces you should use the versions of 

    System.Windows.Forms.TextRenderer.DrawText(System.Drawing.IDeviceContext,System.String,System.Dra

    wing.Font,System.Drawing.Point,System.Drawing.Color) and 

    System.Windows.Forms.TextRenderer.MeasureText(System.Drawing.IDeviceContext,System.String,System.

    Drawing.Font) that take a System.Drawing.Size and System.Windows.Forms.TextFormatFlags 

    parameter. For an example,see 

    System.Windows.Forms.TextRenderer.MeasureText(System.Drawing.IDeviceContext,System.String,System.

    Drawing.Font,System.Drawing.Size,System.Windows.Forms.TextFormatFlags).

  

  MeasureText(text: str,font: Font,proposedSize: Size,flags: TextFormatFlags) -> Size

  

   Provides the size,in pixels,of the specified text when drawn with the specified font and 

    formatting instructions,using the specified size to create the initial bounding rectangle for 

    the text.

  

  

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   proposedSize: The System.Drawing.Size of the initial bounding rectangle.

   flags: The formatting instructions to apply to the measured text.

   Returns: The System.Drawing.Size,in pixels,of text drawn with the specified font and format.

  MeasureText(text: str,font: Font,proposedSize: Size) -> Size

  

   Provides the size,in pixels,of the specified text when drawn with the specified font,using 

    the specified size to create an initial bounding rectangle.

  

  

   text: The text to measure.

   font: The System.Drawing.Font to apply to the measured text.

   proposedSize: The System.Drawing.Size of the initial bounding rectangle.

   Returns: The System.Drawing.Size,in pixels,of text drawn with the specified font.
  """
  pass
