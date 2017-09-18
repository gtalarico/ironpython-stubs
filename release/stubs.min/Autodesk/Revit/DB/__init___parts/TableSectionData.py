class TableSectionData(object,IDisposable):
 """
 The TableSectionData class represents a serialized version of an instance of

    section table data. The class holds row,column and cell data.
 """
 def AllowOverrideCellStyle(self,nRow,nCol):
  """
  AllowOverrideCellStyle(self: TableSectionData,nRow: int,nCol: int) -> bool

  

   Identifies if the style can be overridden in the given cell.

   Returns: True if allow to override cell style.
  """
  pass
 def CanInsertColumn(self,nIndex):
  """
  CanInsertColumn(self: TableSectionData,nIndex: int) -> bool

  

   Verifies if a new column can be inserted at the given index.

  

   nIndex: An integer index.

   Returns: True if the column can be inserted,false otherwise.
  """
  pass
 def CanInsertRow(self,nIndex):
  """
  CanInsertRow(self: TableSectionData,nIndex: int) -> bool

  

   Verifies if a new row can be inserted at the given index.

   Returns: True if the row can be inserted,false otherwise.
  """
  pass
 def CanRemoveColumn(self,nIndex):
  """
  CanRemoveColumn(self: TableSectionData,nIndex: int) -> bool

  

   Verifies that if the column at the given index can be removed.

  

   nIndex: An integer index.

   Returns: True if the column can be removed,false otherwise.
  """
  pass
 def CanRemoveRow(self,nIndex):
  """
  CanRemoveRow(self: TableSectionData,nIndex: int) -> bool

  

   Verifies that if the row at the given index can be removed..

  

   nIndex: An integer index.

   Returns: True if the row can be removed,false otherwise
  """
  pass
 def ClearCell(self,nRow,nCol):
  """
  ClearCell(self: TableSectionData,nRow: int,nCol: int)

   Deletes text or image,or removes parameter of this cell.
  """
  pass
 def Dispose(self):
  """ Dispose(self: TableSectionData) """
  pass
 def GetCellCalculatedValue(self,*__args):
  """
  GetCellCalculatedValue(self: TableSectionData,nRow: int,nCol: int) -> TableCellCalculatedValueData

  

   Gets the calculated value for the specified cell

  GetCellCalculatedValue(self: TableSectionData,nCol: int) -> TableCellCalculatedValueData

  

   Gets the calculated value for the specified column
  """
  pass
 def GetCellCategoryId(self,*__args):
  """
  GetCellCategoryId(self: TableSectionData,nRow: int,nCol: int) -> ElementId

  

   Returns a cell's CategoryId and if no CategoryId exists for this cell,

     it 

    would come from the column.

     Associated with the paramId to find the correct 

    element.

  

  GetCellCategoryId(self: TableSectionData,nCol: int) -> ElementId

  

   Returns a column's ParamId

     Associated with the paramId to find the correct 

    element
  """
  pass
 def GetCellCombinedParameters(self,*__args):
  """
  GetCellCombinedParameters(self: TableSectionData,nRow: int,nCol: int) -> IList[TableCellCombinedParameterData]

  

   Returns an array of combined parameter data for the specified cell

  GetCellCombinedParameters(self: TableSectionData,nCol: int) -> IList[TableCellCombinedParameterData]

  

   Returns an array of combined parameter data for the specified column
  """
  pass
 def GetCellFormatOptions(self,*__args):
  """
  GetCellFormatOptions(self: TableSectionData,nRow: int,nCol: int,ccda: Document) -> FormatOptions

  

   Returns a cell's FormatOptions and if no FormatOptions exists for this cell,

    

     it would come from the column,or the row,or the section.

  

  GetCellFormatOptions(self: TableSectionData,nCol: int,ccda: Document) -> FormatOptions

  

   Returns a column's cell FormatOptions and if no FormatOptions exists for this 

    column,

     it would come from the section.
  """
  pass
 def GetCellParamId(self,*__args):
  """
  GetCellParamId(self: TableSectionData,nRow: int,nCol: int) -> ElementId

  

   Returns a cell's ParamId and if no ParamId exists for this cell,

     it would 

    come from the column

  

  GetCellParamId(self: TableSectionData,nCol: int) -> ElementId

  

   Returns a column's ParamId
  """
  pass
 def GetCellText(self,nRow,nCol):
  """
  GetCellText(self: TableSectionData,nRow: int,nCol: int) -> str

  

   Returns the text shown by this cell,if the cell's type is CellType.Text or 

    CellType.ParameterText.

  

  

   nRow: The cell row.

   nCol: The cell column.

   Returns: The text in the cell,or an empty string if the type if not CellType.Text or 

    CellType.ParameterText.
  """
  pass
 def GetCellType(self,*__args):
  """
  GetCellType(self: TableSectionData,nRow: int,nCol: int) -> CellType

  

   Returns a cell's Type and if no Type exists for this cell,

     it would come 

    from the column,or the row,or the section

  

  GetCellType(self: TableSectionData,nCol: int) -> CellType

  

   Returns a column's cell type and if no type exists for this column,

     it 

    would come from the section
  """
  pass
 def GetCellUnitType(self,nRow,nCol):
  """
  GetCellUnitType(self: TableSectionData,nRow: int,nCol: int) -> UnitType

  

   Gets the unit type of a cell,if applicable.

  

   nRow: The row index of the cell

   nCol: The column index of the cell

   Returns: The unit type,or UT_Undefined if the cell does not contain a number with units.
  """
  pass
 def GetColumnWidth(self,nCol):
  """
  GetColumnWidth(self: TableSectionData,nCol: int) -> float

  

   Returns a column's width in feet
  """
  pass
 def GetColumnWidthInPixels(self,nCol):
  """
  GetColumnWidthInPixels(self: TableSectionData,nCol: int) -> int

  

   This returns a column's width in pixels
  """
  pass
 def GetMergedCell(self,nRow,nCol):
  """
  GetMergedCell(self: TableSectionData,nRow: int,nCol: int) -> TableMergedCell

  

   Gets the whole merged cell that this cell is a part of.

  

   nRow: The cell row.

   nCol: The cell column.
  """
  pass
 def GetRowHeight(self,nRow):
  """
  GetRowHeight(self: TableSectionData,nRow: int) -> float

  

   Returns a row's height in feet
  """
  pass
 def GetRowHeightInPixels(self,nRow):
  """
  GetRowHeightInPixels(self: TableSectionData,nRow: int) -> int

  

   This returns a row's height in pixels
  """
  pass
 def GetTableCellStyle(self,nRow,nCol):
  """
  GetTableCellStyle(self: TableSectionData,nRow: int,nCol: int) -> TableCellStyle

  

   Returns a cell's style and if no style exists for this cell,

     it would come 

    from the column,or the section
  """
  pass
 def InsertColumn(self,index):
  """
  InsertColumn(self: TableSectionData,index: int)

   Inserts a new column at the specified index relative to the current set of 

    columns.

  

  

   index: An integer index.
  """
  pass
 def InsertImage(self,nRow,nColumn,imageSymbolId):
  """
  InsertImage(self: TableSectionData,nRow: int,nColumn: int,imageSymbolId: ElementId)

   Inserts a image in the given cell.

  

   nRow: The given row index.

   nColumn: The given column index.

   imageSymbolId: The element id of the image symbol.
  """
  pass
 def InsertRow(self,nIndex):
  """
  InsertRow(self: TableSectionData,nIndex: int)

   Inserts a row data at a specified index.

  

   nIndex: An integer index.
  """
  pass
 def IsAcceptableParamIdAndCategoryId(self,*__args):
  """
  IsAcceptableParamIdAndCategoryId(self: TableSectionData,paramId: ElementId,categoryId: ElementId) -> bool

  

   Identifies if the given parameter id and category id can be assigned to a cell 

    in this table.

  

   Returns: True if the ParamId and CategoryId are all acceptable.

  IsAcceptableParamIdAndCategoryId(self: TableSectionData,nRow: int,paramId: ElementId,categoryId: ElementId) -> bool

  

   Identifies if the given parameter id and category id can be assigned to a cell 

    in the given row in this table.

  

  

   nRow: row index

   Returns: True if the ParamId and CategoryId are all valid.
  """
  pass
 def IsCellFormattable(self,nRow,nCol):
  """
  IsCellFormattable(self: TableSectionData,nRow: int,nCol: int) -> bool

  

   Determines whether the cell is formattable or not

  

   nRow: The row index of the cell

   nCol: The column index of the cell
  """
  pass
 def IsCellOverridden(self,*__args):
  """
  IsCellOverridden(self: TableSectionData,nRow: int,nCol: int) -> bool

  

   Indicates if the cell is overridden or not.

  IsCellOverridden(self: TableSectionData,nCol: int) -> bool

  

   Indicates if the column is overridden or not.
  """
  pass
 def IsDataOutOfDate(self):
  """
  IsDataOutOfDate(self: TableSectionData) -> bool

  

   Indicates whether the data in this section is out of date.

   Returns: True if the data in this section is out of date,false otherwise.
  """
  pass
 def IsValidColumnNumber(self,nCol):
  """
  IsValidColumnNumber(self: TableSectionData,nCol: int) -> bool

  

   Verifies if the column number is valid.

  

   nCol: The column number.

   Returns: True if the column number is between FirstColumnNumber and LastColumnNumber,

    false otherwise.
  """
  pass
 def IsValidImageSymbolId(self,imageSymbolId):
  """
  IsValidImageSymbolId(self: TableSectionData,imageSymbolId: ElementId) -> bool

  

   Identifies if the element id represents a valid ImageSymbol element.

  

   imageSymbolId: The element id of the image symbol.
  """
  pass
 def IsValidRowNumber(self,nRow):
  """
  IsValidRowNumber(self: TableSectionData,nRow: int) -> bool

  

   Verifies if the row number is valid.

  

   nRow: The row number.

   Returns: True if the row number is between FirstRowNumber and LastRowNumber,false 

    otherwise.
  """
  pass
 def MergeCells(self,mergedCell):
  """
  MergeCells(self: TableSectionData,mergedCell: TableMergedCell)

   Merges cells for the given area.
  """
  pass
 def RefreshData(self):
  """
  RefreshData(self: TableSectionData) -> bool

  

   Rebuilds the data in this section if it is out of date.

   Returns: True if the data is up to date after the refresh.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: TableSectionData,disposing: bool) """
  pass
 def RemoveColumn(self,nIndex):
  """
  RemoveColumn(self: TableSectionData,nIndex: int)

   Removes a column data at a specified index.

  

   nIndex: An integer index
  """
  pass
 def RemoveRow(self,nIndex):
  """
  RemoveRow(self: TableSectionData,nIndex: int)

   Removes a row data at a specified index.

  

   nIndex: An integer index.
  """
  pass
 def ResetCellOverride(self,*__args):
  """
  ResetCellOverride(self: TableSectionData,nRow: int,nCol: int)

   Resets the override of the cell.

  ResetCellOverride(self: TableSectionData,nCol: int)

   Resets the override of the column.
  """
  pass
 def SetCellCalculatedValue(self,*__args):
  """
  SetCellCalculatedValue(self: TableSectionData,nRow: int,nCol: int,pCalcValue: TableCellCalculatedValueData)

   Allows the caller to set the calculated value for a specified cell

  SetCellCalculatedValue(self: TableSectionData,nCol: int,pCalcValue: TableCellCalculatedValueData)

   Allows the caller to set the calculated value for a specified column
  """
  pass
 def SetCellCombinedParameters(self,*__args):
  """ SetCellCombinedParameters(self: TableSectionData,nRow: int,nCol: int,paramData: IList[TableCellCombinedParameterData])SetCellCombinedParameters(self: TableSectionData,nCol: int,paramData: IList[TableCellCombinedParameterData]) """
  pass
 def SetCellFormatOptions(self,nRow,nCol,options):
  """
  SetCellFormatOptions(self: TableSectionData,nRow: int,nCol: int,options: FormatOptions)

   Sets a cell's FormatOptions.

  

   nRow: The row index of the cell

   nCol: The column index of the cell

   options: The format option to assign
  """
  pass
 def SetCellParamIdAndCategoryId(self,*__args):
  """
  SetCellParamIdAndCategoryId(self: TableSectionData,nRow: int,nCol: int,paramId: ElementId,categoryId: ElementId)

   Sets a cell's category and parameter Id

  SetCellParamIdAndCategoryId(self: TableSectionData,nCol: int,paramId: ElementId,categoryId: ElementId)

   Sets a column's category and parameter Id
  """
  pass
 def SetCellStyle(self,*__args):
  """
  SetCellStyle(self: TableSectionData,nRow: int,nCol: int,Style: TableCellStyle)

   Sets a cell's style

  SetCellStyle(self: TableSectionData,nCol: int,Style: TableCellStyle)

   Sets a column's style.

  SetCellStyle(self: TableSectionData,Style: TableCellStyle)

   Sets a section's style
  """
  pass
 def SetCellText(self,nRow,nCol,text):
  """
  SetCellText(self: TableSectionData,nRow: int,nCol: int,text: str)

   Sets a cell's to display the specified text.

  

   nRow: The cell row.

   nCol: The cell column.

   text: The text to show in the cell.
  """
  pass
 def SetCellType(self,*__args):
  """
  SetCellType(self: TableSectionData,nRow: int,nCol: int,type: CellType)

   Sets a cell's Type

  SetCellType(self: TableSectionData,nCol: int,type: CellType)

   Sets a column's cell type
  """
  pass
 def SetColumnWidth(self,nCol,width):
  """
  SetColumnWidth(self: TableSectionData,nCol: int,width: float)

   Sets a column's width in feet
  """
  pass
 def SetColumnWidthInPixels(self,nCol,width):
  """
  SetColumnWidthInPixels(self: TableSectionData,nCol: int,width: int)

   This sets a column's width in pixels
  """
  pass
 def SetMergedCell(self,nRow,nCol,mergedCell):
  """
  SetMergedCell(self: TableSectionData,nRow: int,nCol: int,mergedCell: TableMergedCell)

   Sets the merged cell that this cell is a part of.

  

   nRow: The cell row.

   nCol: The cell column.
  """
  pass
 def SetRowHeight(self,nRow,height):
  """
  SetRowHeight(self: TableSectionData,nRow: int,height: float)

   Sets a row's height in feet
  """
  pass
 def SetRowHeightInPixels(self,nRow,height):
  """
  SetRowHeightInPixels(self: TableSectionData,nRow: int,height: int)

   This sets a row's height in pixels
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 FirstColumnNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The first column in this section of the table.



Get: FirstColumnNumber(self: TableSectionData) -> int



"""

 FirstRowNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The first row in this section of the table.



Get: FirstRowNumber(self: TableSectionData) -> int



"""

 HideSection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Whether or not the section is hidden.



Get: HideSection(self: TableSectionData) -> bool



Set: HideSection(self: TableSectionData)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: TableSectionData) -> bool



"""

 LastColumnNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The last column in this section of the table.



Get: LastColumnNumber(self: TableSectionData) -> int



"""

 LastRowNumber=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The last row in this section of the table.



Get: LastRowNumber(self: TableSectionData) -> int



"""

 NeedsRefresh=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if the table data need to refresh.



Get: NeedsRefresh(self: TableSectionData) -> bool



Set: NeedsRefresh(self: TableSectionData)=value

"""

 NumberOfColumns=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of items in column data array.



Get: NumberOfColumns(self: TableSectionData) -> int



Set: NumberOfColumns(self: TableSectionData)=value

"""

 NumberOfRows=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of items in row data array.



Get: NumberOfRows(self: TableSectionData) -> int



Set: NumberOfRows(self: TableSectionData)=value

"""


