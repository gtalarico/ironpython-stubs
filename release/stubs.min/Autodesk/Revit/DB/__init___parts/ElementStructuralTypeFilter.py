class ElementStructuralTypeFilter(ElementQuickFilter,IDisposable):
 """
 A filter used to find elements matching a structural type.
 
 ElementStructuralTypeFilter(structuralType: StructuralType,inverted: bool)
 ElementStructuralTypeFilter(structuralType: StructuralType)
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
 def __new__(self,structuralType,inverted=None):
  """
  __new__(cls: type,structuralType: StructuralType,inverted: bool)
  __new__(cls: type,structuralType: StructuralType)
  """
  pass
 StructuralType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The structural type.

Get: StructuralType(self: ElementStructuralTypeFilter) -> StructuralType

"""


