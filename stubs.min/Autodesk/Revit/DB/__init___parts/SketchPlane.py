class SketchPlane(Element,IDisposable):
 """ Represents a sketch plane or work plane. """
 @staticmethod
 def Create(document,*__args):
  """
  Create(document: Document,plane: Plane) -> SketchPlane
  
   Creates a new sketch plane from a geometric plane.
  
   document: The document.
   plane: The geometry plane where the sketch plane will be created.
   Returns: The newly created sketch plane.
  Create(document: Document,planarFaceReference: Reference) -> SketchPlane
  
   Creates a new sketch plane from a reference to a planar face.
  
   document: The document.
   planarFaceReference: The reference of the planar face where the sketch plane will be created.
   Returns: The newly created sketch plane.
  Create(document: Document,datumId: ElementId) -> SketchPlane
  
   Creates a sketch plane from a grid,reference plane,or level.
  
   document: The document.
   datumId: The id of the grid,reference plane,or level.
   Returns: The newly created sketch plane.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetPlane(self):
  """
  GetPlane(self: SketchPlane) -> Plane
  
   Returns the corresponding Plane.
   Returns: The plane upon which elements created with this sketch plane will lie.
  """
  pass
 def GetPlaneReference(self):
  """
  GetPlaneReference(self: SketchPlane) -> Reference
  
   Returns a reference to this element as a plane.
   Returns: The reference.
  """
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
 IsSuitableForModelElements=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if the sketch plane can be assigned to model elements.

Get: IsSuitableForModelElements(self: SketchPlane) -> bool

"""


