class MeasureItemEventArgs(EventArgs):
 """
 Provides data for the MeasureItem event of the System.Windows.Forms.ListBox,System.Windows.Forms.ComboBox,System.Windows.Forms.CheckedListBox,and System.Windows.Forms.MenuItem controls.

 

 MeasureItemEventArgs(graphics: Graphics,index: int,itemHeight: int)

 MeasureItemEventArgs(graphics: Graphics,index: int)
 """
 @staticmethod
 def __new__(self,graphics,index,itemHeight=None):
  """
  __new__(cls: type,graphics: Graphics,index: int,itemHeight: int)

  __new__(cls: type,graphics: Graphics,index: int)
  """
  pass
 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics object to measure against.



Get: Graphics(self: MeasureItemEventArgs) -> Graphics



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the item for which the height and width is needed.



Get: Index(self: MeasureItemEventArgs) -> int



"""

 ItemHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of the item specified by the System.Windows.Forms.MeasureItemEventArgs.Index.



Get: ItemHeight(self: MeasureItemEventArgs) -> int



Set: ItemHeight(self: MeasureItemEventArgs)=value

"""

 ItemWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the item specified by the System.Windows.Forms.MeasureItemEventArgs.Index.



Get: ItemWidth(self: MeasureItemEventArgs) -> int



Set: ItemWidth(self: MeasureItemEventArgs)=value

"""


