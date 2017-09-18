class DataGridViewAutoSizeColumnsModeEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridView.AutoSizeColumnsModeChanged event.

 

 DataGridViewAutoSizeColumnsModeEventArgs(previousModes: Array[DataGridViewAutoSizeColumnMode])
 """
 @staticmethod
 def __new__(self,previousModes):
  """ __new__(cls: type,previousModes: Array[DataGridViewAutoSizeColumnMode]) """
  pass
 PreviousModes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an array of the previous values of the column System.Windows.Forms.DataGridViewColumn.AutoSizeMode properties.



Get: PreviousModes(self: DataGridViewAutoSizeColumnsModeEventArgs) -> Array[DataGridViewAutoSizeColumnMode]



"""


