class ErrorEventArgs(EventArgs):
 """
 Provides data for the System.IO.FileSystemWatcher.Error event.

 

 ErrorEventArgs(exception: Exception)
 """
 def GetException(self):
  """
  GetException(self: ErrorEventArgs) -> Exception

  

   Gets the System.Exception that represents the error that occurred.

   Returns: An System.Exception that represents the error that occurred.
  """
  pass
 @staticmethod
 def __new__(self,exception):
  """ __new__(cls: type,exception: Exception) """
  pass
