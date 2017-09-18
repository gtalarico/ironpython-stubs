class DataGridCheckBoxColumn(DataGridBoundColumn):
 """
 Represents a System.Windows.Controls.DataGrid column that hosts System.Windows.Controls.CheckBox controls in its cells.

 

 DataGridCheckBoxColumn()
 """
 DataGridOwner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the System.Windows.Controls.DataGrid control that contains this column.



"""

 IsThreeState=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the hosted System.Windows.Controls.CheckBox controls enable three states or two.



Get: IsThreeState(self: DataGridCheckBoxColumn) -> bool



Set: IsThreeState(self: DataGridCheckBoxColumn)=value

"""


 DefaultEditingElementStyle=None
 DefaultElementStyle=None
 IsThreeStateProperty=None

