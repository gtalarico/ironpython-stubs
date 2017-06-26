class FieldValues(object,IDisposable):
 """
 Contains values corresponding to domain points.
    Each domain point may have an array of values,each corresponding to a separate "measurement" for which this value was calculated.
 
 FieldValues(otherObject: FieldValues)
 FieldValues(vectorAtPoint: IList[VectorAtPoint])
 FieldValues(valueAtPoint: IList[ValueAtPoint],unitDirection: XYZ)
 FieldValues(valueAtPoint: IList[ValueAtPoint])
 """
 def Dispose(self):
  """ Dispose(self: FieldValues) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FieldValues,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,otherObject: FieldValues)
  __new__(cls: type,vectorAtPoint: IList[VectorAtPoint])
  __new__(cls: type,valueAtPoint: IList[ValueAtPoint],unitDirection: XYZ)
  __new__(cls: type,valueAtPoint: IList[ValueAtPoint])
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FieldValues) -> bool

"""


