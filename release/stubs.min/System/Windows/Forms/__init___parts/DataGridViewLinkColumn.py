class DataGridViewLinkColumn(DataGridViewColumn,ICloneable,IDisposable,IComponent):
 """
 Represents a column of cells that contain links in a System.Windows.Forms.DataGridView control.

 

 DataGridViewLinkColumn()
 """
 def Clone(self):
  """
  Clone(self: DataGridViewLinkColumn) -> object

  

   Creates an exact copy of this column.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewLinkColumn.
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
  ToString(self: DataGridViewLinkColumn) -> str

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
 ActiveLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used to display an active link within cells in the column.



Get: ActiveLinkColor(self: DataGridViewLinkColumn) -> Color



Set: ActiveLinkColor(self: DataGridViewLinkColumn)=value

"""

 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to create new cells.



Get: CellTemplate(self: DataGridViewLinkColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewLinkColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 LinkBehavior=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that represents the behavior of links within cells in the column.



Get: LinkBehavior(self: DataGridViewLinkColumn) -> LinkBehavior



Set: LinkBehavior(self: DataGridViewLinkColumn)=value

"""

 LinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used to display an unselected link within cells in the column.



Get: LinkColor(self: DataGridViewLinkColumn) -> Color



Set: LinkColor(self: DataGridViewLinkColumn)=value

"""

 Text=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the link text displayed in a column's cells if System.Windows.Forms.DataGridViewLinkColumn.UseColumnTextForLinkValue is true.



Get: Text(self: DataGridViewLinkColumn) -> str



Set: Text(self: DataGridViewLinkColumn)=value

"""

 TrackVisitedState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the link changes color if it has been visited.



Get: TrackVisitedState(self: DataGridViewLinkColumn) -> bool



Set: TrackVisitedState(self: DataGridViewLinkColumn)=value

"""

 UseColumnTextForLinkValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the System.Windows.Forms.DataGridViewLinkColumn.Text property value is displayed as the link text.



Get: UseColumnTextForLinkValue(self: DataGridViewLinkColumn) -> bool



Set: UseColumnTextForLinkValue(self: DataGridViewLinkColumn)=value

"""

 VisitedLinkColor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the color used to display a link that has been previously visited.



Get: VisitedLinkColor(self: DataGridViewLinkColumn) -> Color



Set: VisitedLinkColor(self: DataGridViewLinkColumn)=value

"""


