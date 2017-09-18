class GroupBoxRenderer(object):
 """ Provides methods used to render a group box control with or without visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawGroupBox(g,bounds,*__args):
  """
  DrawGroupBox(g: Graphics,bounds: Rectangle,groupBoxText: str,font: Font,flags: TextFormatFlags,state: GroupBoxState)

   Draws a group box control in the specified state and bounds,with the specified text,font,and 

    text formatting.

  

  

   g: The System.Drawing.Graphics used to draw the group box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the group box.

   groupBoxText: The System.String to draw with the group box.

   font: The System.Drawing.Font to apply to groupBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.

  

  DrawGroupBox(g: Graphics,bounds: Rectangle,groupBoxText: str,font: Font,textColor: Color,flags: TextFormatFlags,state: GroupBoxState)

   Draws a group box control in the specified state and bounds,with the specified text,font,

    color,and text formatting.

  

  

   g: The System.Drawing.Graphics used to draw the group box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the group box.

   groupBoxText: The System.String to draw with the group box.

   font: The System.Drawing.Font to apply to groupBoxText.

   textColor: The System.Drawing.Color to apply to groupBoxText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.

  

  DrawGroupBox(g: Graphics,bounds: Rectangle,groupBoxText: str,font: Font,textColor: Color,state: GroupBoxState)

   Draws a group box control in the specified state and bounds,with the specified text,font,and 

    color.

  

  

   g: The System.Drawing.Graphics used to draw the group box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the group box.

   groupBoxText: The System.String to draw with the group box.

   font: The System.Drawing.Font to apply to groupBoxText.

   textColor: The System.Drawing.Color to apply to groupBoxText.

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.

  

  DrawGroupBox(g: Graphics,bounds: Rectangle,state: GroupBoxState)

   Draws a group box control in the specified state and bounds.

  

   g: The System.Drawing.Graphics used to draw the group box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the group box.

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.

  

  DrawGroupBox(g: Graphics,bounds: Rectangle,groupBoxText: str,font: Font,state: GroupBoxState)

   Draws a group box control in the specified state and bounds,with the specified text and font.

  

   g: The System.Drawing.Graphics used to draw the group box.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the group box.

   groupBoxText: The System.String to draw with the group box.

   font: The System.Drawing.Font to apply to groupBoxText.

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.
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
  IsBackgroundPartiallyTransparent(state: GroupBoxState) -> bool

  

   Indicates whether the background of the group box has any semitransparent or alpha-blended 

    pieces.

  

  

   state: One of the System.Windows.Forms.VisualStyles.GroupBoxState values that specifies the visual 

    state of the group box.

  

   Returns: true if the background of the group box has semitransparent or alpha-blended pieces; otherwise,

    false.
  """
  pass
 RenderMatchingApplicationState=True

