class DataGridViewSortCompareEventArgs(HandledEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.SortCompare event.

 

 DataGridViewSortCompareEventArgs(dataGridViewColumn: DataGridViewColumn,cellValue1: object,cellValue2: object,rowIndex1: int,rowIndex2: int)
 """
 @staticmethod
 def __new__(self,dataGridViewColumn,cellValue1,cellValue2,rowIndex1,rowIndex2):
  """ __new__(cls: type,dataGridViewColumn: DataGridViewColumn,cellValue1: object,cellValue2: object,rowIndex1: int,rowIndex2: int) """
  pass
 CellValue1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the first cell to compare.



Get: CellValue1(self: DataGridViewSortCompareEventArgs) -> object



"""

 CellValue2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of the second cell to compare.



Get: CellValue2(self: DataGridViewSortCompareEventArgs) -> object



"""

 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the column being sorted.



Get: Column(self: DataGridViewSortCompareEventArgs) -> DataGridViewColumn



"""

 RowIndex1=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the row containing the first cell to compare.



Get: RowIndex1(self: DataGridViewSortCompareEventArgs) -> int



"""

 RowIndex2=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the index of the row containing the second cell to compare.



Get: RowIndex2(self: DataGridViewSortCompareEventArgs) -> int



"""

 SortResult=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating the order in which the compared cells will be sorted.



Get: SortResult(self: DataGridViewSortCompareEventArgs) -> int



Set: SortResult(self: DataGridViewSortCompareEventArgs)=value

"""


