class DrawListViewItemEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.ListView.DrawItem event.

 

 DrawListViewItemEventArgs(graphics: Graphics,item: ListViewItem,bounds: Rectangle,itemIndex: int,state: ListViewItemStates)
 """
 def DrawBackground(self):
  """
  DrawBackground(self: DrawListViewItemEventArgs)

   Draws the background of the System.Windows.Forms.ListViewItem using its current background color.
  """
  pass
 def DrawFocusRectangle(self):
  """
  DrawFocusRectangle(self: DrawListViewItemEventArgs)

   Draws a focus rectangle for the System.Windows.Forms.ListViewItem if it has focus.
  """
  pass
 def DrawText(self,flags=None):
  """
  DrawText(self: DrawListViewItemEventArgs,flags: TextFormatFlags)

   Draws the text of the System.Windows.Forms.ListViewItem using its current foreground color and 

    formatting it with the specified System.Windows.Forms.TextFormatFlags values.

  

  

   flags: A bitwise combination of System.Windows.Forms.TextFormatFlags values.

  DrawText(self: DrawListViewItemEventArgs)

   Draws the text of the System.Windows.Forms.ListViewItem using its current foreground color.
  """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 @staticmethod
 def __new__(self,graphics,item,bounds,itemIndex,state):
  """ __new__(cls: type,graphics: Graphics,item: ListViewItem,bounds: Rectangle,itemIndex: int,state: ListViewItemStates) """
  pass
 Bounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the System.Windows.Forms.ListViewItem to draw.



Get: Bounds(self: DrawListViewItemEventArgs) -> Rectangle



"""

 DrawDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a property indicating whether the System.Windows.Forms.ListView control will use the default drawing for the System.Windows.Forms.ListViewItem.



Get: DrawDefault(self: DrawListViewItemEventArgs) -> bool



Set: DrawDefault(self: DrawListViewItemEventArgs)=value

"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to draw the System.Windows.Forms.ListViewItem.



Get: Graphics(self: DrawListViewItemEventArgs) -> Graphics



"""

 Item=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.ListViewItem to draw.



Get: Item(self: DrawListViewItemEventArgs) -> ListViewItem



"""

 ItemIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the System.Windows.Forms.ListViewItem within the System.Windows.Forms.ListView.Items collection of the containing System.Windows.Forms.ListView.



Get: ItemIndex(self: DrawListViewItemEventArgs) -> int



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the current state of the System.Windows.Forms.ListViewItem to draw.



Get: State(self: DrawListViewItemEventArgs) -> ListViewItemStates



"""


