class HostObject(Element,IDisposable):
 """ A base class that provides support for all objects that can host other objects,such as walls roofs,and floors. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def FindInserts(self,addRectOpenings,includeShadows,includeEmbeddedWalls,includeSharedEmbeddedInserts):
  """
  FindInserts(self: HostObject,addRectOpenings: bool,includeShadows: bool,includeEmbeddedWalls: bool,includeSharedEmbeddedInserts: bool) -> IList[ElementId]

  

   Gets the ids of the instances inserted into this host object.

  

   addRectOpenings: True if rectangular openings should be included in the return.

   includeShadows: True if shadows should be included in the return.

   includeEmbeddedWalls: True if embedded walls should be included in the return.

   includeSharedEmbeddedInserts: True if shared embedded inserts should be included in the return.

   Returns: All the insertable instances' ids.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
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
