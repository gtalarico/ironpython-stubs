class DataGridComboBoxColumn(DataGridColumn):
 """
 Represents a System.Windows.Controls.DataGrid column that hosts System.Windows.Controls.ComboBox controls in its cells.

 

 DataGridComboBoxColumn()
 """
 def OnSelectedItemBindingChanged(self,*args):
  """
  OnSelectedItemBindingChanged(self: DataGridComboBoxColumn,oldBinding: BindingBase,newBinding: BindingBase)

   Notifies the System.Windows.Controls.DataGrid when the 

    System.Windows.Controls.DataGridComboBoxColumn.SelectedItemBinding property changes.

  

  

   oldBinding: The previous binding.

   newBinding: The binding that the column has been changed to.
  """
  pass
 def OnSelectedValueBindingChanged(self,*args):
  """
  OnSelectedValueBindingChanged(self: DataGridComboBoxColumn,oldBinding: BindingBase,newBinding: BindingBase)

   Notifies the System.Windows.Controls.DataGrid when the 

    System.Windows.Controls.DataGridComboBoxColumn.SelectedValueBinding property changes.

  

  

   oldBinding: The previous binding.

   newBinding: The binding that the column has been changed to.
  """
  pass
 def OnTextBindingChanged(self,*args):
  """
  OnTextBindingChanged(self: DataGridComboBoxColumn,oldBinding: BindingBase,newBinding: BindingBase)

   Notifies the System.Windows.Controls.DataGrid when the 

    System.Windows.Controls.DataGridComboBoxColumn.TextBinding property changes.

  

  

   oldBinding: The previous binding.

   newBinding: The binding that the column has been changed to.
  """
  pass
 ClipboardContentBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding object to use when getting or setting cell content for the clipboard.



Get: ClipboardContentBinding(self: DataGridComboBoxColumn) -> BindingBase



Set: ClipboardContentBinding(self: DataGridComboBoxColumn)=value

"""

 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""

 DisplayMemberPath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a path to a value on the source object to provide the visual representation of the object.



Get: DisplayMemberPath(self: DataGridComboBoxColumn) -> str



Set: DisplayMemberPath(self: DataGridComboBoxColumn)=value

"""

 EditingElementStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the element that the column displays for a cell in editing mode.



Get: EditingElementStyle(self: DataGridComboBoxColumn) -> Style



Set: EditingElementStyle(self: DataGridComboBoxColumn)=value

"""

 ElementStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the style that is used when rendering the element that the column displays for a cell that is not in editing mode.



Get: ElementStyle(self: DataGridComboBoxColumn) -> Style



Set: ElementStyle(self: DataGridComboBoxColumn)=value

"""

 ItemsSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a collection that is used to generate the content of the combo box control.



Get: ItemsSource(self: DataGridComboBoxColumn) -> IEnumerable



Set: ItemsSource(self: DataGridComboBoxColumn)=value

"""

 SelectedItemBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding for the currently selected item.



Get: SelectedItemBinding(self: DataGridComboBoxColumn) -> BindingBase



Set: SelectedItemBinding(self: DataGridComboBoxColumn)=value

"""

 SelectedValueBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the value of the selected item,obtained by using System.Windows.Controls.DataGridComboBoxColumn.SelectedValuePath.



Get: SelectedValueBinding(self: DataGridComboBoxColumn) -> BindingBase



Set: SelectedValueBinding(self: DataGridComboBoxColumn)=value

"""

 SelectedValuePath=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the path that is used to get the System.Windows.Controls.Primitives.Selector.SelectedValue from the System.Windows.Controls.Primitives.Selector.SelectedItem.



Get: SelectedValuePath(self: DataGridComboBoxColumn) -> str



Set: SelectedValuePath(self: DataGridComboBoxColumn)=value

"""

 TextBinding=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the binding for the text in the text box portion of the System.Windows.Controls.ComboBox control.



Get: TextBinding(self: DataGridComboBoxColumn) -> BindingBase



Set: TextBinding(self: DataGridComboBoxColumn)=value

"""


 DefaultEditingElementStyle=None
 DefaultElementStyle=None
 DisplayMemberPathProperty=None
 EditingElementStyleProperty=None
 ElementStyleProperty=None
 ItemsSourceProperty=None
 SelectedValuePathProperty=None
 TextBlockComboBoxStyleKey=None

