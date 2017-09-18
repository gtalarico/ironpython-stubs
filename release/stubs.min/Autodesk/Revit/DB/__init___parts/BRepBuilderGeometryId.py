class BRepBuilderGeometryId(object,IDisposable):
 """
 This class is used by the BRepBuilder class to identify objects it creates (faces,edges,etc.).

 

 BRepBuilderGeometryId(other: BRepBuilderGeometryId)
 """
 def Dispose(self):
  """ Dispose(self: BRepBuilderGeometryId) """
  pass
 @staticmethod
 def InvalidGeometryId():
  """
  InvalidGeometryId() -> BRepBuilderGeometryId

  

   Returns an invalid BRepBuilderGeometryId,used as a return value to indicate an 

    error.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: BRepBuilderGeometryId,disposing: bool) """
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
 def __new__(self,other):
  """ __new__(cls: type,other: BRepBuilderGeometryId) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: BRepBuilderGeometryId) -> bool



"""


