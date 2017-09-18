class DataGridHyperlinkColumn(DataGridBoundColumn):
 """
 Represents a System.Windows.Controls.DataGrid column that hosts System.Uri elements in its cells.

 

 DataGridHyperlinkColumn()
 """
 def OnContentBindingChanged(self,*args):
  """
  OnContentBindingChanged(self: DataGridHyperlinkColumn,oldBinding: BindingBase,newBinding: BindingBase)

   Notifies the System.Windows.Controls.DataGrid when the 

    System.Windows.Controls.DataGridHyperlinkColumn.ContentBinding property changes.

  

  

   oldBinding: The previous binding.

   newBinding: The binding that the column has been changed to.
  """
  pass
 ContentBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding to the text of the hyperlink.



Get: ContentBinding(self: DataGridHyperlinkColumn) -> BindingBase



Set: ContentBinding(self: DataGridHyperlinkColumn)=value

"""

 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""

 TargetName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the name of a target window or frame for the hyperlink.



Get: TargetName(self: DataGridHyperlinkColumn) -> str



Set: TargetName(self: DataGridHyperlinkColumn)=value

"""


 DefaultEditingElementStyle=None
 DefaultElementStyle=None
 TargetNameProperty=None

