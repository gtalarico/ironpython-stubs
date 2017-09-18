class DataGridViewDataErrorEventArgs(DataGridViewCellCancelEventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.DataError event.

 

 DataGridViewDataErrorEventArgs(exception: Exception,columnIndex: int,rowIndex: int,context: DataGridViewDataErrorContexts)
 """
 @staticmethod
 def __new__(self,exception,columnIndex,rowIndex,context):
  """ __new__(cls: type,exception: Exception,columnIndex: int,rowIndex: int,context: DataGridViewDataErrorContexts) """
  pass
 Context=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets details about the state of the System.Windows.Forms.DataGridView when the error occurred.



Get: Context(self: DataGridViewDataErrorEventArgs) -> DataGridViewDataErrorContexts



"""

 Exception=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the exception that represents the error.



Get: Exception(self: DataGridViewDataErrorEventArgs) -> Exception



"""

 ThrowException=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether to throw the exception after the System.Windows.Forms.DataGridViewDataErrorEventHandler delegate is finished with it.



Get: ThrowException(self: DataGridViewDataErrorEventArgs) -> bool



Set: ThrowException(self: DataGridViewDataErrorEventArgs)=value

"""


