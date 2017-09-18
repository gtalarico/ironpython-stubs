class TableLayoutCellPaintEventArgs(PaintEventArgs,IDisposable):
 """
 Provides data for the System.Windows.Forms.TableLayoutPanel.CellPaint event.

 

 TableLayoutCellPaintEventArgs(g: Graphics,clipRectangle: Rectangle,cellBounds: Rectangle,column: int,row: int)
 """
 def Dispose(self):
  """
  Dispose(self: PaintEventArgs,disposing: bool)

   Releases the unmanaged resources used by the System.Windows.Forms.PaintEventArgs and optionally 

    releases the managed resources.

  

  

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,g,clipRectangle,cellBounds,column,row):
  """ __new__(cls: type,g: Graphics,clipRectangle: Rectangle,cellBounds: Rectangle,column: int,row: int) """
  pass
 CellBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the size and location of the cell.



Get: CellBounds(self: TableLayoutCellPaintEventArgs) -> Rectangle



"""

 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column of the cell.



Get: Column(self: TableLayoutCellPaintEventArgs) -> int



"""

 Row=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row of the cell.



Get: Row(self: TableLayoutCellPaintEventArgs) -> int



"""


