class TextBoxRenderer(object):
 """ Provides methods used to render a text box control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawTextBox(g,bounds,*__args):
  """
  DrawTextBox(g: Graphics,bounds: Rectangle,textBoxText: str,font: Font,flags: TextFormatFlags,state: TextBoxState)

   Draws a text box control in the specified state and bounds,and with the specified text and text 

    formatting.

  

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   textBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to textBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.TextBoxState values that specifies the visual state 

    of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,textBoxText: str,font: Font,textBounds: Rectangle,flags: TextFormatFlags,state: TextBoxState)

   Draws a text box control in the specified state and bounds,and with the specified text,text 

    bounds,and text formatting.

  

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   textBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to textBoxText.

   textBounds: The System.Drawing.Rectangle that specifies the bounds of textBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.TextBoxState values that specifies the visual state 

    of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,textBoxText: str,font: Font,textBounds: Rectangle,state: TextBoxState)

   Draws a text box control in the specified state and bounds,and with the specified text and text 

    bounds.

  

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   textBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to textBoxText.

   textBounds: The System.Drawing.Rectangle that specifies the bounds of textBoxText.

   state: One of the System.Windows.Forms.VisualStyles.TextBoxState values that specifies the visual state 

    of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,state: TextBoxState)

   Draws a text box control in the specified state and bounds.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   state: One of the System.Windows.Forms.VisualStyles.TextBoxState values that specifies the visual state 

    of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,textBoxText: str,font: Font,state: TextBoxState)

   Draws a text box control in the specified state and bounds,and with the specified text.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   textBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to textBoxText.

   state: One of the System.Windows.Forms.VisualStyles.TextBoxState values that specifies the visual state 

    of the text box.
  """
  pass
 IsSupported=True

