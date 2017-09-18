class DataGridViewComboBoxColumn(DataGridViewColumn,ICloneable,IDisposable,IComponent):
 """
 Represents a column of System.Windows.Forms.DataGridViewComboBoxCell objects.

 

 DataGridViewComboBoxColumn()
 """
 def Clone(self):
  """
  Clone(self: DataGridViewComboBoxColumn) -> object

  

   Creates an exact copy of this column.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewComboBoxColumn.
  """
  pass
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
  ToString(self: DataGridViewComboBoxColumn) -> str

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
 AutoComplete=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether cells in the column will match the characters being entered in the cell with one from the possible selections.



Get: AutoComplete(self: DataGridViewComboBoxColumn) -> bool



Set: AutoComplete(self: DataGridViewComboBoxColumn)=value

"""

 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to create cells.



Get: CellTemplate(self: DataGridViewComboBoxColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewComboBoxColumn)=value

"""

 DataSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the data source that populates the selections for the combo boxes.



Get: DataSource(self: DataGridViewComboBoxColumn) -> object



Set: DataSource(self: DataGridViewComboBoxColumn)=value

"""

 DisplayMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that specifies the property or column from which to retrieve strings for display in the combo boxes.



Get: DisplayMember(self: DataGridViewComboBoxColumn) -> str



Set: DisplayMember(self: DataGridViewComboBoxColumn)=value

"""

 DisplayStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines how the combo box is displayed when not editing.



Get: DisplayStyle(self: DataGridViewComboBoxColumn) -> DataGridViewComboBoxDisplayStyle



Set: DisplayStyle(self: DataGridViewComboBoxColumn)=value

"""

 DisplayStyleForCurrentCellOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.DataGridViewComboBoxColumn.DisplayStyle property value applies only to the current cell in the System.Windows.Forms.DataGridView control when the current cell is in this column.



Get: DisplayStyleForCurrentCellOnly(self: DataGridViewComboBoxColumn) -> bool



Set: DisplayStyleForCurrentCellOnly(self: DataGridViewComboBoxColumn)=value

"""

 DropDownWidth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width of the drop-down lists of the combo boxes.



Get: DropDownWidth(self: DataGridViewComboBoxColumn) -> int



Set: DropDownWidth(self: DataGridViewComboBoxColumn)=value

"""

 FlatStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the flat style appearance of the column's cells.



Get: FlatStyle(self: DataGridViewComboBoxColumn) -> FlatStyle



Set: FlatStyle(self: DataGridViewComboBoxColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 Items=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the collection of objects used as selections in the combo boxes.



Get: Items(self: DataGridViewComboBoxColumn) -> ObjectCollection



"""

 MaxDropDownItems=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the maximum number of items in the drop-down list of the cells in the column.



Get: MaxDropDownItems(self: DataGridViewComboBoxColumn) -> int



Set: MaxDropDownItems(self: DataGridViewComboBoxColumn)=value

"""

 Sorted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the items in the combo box are sorted.



Get: Sorted(self: DataGridViewComboBoxColumn) -> bool



Set: Sorted(self: DataGridViewComboBoxColumn)=value

"""

 ValueMember=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that specifies the property or column from which to get values that correspond to the selections in the drop-down list.



Get: ValueMember(self: DataGridViewComboBoxColumn) -> str



Set: ValueMember(self: DataGridViewComboBoxColumn)=value

"""


