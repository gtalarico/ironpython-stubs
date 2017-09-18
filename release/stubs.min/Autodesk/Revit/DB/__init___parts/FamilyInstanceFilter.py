class FamilyInstanceFilter(ElementSlowFilter,IDisposable):
 """
 A filter used to find elements that are family instances of the given family symbol.

 

 FamilyInstanceFilter(document: Document,familySymbolId: ElementId)
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
 def __new__(self,document,familySymbolId):
  """ __new__(cls: type,document: Document,familySymbolId: ElementId) """
  pass
 FamilySymbolId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The family symbol id.



Get: FamilySymbolId(self: FamilyInstanceFilter) -> ElementId



"""


