class IDataGridEditingService:
 """ Represents methods that process editing requests. """
 def BeginEdit(self,gridColumn,rowNumber):
  """
  BeginEdit(self: IDataGridEditingService,gridColumn: DataGridColumnStyle,rowNumber: int) -> bool

  

   Begins an edit operation.

  

   gridColumn: The System.Windows.Forms.DataGridColumnStyle to edit.

   rowNumber: The index of the row to edit

   Returns: true if the operation can be performed; otherwise false.
  """
  pass
 def EndEdit(self,gridColumn,rowNumber,shouldAbort):
  """
  EndEdit(self: IDataGridEditingService,gridColumn: DataGridColumnStyle,rowNumber: int,shouldAbort: bool) -> bool

  

   Ends the edit operation.

  

   gridColumn: The System.Windows.Forms.DataGridColumnStyle to edit.

   rowNumber: The number of the row to edit

   shouldAbort: True if an abort operation is requested

   Returns: true if value is commited; otherwise false.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
