class DataGridViewBand(DataGridViewElement,ICloneable,IDisposable):
 """ Represents a linear collection of elements in a System.Windows.Forms.DataGridView control. """
 def Clone(self):
  """
  Clone(self: DataGridViewBand) -> object

  

   Creates an exact copy of this band.

   Returns: An System.Object that represents the cloned System.Windows.Forms.DataGridViewBand.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: DataGridViewBand)

   Releases all resources used by the System.Windows.Forms.DataGridViewBand.
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
  ToString(self: DataGridViewBand) -> str

  

   Returns a string that represents the current band.

   Returns: A System.String that represents the current System.Windows.Forms.DataGridViewBand.
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
 ContextMenuStrip=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the shortcut menu for the band.



Get: ContextMenuStrip(self: DataGridViewBand) -> ContextMenuStrip



Set: ContextMenuStrip(self: DataGridViewBand)=value

"""

 DefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the default cell style of the band.



Get: DefaultCellStyle(self: DataGridViewBand) -> DataGridViewCellStyle



Set: DefaultCellStyle(self: DataGridViewBand)=value

"""

 DefaultHeaderCellType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the run-time type of the default header cell.



Get: DefaultHeaderCellType(self: DataGridViewBand) -> Type



Set: DefaultHeaderCellType(self: DataGridViewBand)=value

"""

 Displayed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band is currently displayed onscreen.



Get: Displayed(self: DataGridViewBand) -> bool



"""

 Frozen=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the band will move when a user scrolls through the System.Windows.Forms.DataGridView.



Get: Frozen(self: DataGridViewBand) -> bool



Set: Frozen(self: DataGridViewBand)=value

"""

 HasDefaultCellStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the System.Windows.Forms.DataGridViewBand.DefaultCellStyle property has been set.



Get: HasDefaultCellStyle(self: DataGridViewBand) -> bool



"""

 HeaderCellCore=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the header cell of the System.Windows.Forms.DataGridViewBand.



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the relative position of the band within the System.Windows.Forms.DataGridView control.



Get: Index(self: DataGridViewBand) -> int



"""

 InheritedStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the cell style in effect for the current band,taking into account style inheritance.



Get: InheritedStyle(self: DataGridViewBand) -> DataGridViewCellStyle



"""

 IsRow=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the band represents a row.



"""

 ReadOnly=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the user can edit the band's cells.



Get: ReadOnly(self: DataGridViewBand) -> bool



Set: ReadOnly(self: DataGridViewBand)=value

"""

 Resizable=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the band can be resized in the user interface (UI).



Get: Resizable(self: DataGridViewBand) -> DataGridViewTriState



Set: Resizable(self: DataGridViewBand)=value

"""

 Selected=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the band is in a selected user interface (UI) state.



Get: Selected(self: DataGridViewBand) -> bool



Set: Selected(self: DataGridViewBand)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that contains data to associate with the band.



Get: Tag(self: DataGridViewBand) -> object



Set: Tag(self: DataGridViewBand)=value

"""

 Visible=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the band is visible to the user.



Get: Visible(self: DataGridViewBand) -> bool



Set: Visible(self: DataGridViewBand)=value

"""


