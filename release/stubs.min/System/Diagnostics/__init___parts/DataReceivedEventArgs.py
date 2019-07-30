class DataReceivedEventArgs(EventArgs):
 """ Provides data for the System.Diagnostics.Process.OutputDataReceived and System.Diagnostics.Process.ErrorDataReceived events. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DataReceivedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 Data=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the line of characters that was written to a redirected System.Diagnostics.Process output stream.

Get: Data(self: DataReceivedEventArgs) -> str

"""


