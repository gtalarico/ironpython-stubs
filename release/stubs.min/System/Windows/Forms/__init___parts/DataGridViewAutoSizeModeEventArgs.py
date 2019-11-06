class DataGridViewAutoSizeModeEventArgs(EventArgs):
 """
 Provides data for the System.Windows.Forms.DataGridViewSystem.Windows.Forms.DataGridView.AutoSizeRowsModeChanged and System.Windows.Forms.DataGridView.RowHeadersWidthSizeModeChanged events.
 
 DataGridViewAutoSizeModeEventArgs(previousModeAutoSized: bool)
 """
 def Instance(self):
  """ This function has been arbitrarily put into the stubs"""
  return DataGridViewAutoSizeModeEventArgs()

 @staticmethod
 def __new__(self,previousModeAutoSized):
  """ __new__(cls: type,previousModeAutoSized: bool) """
  pass
 PreviousModeAutoSized=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value specifying whether the System.Windows.Forms.DataGridView was previously set to automatically resize.

Get: PreviousModeAutoSized(self: DataGridViewAutoSizeModeEventArgs) -> bool

"""


