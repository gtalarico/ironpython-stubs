class TableViewUIUtils(object):
 """ This utility class contains members that involve the Revit UI and operate on schedule views or MEP electrical panel schedules. """
 @staticmethod
 def TestCellAndPromptToEditTypeParameter(tableView,sectionType,row,column):
  """
  TestCellAndPromptToEditTypeParameter(tableView: TableView,sectionType: SectionType,row: int,column: int) -> bool

  

   Prompts the end-user to control whether a type parameter contained in the 

    specified table cell should be allowed edited.

  

  

   tableView: The table view.

   sectionType: The section the row lies in.

   row: The row index in the section.

   column: The column index in the section.

   Returns: Returns true if editing the cell is allowed; otherwise false.
  """
  pass
 __all__=[
  'TestCellAndPromptToEditTypeParameter',
 ]

