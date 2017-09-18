class IDataGridViewEditingCell:
 """ Defines common functionality for a cell that allows the manipulation of its value. """
 def GetEditingCellFormattedValue(self,context):
  """
  GetEditingCellFormattedValue(self: IDataGridViewEditingCell,context: DataGridViewDataErrorContexts) -> object

  

   Retrieves the formatted value of the cell.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    specifies the context in which the data is needed.

  

   Returns: An System.Object that represents the formatted version of the cell contents.
  """
  pass
 def PrepareEditingCellForEdit(self,selectAll):
  """
  PrepareEditingCellForEdit(self: IDataGridViewEditingCell,selectAll: bool)

   Prepares the currently selected cell for editing

  

   selectAll: true to select the cell contents; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 EditingCellFormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the formatted value of the cell.



Get: EditingCellFormattedValue(self: IDataGridViewEditingCell) -> object



Set: EditingCellFormattedValue(self: IDataGridViewEditingCell)=value

"""

 EditingCellValueChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the value of the cell has changed.



Get: EditingCellValueChanged(self: IDataGridViewEditingCell) -> bool



Set: EditingCellValueChanged(self: IDataGridViewEditingCell)=value

"""


