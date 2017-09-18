class DrawToolTipEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ToolTip.Draw event.

 

 DrawToolTipEventArgs(graphics: Graphics,associatedWindow: IWin32Window,associatedControl: Control,bounds: Rectangle,toolTipText: str,backColor: Color,foreColor: Color,font: Font)
 """
 def DrawBackground(self):
  """
  DrawBackground(self: DrawToolTipEventArgs)

   Draws the background of the System.Windows.Forms.ToolTip using the system background color.
  """
  pass
 def DrawBorder(self):
  """
  DrawBorder(self: DrawToolTipEventArgs)

   Draws the border of the System.Windows.Forms.ToolTip using the system border color.
  """
  pass
 def DrawText(self,flags=None):
  """
  DrawText(self: DrawToolTipEventArgs,flags: TextFormatFlags)

   Draws the text of the System.Windows.Forms.ToolTip using the system text color and font,and the 

    specified text layout.

  

  

   flags: A System.Windows.Forms.TextFormatFlags containing a bitwise combination of values that specifies 

    the display and layout for the System.Windows.Forms.DrawToolTipEventArgs.ToolTipText.

  

  DrawText(self: DrawToolTipEventArgs)

   Draws the text of the System.Windows.Forms.ToolTip using the system text color and font.
  """
  pass
 @staticmethod
 def __new__(self,graphics,associatedWindow,associatedControl,bounds,toolTipText,backColor,foreColor,font):
  """ __new__(cls: type,graphics: Graphics,associatedWindow: IWin32Window,associatedControl: Control,bounds: Rectangle,toolTipText: str,backColor: Color,foreColor: Color,font: Font) """
  pass
 AssociatedControl=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the control for which the System.Windows.Forms.ToolTip is being drawn.



Get: AssociatedControl(self: DrawToolTipEventArgs) -> Control



"""

 AssociatedWindow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window to which this System.Windows.Forms.ToolTip is bound.



Get: AssociatedWindow(self: DrawToolTipEventArgs) -> IWin32Window



"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the System.Windows.Forms.ToolTip to draw.



Get: Bounds(self: DrawToolTipEventArgs) -> Rectangle



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font used to draw the System.Windows.Forms.ToolTip.



Get: Font(self: DrawToolTipEventArgs) -> Font



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the graphics surface used to draw the System.Windows.Forms.ToolTip.



Get: Graphics(self: DrawToolTipEventArgs) -> Graphics



"""

 ToolTipText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the text for the System.Windows.Forms.ToolTip that is being drawn.



Get: ToolTipText(self: DrawToolTipEventArgs) -> str



"""


