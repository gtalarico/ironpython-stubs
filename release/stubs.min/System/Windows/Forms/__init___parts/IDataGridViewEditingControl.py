class IDataGridViewEditingControl:
 """ Defines common functionality for controls that are hosted within cells of a System.Windows.Forms.DataGridView. """
 def ApplyCellStyleToEditingControl(self,dataGridViewCellStyle):
  """
  ApplyCellStyleToEditingControl(self: IDataGridViewEditingControl,dataGridViewCellStyle: DataGridViewCellStyle)

   Changes the control's user interface (UI) to be consistent with the specified cell style.

  

   dataGridViewCellStyle: The System.Windows.Forms.DataGridViewCellStyle to use as the model for the UI.
  """
  pass
 def EditingControlWantsInputKey(self,keyData,dataGridViewWantsInputKey):
  """
  EditingControlWantsInputKey(self: IDataGridViewEditingControl,keyData: Keys,dataGridViewWantsInputKey: bool) -> bool

  

   Determines whether the specified key is a regular input key that the editing control should 

    process or a special key that the System.Windows.Forms.DataGridView should process.

  

  

   keyData: A System.Windows.Forms.Keys that represents the key that was pressed.

   dataGridViewWantsInputKey: true when the System.Windows.Forms.DataGridView wants to process the System.Windows.Forms.Keys 

    in keyData; otherwise,false.

  

   Returns: true if the specified key is a regular input key that should be handled by the editing control; 

    otherwise,false.
  """
  pass
 def GetEditingControlFormattedValue(self,context):
  """
  GetEditingControlFormattedValue(self: IDataGridViewEditingControl,context: DataGridViewDataErrorContexts) -> object

  

   Retrieves the formatted value of the cell.

  

   context: A bitwise combination of System.Windows.Forms.DataGridViewDataErrorContexts values that 

    specifies the context in which the data is needed.

  

   Returns: An System.Object that represents the formatted version of the cell contents.
  """
  pass
 def PrepareEditingControlForEdit(self,selectAll):
  """
  PrepareEditingControlForEdit(self: IDataGridViewEditingControl,selectAll: bool)

   Prepares the currently selected cell for editing.

  

   selectAll: true to select all of the cell's content; otherwise,false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 EditingControlDataGridView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.DataGridView that contains the cell.



Get: EditingControlDataGridView(self: IDataGridViewEditingControl) -> DataGridView



Set: EditingControlDataGridView(self: IDataGridViewEditingControl)=value

"""

 EditingControlFormattedValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the formatted value of the cell being modified by the editor.



Get: EditingControlFormattedValue(self: IDataGridViewEditingControl) -> object



Set: EditingControlFormattedValue(self: IDataGridViewEditingControl)=value

"""

 EditingControlRowIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the index of the hosting cell's parent row.



Get: EditingControlRowIndex(self: IDataGridViewEditingControl) -> int



Set: EditingControlRowIndex(self: IDataGridViewEditingControl)=value

"""

 EditingControlValueChanged=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the value of the editing control differs from the value of the hosting cell.



Get: EditingControlValueChanged(self: IDataGridViewEditingControl) -> bool



Set: EditingControlValueChanged(self: IDataGridViewEditingControl)=value

"""

 EditingPanelCursor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cursor used when the mouse pointer is over the System.Windows.Forms.DataGridView.EditingPanel but not over the editing control.



Get: EditingPanelCursor(self: IDataGridViewEditingControl) -> Cursor



"""

 RepositionEditingControlOnValueChange=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the cell contents need to be repositioned whenever the value changes.



Get: RepositionEditingControlOnValueChange(self: IDataGridViewEditingControl) -> bool



"""


