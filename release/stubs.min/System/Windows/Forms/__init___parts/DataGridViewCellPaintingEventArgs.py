class DataGridViewCellPaintingEventArgs(HandledEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.CellPainting event.

 

 DataGridViewCellPaintingEventArgs(dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,columnIndex: int,cellState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts)
 """
 def Paint(self,clipBounds,paintParts):
  """
  Paint(self: DataGridViewCellPaintingEventArgs,clipBounds: Rectangle,paintParts: DataGridViewPaintParts)

   Paints the specified parts of the cell for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.

  

   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values specifying the parts 

    to paint.
  """
  pass
 def PaintBackground(self,clipBounds,cellsPaintSelectionBackground):
  """
  PaintBackground(self: DataGridViewCellPaintingEventArgs,clipBounds: Rectangle,cellsPaintSelectionBackground: bool)

   Paints the cell background for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.

  

   cellsPaintSelectionBackground: true to paint the background of the specified bounds with the color of the 

    System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 

    System.Windows.Forms.DataGridViewCell.InheritedStyle; false to paint the background of the 

    specified bounds with the color of the System.Windows.Forms.DataGridViewCellStyle.BackColor 

    property of the System.Windows.Forms.DataGridViewCell.InheritedStyle.
  """
  pass
 def PaintContent(self,clipBounds):
  """
  PaintContent(self: DataGridViewCellPaintingEventArgs,clipBounds: Rectangle)

   Paints the cell content for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.
  """
  pass
 @staticmethod
 def __new__(self,dataGridView,graphics,clipBounds,cellBounds,rowIndex,columnIndex,cellState,value,formattedValue,errorText,cellStyle,advancedBorderStyle,paintParts):
  """ __new__(cls: type,dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,cellBounds: Rectangle,rowIndex: int,columnIndex: int,cellState: DataGridViewElementStates,value: object,formattedValue: object,errorText: str,cellStyle: DataGridViewCellStyle,advancedBorderStyle: DataGridViewAdvancedBorderStyle,paintParts: DataGridViewPaintParts) """
  pass
 AdvancedBorderStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the border style of the current System.Windows.Forms.DataGridViewCell.



Get: AdvancedBorderStyle(self: DataGridViewCellPaintingEventArgs) -> DataGridViewAdvancedBorderStyle



"""

 CellBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the bounds of the current System.Windows.Forms.DataGridViewCell.



Get: CellBounds(self: DataGridViewCellPaintingEventArgs) -> Rectangle



"""

 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style of the current System.Windows.Forms.DataGridViewCell.



Get: CellStyle(self: DataGridViewCellPaintingEventArgs) -> DataGridViewCellStyle



"""

 ClipBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the area of the System.Windows.Forms.DataGridView that needs to be repainted.



Get: ClipBounds(self: DataGridViewCellPaintingEventArgs) -> Rectangle



"""

 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index of the current System.Windows.Forms.DataGridViewCell.



Get: ColumnIndex(self: DataGridViewCellPaintingEventArgs) -> int



"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string that represents an error message for the current System.Windows.Forms.DataGridViewCell.



Get: ErrorText(self: DataGridViewCellPaintingEventArgs) -> str



"""

 FormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the formatted value of the current System.Windows.Forms.DataGridViewCell.



Get: FormattedValue(self: DataGridViewCellPaintingEventArgs) -> object



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to paint the current System.Windows.Forms.DataGridViewCell.



Get: Graphics(self: DataGridViewCellPaintingEventArgs) -> Graphics



"""

 PaintParts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cell parts that are to be painted.



Get: PaintParts(self: DataGridViewCellPaintingEventArgs) -> DataGridViewPaintParts



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row index of the current System.Windows.Forms.DataGridViewCell.



Get: RowIndex(self: DataGridViewCellPaintingEventArgs) -> int



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the current System.Windows.Forms.DataGridViewCell.



Get: State(self: DataGridViewCellPaintingEventArgs) -> DataGridViewElementStates



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the current System.Windows.Forms.DataGridViewCell.



Get: Value(self: DataGridViewCellPaintingEventArgs) -> object



"""


