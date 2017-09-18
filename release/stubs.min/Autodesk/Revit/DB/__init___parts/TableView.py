class TableView(View,IDisposable):
 """
 This represents a view that shows a table.

    Most of the layout data for the table is contained in the TableData class.
 """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAvailableParameterCategories(self,sectionType,row):
  """
  GetAvailableParameterCategories(self: TableView,sectionType: SectionType,row: int) -> IList[ElementId]

  

   Get all available parameter categories.

  

   sectionType: The section the row lies in.

   row: The row.

   Returns: The available parameter categories.
  """
  pass
 @staticmethod
 def GetAvailableParameters(cda,categoryId):
  """
  GetAvailableParameters(cda: Document,categoryId: ElementId) -> IList[ElementId]

  

   Gets a list of valid parameters for the specified category that can be used in 

    the table view.

  

  

   cda: The document.

   categoryId: The specified element category id.

   Returns: The IDs of all valid parameters.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 def GetCalculatedValueName(self,sectionType,row,column):
  """
  GetCalculatedValueName(self: TableView,sectionType: SectionType,row: int,column: int) -> str

  

   Gets the calculated value name for a cell from the template view.

  

   sectionType: The section type.

   row: The row.

   column: The column.

   Returns: The name of the calculated value.
  """
  pass
 def GetCalculatedValueText(self,sectionType,row,column):
  """
  GetCalculatedValueText(self: TableView,sectionType: SectionType,row: int,column: int) -> str

  

   Gets the calculated value text for a cell from the instance view.

  

   sectionType: The section type.

   row: The row.

   column: The column.

   Returns: The calculated value text.
  """
  pass
 def GetCellText(self,sectionType,row,column):
  """
  GetCellText(self: TableView,sectionType: SectionType,row: int,column: int) -> str

  

   Gets the cell's text based on its type

  

   sectionType: The requested section type

   row: Row Number in the Section

   column: Column Number in the Section

   Returns: The text for the given cell
  """
  pass
 def IsValidSectionType(self,sectionType):
  """
  IsValidSectionType(self: TableView,sectionType: SectionType) -> bool

  

   Identifies if the section type is valid for this view.

  

   sectionType: The section type.

   Returns: True if the Section Type is valid,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 MaximumColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum column width



Get: MaximumColumnWidth(self: TableView) -> int



"""

 MaximumGridWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the allowed maximum grid width



Get: MaximumGridWidth(self: TableView) -> int



"""

 MaximumRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the maximum row height



Get: MaximumRowHeight(self: TableView) -> int



"""

 MinimumColumnWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minimum column width



Get: MinimumColumnWidth(self: TableView) -> int



"""

 MinimumRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the minimum row height



Get: MinimumRowHeight(self: TableView) -> int



"""

 TargetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """the element id of the element that is being viewed



Get: TargetId(self: TableView) -> ElementId



Set: TargetId(self: TableView)=value

"""


