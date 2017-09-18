class DataGridViewTextBoxColumn(DataGridViewColumn,ICloneable,IDisposable,IComponent):
 """
 Hosts a collection of System.Windows.Forms.DataGridViewTextBoxCell cells.

 

 DataGridViewTextBoxColumn()
 """
 def Dispose(self):
  """
  Dispose(self: DataGridViewColumn,disposing: bool)

   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def OnDataGridViewChanged(self,*args):
  """
  OnDataGridViewChanged(self: DataGridViewBand)

   Called when the band is associated with a different System.Windows.Forms.DataGridView.
  """
  pass
 def RaiseCellClick(self,*args):
  """
  RaiseCellClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellContentClick(self,*args):
  """
  RaiseCellContentClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellContentDoubleClick(self,*args):
  """
  RaiseCellContentDoubleClick(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellContentDoubleClick event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseCellValueChanged(self,*args):
  """
  RaiseCellValueChanged(self: DataGridViewElement,e: DataGridViewCellEventArgs)

   Raises the System.Windows.Forms.DataGridView.CellValueChanged event.

  

   e: A System.Windows.Forms.DataGridViewCellEventArgs that contains the event data.
  """
  pass
 def RaiseDataError(self,*args):
  """
  RaiseDataError(self: DataGridViewElement,e: DataGridViewDataErrorEventArgs)

   Raises the System.Windows.Forms.DataGridView.DataError event.

  

   e: A System.Windows.Forms.DataGridViewDataErrorEventArgs that contains the event data.
  """
  pass
 def RaiseMouseWheel(self,*args):
  """
  RaiseMouseWheel(self: DataGridViewElement,e: MouseEventArgs)

   Raises the System.Windows.Forms.Control.MouseWheel event.

  

   e: A System.Windows.Forms.MouseEventArgs that contains the event data.
  """
  pass
 def ToString(self):
  """
  ToString(self: DataGridViewTextBoxColumn) -> str

   Returns: A System.String that describes the column.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to model cell appearance.



Get: CellTemplate(self: DataGridViewTextBoxColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewTextBoxColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 MaxInputLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of characters that can be entered into the text box.



Get: MaxInputLength(self: DataGridViewTextBoxColumn) -> int



Set: MaxInputLength(self: DataGridViewTextBoxColumn)=value

"""

 SortMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the sort mode for the column.



Get: SortMode(self: DataGridViewTextBoxColumn) -> DataGridViewColumnSortMode



Set: SortMode(self: DataGridViewTextBoxColumn)=value

"""


