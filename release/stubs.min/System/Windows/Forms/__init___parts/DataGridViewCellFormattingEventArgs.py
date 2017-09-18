class DataGridViewCellFormattingEventArgs(ConvertEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.CellFormatting event of a System.Windows.Forms.DataGridView.

 

 DataGridViewCellFormattingEventArgs(columnIndex: int,rowIndex: int,value: object,desiredType: Type,cellStyle: DataGridViewCellStyle)
 """
 @staticmethod
 def __new__(self,columnIndex,rowIndex,value,desiredType,cellStyle):
  """ __new__(cls: type,columnIndex: int,rowIndex: int,value: object,desiredType: Type,cellStyle: DataGridViewCellStyle) """
  pass
 CellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style of the cell that is being formatted.



Get: CellStyle(self: DataGridViewCellFormattingEventArgs) -> DataGridViewCellStyle



Set: CellStyle(self: DataGridViewCellFormattingEventArgs)=value

"""

 ColumnIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column index of the cell that is being formatted.



Get: ColumnIndex(self: DataGridViewCellFormattingEventArgs) -> int



"""

 FormattingApplied=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the cell value has been successfully formatted.



Get: FormattingApplied(self: DataGridViewCellFormattingEventArgs) -> bool



Set: FormattingApplied(self: DataGridViewCellFormattingEventArgs)=value

"""

 RowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the row index of the cell that is being formatted.



Get: RowIndex(self: DataGridViewCellFormattingEventArgs) -> int



"""


