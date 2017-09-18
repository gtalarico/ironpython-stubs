class ChangeType(object,IDisposable):
 """ A class representing a change that can be detected and tracked during Dynamic Update. """
 @staticmethod
 def ConcatenateChangeTypes(changeType1,changeType2):
  """
  ConcatenateChangeTypes(changeType1: ChangeType,changeType2: ChangeType) -> ChangeType

  

   Creates a ChangeType that is a union of the two input ChangeTypes

  

   changeType1: First input ChangeType to be concatenated

   changeType2: Second input ChangeType to be concatenated

   Returns: A new ChangeType that is a concatenation/union of the input change types
  """
  pass
 def Contains(self,changeType):
  """
  Contains(self: ChangeType,changeType: ChangeType) -> bool

  

   Checks whether this ChangeType contains the input ChangeType

   Returns: True if input changeType is contained by this ChangeType
  """
  pass
 def Dispose(self):
  """ Dispose(self: ChangeType) """
  pass
 def IsIdentical(self,changeType):
  """
  IsIdentical(self: ChangeType,changeType: ChangeType) -> bool

  

   Compares if two ChangeTypes are identical

  

   changeType: Input ChangeType to be compared

   Returns: True if the this ChangeType and input ChangeType are identical
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ChangeType,disposing: bool) """
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



Get: IsValidObject(self: ChangeType) -> bool



"""


