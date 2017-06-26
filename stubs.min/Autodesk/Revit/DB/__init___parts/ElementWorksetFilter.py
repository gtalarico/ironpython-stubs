class ElementWorksetFilter(ElementQuickFilter,IDisposable):
 """
 A filter used to match elements which reside in a given workset.
 
 ElementWorksetFilter(worksetId: WorksetId,inverted: bool)
 ElementWorksetFilter(worksetId: WorksetId)
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
 def __new__(self,worksetId,inverted=None):
  """
  __new__(cls: type,worksetId: WorksetId,inverted: bool)
  __new__(cls: type,worksetId: WorksetId)
  """
  pass
 WorksetId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The workset id.

Get: WorksetId(self: ElementWorksetFilter) -> WorksetId

"""


