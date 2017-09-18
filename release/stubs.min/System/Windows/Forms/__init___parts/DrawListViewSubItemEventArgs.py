class DrawListViewSubItemEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.DrawSubItem event.

 

 DrawListViewSubItemEventArgs(graphics: Graphics,bounds: Rectangle,item: ListViewItem,subItem: ListViewSubItem,itemIndex: int,columnIndex: int,header: ColumnHeader,itemState: ListViewItemStates)
 """
 def DrawBackground(self):
  """
  DrawBackground(self: DrawListViewSubItemEventArgs)

   Draws the background of the System.Windows.Forms.ListViewItem.ListViewSubItem using its current 

    background color.
  """
  pass
 def DrawFocusRectangle(self,bounds):
  """
  DrawFocusRectangle(self: DrawListViewSubItemEventArgs,bounds: Rectangle)

   Draws a focus rectangle for the System.Windows.Forms.ListViewItem.ListViewSubItem if the parent 

    System.Windows.Forms.ListViewItem has focus.

  

  

   bounds: The area within which to draw the focus rectangle.
  """
  pass
 def DrawText(self,flags=None):
  """
  DrawText(self: DrawListViewSubItemEventArgs,flags: TextFormatFlags)

   Draws the text of the System.Windows.Forms.ListViewItem.ListViewSubItem using its current 

    foreground color and formatting it with the specified System.Windows.Forms.TextFormatFlags 

    values.

  

  

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags values.

  DrawText(self: DrawListViewSubItemEventArgs)

   Draws the text of the System.Windows.Forms.ListViewItem.ListViewSubItem using its current 

    foreground color.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,graphics,bounds,item,subItem,itemIndex,columnIndex,header,itemState):
  """ __new__(cls: type,graphics: Graphics,bounds: Rectangle,item: ListViewItem,subItem: ListViewSubItem,itemIndex: int,columnIndex: int,header: ColumnHeader,itemState: ListViewItemStates) """
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the System.Windows.Forms.ListViewItem.ListViewSubItem to draw.



Get: Bounds(self: DrawListViewSubItemEventArgs) -> Rectangle



"""

 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the System.Windows.Forms.ListView column in which the System.Windows.Forms.ListViewItem.ListViewSubItem is displayed.



Get: ColumnIndex(self: DrawListViewSubItemEventArgs) -> int



"""

 DrawDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.ListViewItem.ListViewSubItem should be drawn by the operating system instead of owner-drawn.



Get: DrawDefault(self: DrawListViewSubItemEventArgs) -> bool



Set: DrawDefault(self: DrawListViewSubItemEventArgs)=value

"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to draw the System.Windows.Forms.ListViewItem.ListViewSubItem.



Get: Graphics(self: DrawListViewSubItemEventArgs) -> Graphics



"""

 Header=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the header of the System.Windows.Forms.ListView column in which the System.Windows.Forms.ListViewItem.ListViewSubItem is displayed.



Get: Header(self: DrawListViewSubItemEventArgs) -> ColumnHeader



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the parent System.Windows.Forms.ListViewItem of the System.Windows.Forms.ListViewItem.ListViewSubItem to draw.



Get: Item(self: DrawListViewSubItemEventArgs) -> ListViewItem



"""

 ItemIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the parent System.Windows.Forms.ListViewItem of the System.Windows.Forms.ListViewItem.ListViewSubItem to draw.



Get: ItemIndex(self: DrawListViewSubItemEventArgs) -> int



"""

 ItemState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the parent System.Windows.Forms.ListViewItem of the System.Windows.Forms.ListViewItem.ListViewSubItem to draw.



Get: ItemState(self: DrawListViewSubItemEventArgs) -> ListViewItemStates



"""

 SubItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListViewItem.ListViewSubItem to draw.



Get: SubItem(self: DrawListViewSubItemEventArgs) -> ListViewSubItem



"""


