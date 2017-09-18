class DataGridBoundColumn(DataGridColumn):
 """ Serves as the base class for columns that can bind to a property in the data source of a System.Windows.Controls.DataGrid. """
 def OnBindingChanged(self,*args):
  """
  OnBindingChanged(self: DataGridBoundColumn,oldBinding: BindingBase,newBinding: BindingBase)

   Notifies the System.Windows.Controls.DataGrid when the value of the 

    System.Windows.Controls.DataGridBoundColumn.Binding property changes.

  

  

   oldBinding: The previous binding.

   newBinding: The binding that the column has been changed to.
  """
  pass
 Binding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding that associates the column with a property in the data source.



Get: Binding(self: DataGridBoundColumn) -> BindingBase



Set: Binding(self: DataGridBoundColumn)=value

"""

 ClipboardContentBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding object to use when getting or setting cell content for the clipboard.



Get: ClipboardContentBinding(self: DataGridBoundColumn) -> BindingBase



Set: ClipboardContentBinding(self: DataGridBoundColumn)=value

"""

 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""

 EditingElementStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the element that the column displays for a cell in editing mode.



Get: EditingElementStyle(self: DataGridBoundColumn) -> Style



Set: EditingElementStyle(self: DataGridBoundColumn)=value

"""

 ElementStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the element that the column displays for a cell that is not in editing mode.



Get: ElementStyle(self: DataGridBoundColumn) -> Style



Set: ElementStyle(self: DataGridBoundColumn)=value

"""


 EditingElementStyleProperty=None
 ElementStyleProperty=None

