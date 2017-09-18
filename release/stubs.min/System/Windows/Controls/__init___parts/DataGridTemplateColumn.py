class DataGridTemplateColumn(DataGridColumn):
 """
 Represents a System.Windows.Controls.DataGrid column that hosts template-specified content in its cells.

 

 DataGridTemplateColumn()
 """
 CellEditingTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template to use to display the contents of a cell that is in editing mode.



Get: CellEditingTemplate(self: DataGridTemplateColumn) -> DataTemplate



Set: CellEditingTemplate(self: DataGridTemplateColumn)=value

"""

 CellEditingTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that determines which template to use to display the contents of a cell that is in editing mode.



Get: CellEditingTemplateSelector(self: DataGridTemplateColumn) -> DataTemplateSelector



Set: CellEditingTemplateSelector(self: DataGridTemplateColumn)=value

"""

 CellTemplate=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the template to use to display the contents of a cell that is not in editing mode.



Get: CellTemplate(self: DataGridTemplateColumn) -> DataTemplate



Set: CellTemplate(self: DataGridTemplateColumn)=value

"""

 CellTemplateSelector=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the object that determines which template to use to display the contents of a cell that is not in editing mode.



Get: CellTemplateSelector(self: DataGridTemplateColumn) -> DataTemplateSelector



Set: CellTemplateSelector(self: DataGridTemplateColumn)=value

"""

 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""


 CellEditingTemplateProperty=None
 CellEditingTemplateSelectorProperty=None
 CellTemplateProperty=None
 CellTemplateSelectorProperty=None

