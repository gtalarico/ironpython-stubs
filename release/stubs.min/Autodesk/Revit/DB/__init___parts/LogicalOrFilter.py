class LogicalOrFilter(ElementLogicalFilter,IDisposable):
 """
 A filter that contains a set of filters. The filter passes when any filter in the set passes.
 
 LogicalOrFilter(filters: IList[ElementFilter])
 LogicalOrFilter(filter1: ElementFilter,filter2: ElementFilter)
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
 def __new__(self,*__args):
  """
  __new__(cls: type,filters: IList[ElementFilter])
  __new__(cls: type,filter1: ElementFilter,filter2: ElementFilter)
  """
  pass
