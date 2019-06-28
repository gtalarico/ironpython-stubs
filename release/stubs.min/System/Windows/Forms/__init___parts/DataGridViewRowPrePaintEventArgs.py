class DataGridViewRowPrePaintEventArgs:
 """
 Provides data for the System.Windows.Forms.DataGridView.RowPrePaint event.
 
 DataGridViewRowPrePaintEventArgs(dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,errorText: str,inheritedRowStyle: DataGridViewCellStyle,isFirstDisplayedRow: bool,isLastVisibleRow: bool)
 """
 def DrawFocus(self,bounds,cellsPaintSelectionBackground):
  """
  DrawFocus(self: DataGridViewRowPrePaintEventArgs,bounds: Rectangle,cellsPaintSelectionBackground: bool)
   Draws the focus rectangle around the specified bounds.
  
   bounds: A System.Drawing.Rectangle that specifies the focus area.
   cellsPaintSelectionBackground: true to use the System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of 
    the System.Windows.Forms.DataGridViewRow.InheritedStyle property to determine the color 
    of the focus rectangle; false to use the 
    System.Windows.Forms.DataGridViewCellStyle.BackColor property of the 
    System.Windows.Forms.DataGridViewRow.InheritedStyle.
  """
  pass
 def PaintCells(self,clipBounds,paintParts):
  """
  PaintCells(self: DataGridViewRowPrePaintEventArgs,clipBounds: Rectangle,paintParts: DataGridViewPaintParts)
   Paints the specified cell parts for the area in the specified bounds.
  
   clipBounds: A System.Drawing.Rectangle that specifies the area of the 
    System.Windows.Forms.DataGridView to be painted.
  
   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values specifying 
    the parts to paint.
  """
  pass
 def PaintCellsBackground(self,clipBounds,cellsPaintSelectionBackground):
  """
  PaintCellsBackground(self: DataGridViewRowPrePaintEventArgs,clipBounds: Rectangle,cellsPaintSelectionBackground: bool)
   Paints the cell backgrounds for the area in the specified bounds.
  
   clipBounds: A System.Drawing.Rectangle that specifies the area of the 
    System.Windows.Forms.DataGridView to be painted.
  
   cellsPaintSelectionBackground: true to paint the background of the specified bounds with the color of the 
    System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 
    System.Windows.Forms.DataGridViewRow.InheritedStyle; false to paint the background of the 
    specified bounds with the color of the 
    System.Windows.Forms.DataGridViewCellStyle.BackColor property of the 
    System.Windows.Forms.DataGridViewRow.InheritedStyle.
  """
  pass
 def PaintCellsContent(self,clipBounds):
  """
  PaintCellsContent(self: DataGridViewRowPrePaintEventArgs,clipBounds: Rectangle)
   Paints the cell contents for the area in the specified bounds.
  
   clipBounds: A System.Drawing.Rectangle that specifies the area of the 
    System.Windows.Forms.DataGridView to be painted.
  """
  pass
 def PaintHeader(self,*__args):
  """
  PaintHeader(self: DataGridViewRowPrePaintEventArgs,paintSelectionBackground: bool)
   Paints the entire row header of the current System.Windows.Forms.DataGridViewRow.
  
   paintSelectionBackground: true to paint the row header with the color of the 
    System.Windows.Forms.DataGridViewCellStyle.SelectionBackColor property of the 
    System.Windows.Forms.DataGridViewRow.InheritedStyle; false to paint the row header with 
    the System.Windows.Forms.DataGridViewCellStyle.BackColor of the 
    System.Windows.Forms.DataGridView.RowHeadersDefaultCellStyle property.
  
  PaintHeader(self: DataGridViewRowPrePaintEventArgs,paintParts: DataGridViewPaintParts)
   Paints the specified parts of the row header of the current row.
  
   paintParts: A bitwise combination of System.Windows.Forms.DataGridViewPaintParts values specifying 
    the parts to paint.
  """
  pass
 @staticmethod
 def __new__(self,dataGridView,graphics,clipBounds,rowBounds,rowIndex,rowState,errorText,inheritedRowStyle,isFirstDisplayedRow,isLastVisibleRow):
  """ __new__(cls: type,dataGridView: DataGridView,graphics: Graphics,clipBounds: Rectangle,rowBounds: Rectangle,rowIndex: int,rowState: DataGridViewElementStates,errorText: str,inheritedRowStyle: DataGridViewCellStyle,isFirstDisplayedRow: bool,isLastVisibleRow: bool) """
  pass
 ClipBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the area of the System.Windows.Forms.DataGridView that needs to be repainted.

Get: ClipBounds(self: DataGridViewRowPrePaintEventArgs) -> Rectangle

Set: ClipBounds(self: DataGridViewRowPrePaintEventArgs)=value
"""

 ErrorText=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a string that represents an error message for the current System.Windows.Forms.DataGridViewRow.

Get: ErrorText(self: DataGridViewRowPrePaintEventArgs) -> str

"""

 Graphics=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Drawing.Graphics used to paint the current System.Windows.Forms.DataGridViewRow.

Get: Graphics(self: DataGridViewRowPrePaintEventArgs) -> Graphics

"""

 InheritedRowStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style applied to the row.

Get: InheritedRowStyle(self: DataGridViewRowPrePaintEventArgs) -> DataGridViewCellStyle

"""

 IsFirstDisplayedRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current row is the first row currently displayed in the System.Windows.Forms.DataGridView.

Get: IsFirstDisplayedRow(self: DataGridViewRowPrePaintEventArgs) -> bool

"""

 IsLastVisibleRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the current row is the last visible row in the System.Windows.Forms.DataGridView.

Get: IsLastVisibleRow(self: DataGridViewRowPrePaintEventArgs) -> bool

"""

 PaintParts=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The cell parts that are to be painted.

Get: PaintParts(self: DataGridViewRowPrePaintEventArgs) -> DataGridViewPaintParts

Set: PaintParts(self: DataGridViewRowPrePaintEventArgs)=value
"""

 RowBounds=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the bounds of the current System.Windows.Forms.DataGridViewRow.

Get: RowBounds(self: DataGridViewRowPrePaintEventArgs) -> Rectangle

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the current System.Windows.Forms.DataGridViewRow.

Get: RowIndex(self: DataGridViewRowPrePaintEventArgs) -> int

"""

 State=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the state of the current System.Windows.Forms.DataGridViewRow.

Get: State(self: DataGridViewRowPrePaintEventArgs) -> DataGridViewElementStates

"""


