class DataGridAutoGeneratingColumnEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Controls.DataGrid.AutoGeneratingColumn event.

 

 DataGridAutoGeneratingColumnEventArgs(propertyName: str,propertyType: Type,column: DataGridColumn)
 """
 @staticmethod
 def __new__(self,propertyName,propertyType,column):
  """ __new__(cls: type,propertyName: str,propertyType: Type,column: DataGridColumn) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether the event should be canceled.



Get: Cancel(self: DataGridAutoGeneratingColumnEventArgs) -> bool



Set: Cancel(self: DataGridAutoGeneratingColumnEventArgs)=value

"""

 Column=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the generated column.



Get: Column(self: DataGridAutoGeneratingColumnEventArgs) -> DataGridColumn



Set: Column(self: DataGridAutoGeneratingColumnEventArgs)=value

"""

 PropertyDescriptor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the descriptor of the property bound to the generated column.



Get: PropertyDescriptor(self: DataGridAutoGeneratingColumnEventArgs) -> object



"""

 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the property bound to the generated column.



Get: PropertyName(self: DataGridAutoGeneratingColumnEventArgs) -> str



"""

 PropertyType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of the property bound to the generated column.



Get: PropertyType(self: DataGridAutoGeneratingColumnEventArgs) -> Type



"""


