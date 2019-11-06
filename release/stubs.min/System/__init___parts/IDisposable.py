class IDisposable:
 """ Defines a method to release allocated resources. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IDisposable()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Dispose(self):
  """
  Dispose(self: IDisposable)
   Performs application-defined tasks associated with freeing,releasing,or resetting unmanaged resources.
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
