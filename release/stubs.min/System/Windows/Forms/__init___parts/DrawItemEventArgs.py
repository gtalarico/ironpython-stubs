class DrawItemEventArgs(EventArgs):
 """
 Provides data for the DrawItem event.

 

 DrawItemEventArgs(graphics: Graphics,font: Font,rect: Rectangle,index: int,state: DrawItemState)

 DrawItemEventArgs(graphics: Graphics,font: Font,rect: Rectangle,index: int,state: DrawItemState,foreColor: Color,backColor: Color)
 """
 def DrawBackground(self):
  """
  DrawBackground(self: DrawItemEventArgs)

   Draws the background within the bounds specified in the 

    erload:System.Windows.Forms.DrawItemEventArgs.#ctor constructor and with the appropriate color.
  """
  pass
 def DrawFocusRectangle(self):
  """
  DrawFocusRectangle(self: DrawItemEventArgs)

   Draws a focus rectangle within the bounds specified in the 

    erload:System.Windows.Forms.DrawItemEventArgs.#ctor constructor.
  """
  pass
 @staticmethod
 def __new__(self,graphics,font,rect,index,state,foreColor=None,backColor=None):
  """
  __new__(cls: type,graphics: Graphics,font: Font,rect: Rectangle,index: int,state: DrawItemState)

  __new__(cls: type,graphics: Graphics,font: Font,rect: Rectangle,index: int,state: DrawItemState,foreColor: Color,backColor: Color)
  """
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the background color of the item that is being drawn.



Get: BackColor(self: DrawItemEventArgs) -> Color



"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the rectangle that represents the bounds of the item that is being drawn.



Get: Bounds(self: DrawItemEventArgs) -> Rectangle



"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font that is assigned to the item being drawn.



Get: Font(self: DrawItemEventArgs) -> Font



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the foreground color of the of the item being drawn.



Get: ForeColor(self: DrawItemEventArgs) -> Color



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the graphics surface to draw the item on.



Get: Graphics(self: DrawItemEventArgs) -> Graphics



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index value of the item that is being drawn.



Get: Index(self: DrawItemEventArgs) -> int



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the item being drawn.



Get: State(self: DrawItemEventArgs) -> DrawItemState



"""


