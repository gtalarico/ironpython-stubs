class DataGridViewCheckBoxColumn(DataGridViewColumn,ICloneable,IDisposable,IComponent):
 """
 Hosts a collection of System.Windows.Forms.DataGridViewCheckBoxCell objects.

 

 DataGridViewCheckBoxColumn()

 DataGridViewCheckBoxColumn(threeState: bool)
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
  ToString(self: DataGridViewCheckBoxColumn) -> str

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
 @staticmethod
 def __new__(self,threeState=None):
  """
  __new__(cls: type)

  __new__(cls: type,threeState: bool)
  """
  pass
 def __str__(self,*args):
  pass
 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to create new cells.



Get: CellTemplate(self: DataGridViewCheckBoxColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewCheckBoxColumn)=value

"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column's default cell style.



Get: DefaultCellStyle(self: DataGridViewCheckBoxColumn) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridViewCheckBoxColumn)=value

"""

 FalseValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to a cell value of false,which appears as an unchecked box.



Get: FalseValue(self: DataGridViewCheckBoxColumn) -> object



Set: FalseValue(self: DataGridViewCheckBoxColumn)=value

"""

 FlatStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the flat style appearance of the check box cells.



Get: FlatStyle(self: DataGridViewCheckBoxColumn) -> FlatStyle



Set: FlatStyle(self: DataGridViewCheckBoxColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 IndeterminateValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to an indeterminate or null cell value,which appears as a disabled checkbox.



Get: IndeterminateValue(self: DataGridViewCheckBoxColumn) -> object



Set: IndeterminateValue(self: DataGridViewCheckBoxColumn)=value

"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 ThreeState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the hosted check box cells will allow three check states rather than two.



Get: ThreeState(self: DataGridViewCheckBoxColumn) -> bool



Set: ThreeState(self: DataGridViewCheckBoxColumn)=value

"""

 TrueValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the underlying value corresponding to a cell value of true,which appears as a checked box.



Get: TrueValue(self: DataGridViewCheckBoxColumn) -> object



Set: TrueValue(self: DataGridViewCheckBoxColumn)=value

"""


