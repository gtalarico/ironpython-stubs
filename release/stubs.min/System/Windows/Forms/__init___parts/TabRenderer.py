class TabRenderer(object):
 """ Provides methods used to render a tab control with visual styles. This class cannot be inherited. """
 @staticmethod
 def DrawTabItem(g,bounds,*__args):
  """
  DrawTabItem(g: Graphics,bounds: Rectangle,image: Image,imageRectangle: Rectangle,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds,with the specified image,and with an optional 

    focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   image: The System.Drawing.Image to draw in the tab.

   imageRectangle: The System.Drawing.Rectangle that specifies the bounds of image.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,tabItemText: str,font: Font,flags: TextFormatFlags,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds,with the specified text and text formatting,and 

    with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   tabItemText: The System.String to draw in the tab.

   font: The System.Drawing.Font to apply to tabItemText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,tabItemText: str,font: Font,flags: TextFormatFlags,image: Image,imageRectangle: Rectangle,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds; with the specified text,text formatting,and 

    image; and with an optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   tabItemText: The System.String to draw in the tab.

   font: The System.Drawing.Font to apply to tabItemText.

   flags: A bitwise combination of the System.Windows.Forms.TextFormatFlags values.

   image: The System.Drawing.Image to draw in the tab.

   imageRectangle: The System.Drawing.Rectangle that specifies the bounds of image.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,tabItemText: str,font: Font,image: Image,imageRectangle: Rectangle,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds,with the specified text and image,and with an 

    optional focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   tabItemText: The System.String to draw in the tab.

   font: The System.Drawing.Font to apply to tabItemText.

   image: The System.Drawing.Image to draw in the tab.

   imageRectangle: The System.Drawing.Rectangle that specifies the bounds of image.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds,and with an optional focus rectangle.

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,state: TabItemState)

   Draws a tab in the specified state and bounds.

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,tabItemText: str,font: Font,focused: bool,state: TabItemState)

   Draws a tab in the specified state and bounds,with the specified text,and with an optional 

    focus rectangle.

  

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   tabItemText: The System.String to draw in the tab.

   font: The System.Drawing.Font to apply to tabItemText.

   focused: true to draw a focus rectangle; otherwise,false.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.

  

  DrawTabItem(g: Graphics,bounds: Rectangle,tabItemText: str,font: Font,state: TabItemState)

   Draws a tab in the specified state and bounds,and with the specified text.

  

   g: The System.Drawing.Graphics used to draw the tab.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab.

   tabItemText: The System.String to draw in the tab.

   font: The System.Drawing.Font to apply to tabItemText.

   state: One of the System.Windows.Forms.VisualStyles.TabItemState values that specifies the visual state 

    of the tab.
  """
  pass
 @staticmethod
 def DrawTabPage(g,bounds):
  """
  DrawTabPage(g: Graphics,bounds: Rectangle)

   Draws a tab page in the specified bounds.

  

   g: The System.Drawing.Graphics used to draw the tab page.

   bounds: The System.Drawing.Rectangle that specifies the bounds of the tab page.
  """
  pass
 IsSupported=True

