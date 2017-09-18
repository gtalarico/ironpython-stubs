class ComboBoxRenderer(object):
 """ Provides methods used to render a combo box control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawDropDownButton(g,bounds,state):
  """
  DrawDropDownButton(g: Graphics,bounds: Rectangle,state: ComboBoxState)

   Draws a drop-down arrow with the current visual style of the operating system.

  

   g: The System.Drawing.Graphics used to draw the drop-down arrow.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the drop-down arrow.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the drop-down arrow.
  """
  pass
 @staticmethod
 def DrawTextBox(g,bounds,*__args):
  """
  DrawTextBox(g: Graphics,bounds: Rectangle,comboBoxText: str,font: Font,flags: TextFormatFlags,state: ComboBoxState)

   Draws a text box in the specified state and bounds,with the specified text and text formatting.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   comboBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to comboBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,comboBoxText: str,font: Font,textBounds: Rectangle,flags: TextFormatFlags,state: ComboBoxState)

   Draws a text box in the specified state and bounds,with the specified text,text formatting,

    and text bounds.

  

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   comboBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to comboBoxText.

   textBounds: The System.Drawing.Rectangle that specifies the bounds in which to draw comboBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,comboBoxText: str,font: Font,textBounds: Rectangle,state: ComboBoxState)

   Draws a text box in the specified state and bounds,with the specified text and text bounds.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   comboBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to comboBoxText.

   textBounds: The System.Drawing.Rectangle that specifies the bounds in which to draw comboBoxText.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,state: ComboBoxState)

   Draws a text box in the specified state and bounds.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the text box.

  

  DrawTextBox(g: Graphics,bounds: Rectangle,comboBoxText: str,font: Font,state: ComboBoxState)

   Draws a text box in the specified state and bounds,with the specified text.

  

   g: The System.Drawing.Graphics used to draw the text box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the text box.

   comboBoxText: The System.String to draw in the text box.

   font: The System.Drawing.Font to apply to comboBoxText.

   state: One of the System.Windows.Forms.VisualStyles.ComboBoxState values that specifies the visual 

    state of the text box.
  """
  pass
 IsSupported=True

