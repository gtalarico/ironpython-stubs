class CurveElementFilter(ElementSlowFilter,IDisposable):
 """
 A filter used to pass curve elements which are of a specific type.
 
 CurveElementFilter(curveElementType: CurveElementType,inverted: bool)
 CurveElementFilter(curveElementType: CurveElementType)
 """
 def Dispose(self):
  """ Dispose(self: ElementFilter,A_0: bool) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ElementFilter,disposing: bool) """
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
 def __new__(self,curveElementType,inverted=None):
  """
  __new__(cls: type,curveElementType: CurveElementType,inverted: bool)
  __new__(cls: type,curveElementType: CurveElementType)
  """
  pass
 CurveElementType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The curve element type.

Get: CurveElementType(self: CurveElementFilter) -> CurveElementType

"""


