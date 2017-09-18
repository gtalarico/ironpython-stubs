class VertexPair(object,IDisposable):
 """
 Indices of a pair of vertices in two CurveLoops(one vertex in each loop).

 

 VertexPair(firstVertexIdx: int,secondVertexIdx: int)
 """
 def Dispose(self):
  """ Dispose(self: VertexPair) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: VertexPair,disposing: bool) """
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
 def __new__(self,firstVertexIdx,secondVertexIdx):
  """ __new__(cls: type,firstVertexIdx: int,secondVertexIdx: int) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 First=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the first index of VertexPair.



Get: First(self: VertexPair) -> int



Set: First(self: VertexPair)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: VertexPair) -> bool



"""

 Second=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies the second index of VertexPair.



Get: Second(self: VertexPair) -> int



Set: Second(self: VertexPair)=value

"""


