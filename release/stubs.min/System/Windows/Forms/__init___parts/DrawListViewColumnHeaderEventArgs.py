class DrawListViewColumnHeaderEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.DrawColumnHeader event.

 

 DrawListViewColumnHeaderEventArgs(graphics: Graphics,bounds: Rectangle,columnIndex: int,header: ColumnHeader,state: ListViewItemStates,foreColor: Color,backColor: Color,font: Font)
 """
 def DrawBackground(self):
  """
  DrawBackground(self: DrawListViewColumnHeaderEventArgs)

   Draws the background of the column header.
  """
  pass
 def DrawText(self,flags=None):
  """
  DrawText(self: DrawListViewColumnHeaderEventArgs,flags: TextFormatFlags)

   Draws the column header text,formatting it with the specified 

    System.Windows.Forms.TextFormatFlags values.

  

  

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags values.

  DrawText(self: DrawListViewColumnHeaderEventArgs)

   Draws the column header text using the default formatting.
  """
  pass
 @staticmethod
 def __new__(self,graphics,bounds,columnIndex,header,state,foreColor,backColor,font):
  """ __new__(cls: type,graphics: Graphics,bounds: Rectangle,columnIndex: int,header: ColumnHeader,state: ListViewItemStates,foreColor: Color,backColor: Color,font: Font) """
  pass
 BackColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the background color of the header.



Get: BackColor(self: DrawListViewColumnHeaderEventArgs) -> Color



"""

 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the column header to draw.



Get: Bounds(self: DrawListViewColumnHeaderEventArgs) -> Rectangle



"""

 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the System.Windows.Forms.ColumnHeader representing the header to draw.



Get: ColumnIndex(self: DrawListViewColumnHeaderEventArgs) -> int



"""

 DrawDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the column header should be drawn by the operating system instead of owner-drawn.



Get: DrawDefault(self: DrawListViewColumnHeaderEventArgs) -> bool



Set: DrawDefault(self: DrawListViewColumnHeaderEventArgs)=value

"""

 Font=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the font used to draw the column header text.



Get: Font(self: DrawListViewColumnHeaderEventArgs) -> Font



"""

 ForeColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the foreground color of the header.



Get: ForeColor(self: DrawListViewColumnHeaderEventArgs) -> Color



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to draw the column header.



Get: Graphics(self: DrawListViewColumnHeaderEventArgs) -> Graphics



"""

 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ColumnHeader representing the column header to draw.



Get: Header(self: DrawListViewColumnHeaderEventArgs) -> ColumnHeader



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the column header.



Get: State(self: DrawListViewColumnHeaderEventArgs) -> ListViewItemStates



"""


