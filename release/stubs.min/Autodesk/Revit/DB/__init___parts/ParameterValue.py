class ParameterValue(object,IDisposable):
 """ A class that holds a value of a parameter element. """
 def Copy(self):
  """
  Copy(self: ParameterValue) -> ParameterValue

  

   Makes an identical copy of the given parameter value.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ParameterValue) """
  pass
 def IsEqual(self,other):
  """
  IsEqual(self: ParameterValue,other: ParameterValue) -> bool

  

   Tests equality with another instance of the same class.

  

   other: The instance to compare with
  """
  pass
 def IsSameType(self,other):
  """
  IsSameType(self: ParameterValue,other: ParameterValue) -> bool

  

   Tests another instance is of the same value type.

  

   other: The instance to compare with
  """
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
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: ParameterValue) -> bool



"""


