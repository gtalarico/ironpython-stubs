class StringParameterValue(ParameterValue,IDisposable):
 """
 A class that holds a String value of a parameter element.
 
 StringParameterValue(value: str)
 StringParameterValue()
 """
 def Dispose(self):
  """ Dispose(self: ParameterValue,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ParameterValue,disposing: bool) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,value=None):
  """
  __new__(cls: type,value: str)
  __new__(cls: type)
  """
  pass
 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The stored value

Get: Value(self: StringParameterValue) -> str

Set: Value(self: StringParameterValue)=value
"""


