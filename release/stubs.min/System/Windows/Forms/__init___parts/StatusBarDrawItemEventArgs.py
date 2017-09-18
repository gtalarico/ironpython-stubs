class StatusBarDrawItemEventArgs(DrawItemEventArgs):
 """
 Provides data for the System.Windows.Forms.StatusBar.DrawItem event.

 

 StatusBarDrawItemEventArgs(g: Graphics,font: Font,r: Rectangle,itemId: int,itemState: DrawItemState,panel: StatusBarPanel)

 StatusBarDrawItemEventArgs(g: Graphics,font: Font,r: Rectangle,itemId: int,itemState: DrawItemState,panel: StatusBarPanel,foreColor: Color,backColor: Color)
 """
 @staticmethod
 def __new__(self,g,font,r,itemId,itemState,panel,foreColor=None,backColor=None):
  """
  __new__(cls: type,g: Graphics,font: Font,r: Rectangle,itemId: int,itemState: DrawItemState,panel: StatusBarPanel)

  __new__(cls: type,g: Graphics,font: Font,r: Rectangle,itemId: int,itemState: DrawItemState,panel: StatusBarPanel,foreColor: Color,backColor: Color)
  """
  pass
 Panel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Forms.StatusBarPanel to draw.



Get: Panel(self: StatusBarDrawItemEventArgs) -> StatusBarPanel



"""


