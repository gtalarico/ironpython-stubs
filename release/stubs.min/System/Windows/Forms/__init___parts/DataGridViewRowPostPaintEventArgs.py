class DataGridViewRowPostPaintEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.RowPostPaint event.

 

 DataGridViewRowPostPaintEventArgs(dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,errorText: str,inheritedRowStyle: DataGridViewCellStyle,isFirstDisplayedRow: bool,isLastVisibleRow: bool)
 """
 def DrawFocus(self,bounds,cellsPaintSelectionBackground):
  """
  DrawFocus(self: DataGridViewRowPostPaintEventArgs,bounds: Rectangle,cellsPaintSelectionBackground: bool)

   Draws the focus rectangle around the specified bounds.

  

   bounds: A System.Drawing.Rectangle that specifies the focus area.

   cellsPaintSelectionBackground: true to use the System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 

    System.Windows.Forms.DataGridViewRow.InheritedStyle property to determine the color of the focus 

    rectangle; false to use the System.Windows.Forms.DataGridViewCellStyle.BackColor property of the 

    System.Windows.Forms.DataGridViewRow.InheritedStyle property.
  """
  pass
 def PaintCells(self,clipBounds,paintParts):
  """
  PaintCells(self: DataGridViewRowPostPaintEventArgs,clipBounds: Rectangle,paintParts: DataGridViewPaintParts)

   Paints the specified cell parts for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.

  

   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values specifying the parts 

    to paint.
  """
  pass
 def PaintCellsBackground(self,clipBounds,cellsPaintSelectionBackground):
  """
  PaintCellsBackground(self: DataGridViewRowPostPaintEventArgs,clipBounds: Rectangle,cellsPaintSelectionBackground: bool)

   Paints the cell backgrounds for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.

  

   cellsPaintSelectionBackground: true to paint the background of the specified bounds with the color of the 

    System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 

    System.Windows.Forms.DataGridViewRow.InheritedStyle; false to paint the background of the 

    specified bounds with the color of the System.Windows.Forms.DataGridViewCellStyle.BackColor 

    property of the System.Windows.Forms.DataGridViewRow.InheritedStyle.
  """
  pass
 def PaintCellsContent(self,clipBounds):
  """
  PaintCellsContent(self: DataGridViewRowPostPaintEventArgs,clipBounds: Rectangle)

   Paints the cell contents for the area in the specified bounds.

  

   clipBounds: A System.Drawing.Rectangle that specifies the area of the System.Windows.Forms.DataGridView to 

    be painted.
  """
  pass
 def PaintHeader(self,*__args):
  """
  PaintHeader(self: DataGridViewRowPostPaintEventArgs,paintParts: DataGridViewPaintParts)

   Paints the specified parts of the row header of the current row.

  

   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values specifying the parts 

    to paint.

  

  PaintHeader(self: DataGridViewRowPostPaintEventArgs,paintSelectionBackground: bool)

   Paints the entire row header of the current System.Windows.Forms.DataGridViewRow.

  

   paintSelectionBackground: true to paint the row header with the color of the 

    System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 

    System.Windows.Forms.DataGridViewRow.InheritedStyle; false to paint the row header with the 

    System.Windows.Forms.DataGridViewCellStyle.BackColor of the 

    System.Windows.Forms.DataGridView.RowHeadersDefaultCellStyle property.
  """
  pass
 @staticmethod
 def __new__(self,dataGridView,graphics,clipBounds,rowBounds,rowIndex,rowState,errorText,inheritedRowStyle,isFirstDisplayedRow,isLastVisibleRow):
  """ __new__(cls: type,dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,errorText: str,inheritedRowStyle: DataGridViewCellStyle,isFirstDisplayedRow: bool,isLastVisibleRow: bool) """
  pass
 ClipBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the area of the System.Windows.Forms.DataGridView that needs to be repainted.



Get: ClipBounds(self: DataGridViewRowPostPaintEventArgs) -> Rectangle



Set: ClipBounds(self: DataGridViewRowPostPaintEventArgs)=value

"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string that represents an error message for the current System.Windows.Forms.DataGridViewRow.



Get: ErrorText(self: DataGridViewRowPostPaintEventArgs) -> str



"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to paint the current System.Windows.Forms.DataGridViewRow.



Get: Graphics(self: DataGridViewRowPostPaintEventArgs) -> Graphics



"""

 InheritedRowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style applied to the current System.Windows.Forms.DataGridViewRow.



Get: InheritedRowStyle(self: DataGridViewRowPostPaintEventArgs) -> DataGridViewCellStyle



"""

 IsFirstDisplayedRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current row is the first row displayed in the System.Windows.Forms.DataGridView.



Get: IsFirstDisplayedRow(self: DataGridViewRowPostPaintEventArgs) -> bool



"""

 IsLastVisibleRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current row is the last visible row displayed in the System.Windows.Forms.DataGridView.



Get: IsLastVisibleRow(self: DataGridViewRowPostPaintEventArgs) -> bool



"""

 RowBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the bounds of the current System.Windows.Forms.DataGridViewRow.



Get: RowBounds(self: DataGridViewRowPostPaintEventArgs) -> Rectangle



"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the current System.Windows.Forms.DataGridViewRow.



Get: RowIndex(self: DataGridViewRowPostPaintEventArgs) -> int



"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the current System.Windows.Forms.DataGridViewRow.



Get: State(self: DataGridViewRowPostPaintEventArgs) -> DataGridViewElementStates



"""


