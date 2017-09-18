class AnnotationSymbol(FamilyInstance,IDisposable):
 """ This object represents a symbol of the Generic Annotation. """
 def addLeader(self):
  """
  addLeader(self: AnnotationSymbol)
   add a leader to this annotation symbol.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def duplicate(self):
  """
  duplicate(self: AnnotationSymbol) -> AnnotationSymbol
  
   Duplicate this annotation symbol.
   Returns: Pointer to the new annotation symbol.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetLeaders(self):
  """
  GetLeaders(self: AnnotationSymbol) -> IList[Leader]
  
   Returns a collection of leaders currently attached to the annotation.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def removeLeader(self):
  """
  removeLeader(self: AnnotationSymbol)
   remove a leader of this annotation symbol.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
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
 AnnotationSymbolType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The AnnotationSymbol style of this AnnotationSymbol.

Get: AnnotationSymbolType(self: AnnotationSymbol) -> AnnotationSymbolType

Set: AnnotationSymbolType(self: AnnotationSymbol)=value
"""


