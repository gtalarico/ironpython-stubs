class DataGridViewImageColumn(DataGridViewColumn,ICloneable,IDisposable,IComponent):
 """
 Hosts a collection of System.Windows.Forms.DataGridViewImageCell objects.

 

 DataGridViewImageColumn()

 DataGridViewImageColumn(valuesAreIcons: bool)
 """
 def Clone(self):
  """
  Clone(self: DataGridViewImageColumn) -> object

  

   Creates an exact copy of this column.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewImageColumn.
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
  ToString(self: DataGridViewImageColumn) -> str

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
 def __new__(self,valuesAreIcons=None):
  """
  __new__(cls: type)

  __new__(cls: type,valuesAreIcons: bool)
  """
  pass
 def __str__(self,*args):
  pass
 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template used to create new cells.



Get: CellTemplate(self: DataGridViewImageColumn) -> DataGridViewCell



Set: CellTemplate(self: DataGridViewImageColumn)=value

"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the column's default cell style.



Get: DefaultCellStyle(self: DataGridViewImageColumn) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridViewImageColumn)=value

"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a string that describes the column's image.



Get: Description(self: DataGridViewImageColumn) -> str



Set: Description(self: DataGridViewImageColumn)=value

"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 Icon=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the icon displayed in the cells of this column when the cell's System.Windows.Forms.DataGridViewCell.Value property is not set and the cell's System.Windows.Forms.DataGridViewImageCell.ValueIsIcon property is set to true.



Get: Icon(self: DataGridViewImageColumn) -> Icon



Set: Icon(self: DataGridViewImageColumn)=value

"""

 Image=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image displayed in the cells of this column when the cell's System.Windows.Forms.DataGridViewCell.Value property is not set and the cell's System.Windows.Forms.DataGridViewImageCell.ValueIsIcon property is set to false.



Get: Image(self: DataGridViewImageColumn) -> Image



Set: Image(self: DataGridViewImageColumn)=value

"""

 ImageLayout=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the image layout in the cells for this column.



Get: ImageLayout(self: DataGridViewImageColumn) -> DataGridViewImageCellLayout



Set: ImageLayout(self: DataGridViewImageColumn)=value

"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 ValuesAreIcons=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether cells in this column display System.Drawing.Icon values.



Get: ValuesAreIcons(self: DataGridViewImageColumn) -> bool



Set: ValuesAreIcons(self: DataGridViewImageColumn)=value

"""


