class FreeFormElement(GenericForm,IDisposable):
 """ A Free Form Element that contains non-parametric geometry created from an input solid outline. """
 def CanOffsetFace(self,face):
  """
  CanOffsetFace(self: FreeFormElement,face: Face) -> bool

  

   Determines if the input face of the FreeFormElement can be offset.

  

   face: The face to be checked.

   Returns: True if the face can be offset,false otherwise.
  """
  pass
 @staticmethod
 def Create(document,geometry):
  """
  Create(document: Document,geometry: Solid) -> FreeFormElement

  

   Creates a new FreeFormElement from a copy of the input geometry.

  

   document: The document in which the element is to be created.

   geometry: The input geometry.

   Returns: returns a new FreeFormElement
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
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
 def SetFaceOffset(self,face,offset):
  """
  SetFaceOffset(self: FreeFormElement,face: Face,offset: float)

   Offsets a planar face of the free form element a certain distance in the normal 

    direction.

  

  

   face: The face to offset.

   offset: The magnitude of the offset. A positive value offsets out of the input solid. A 

    negative value offsets into the solid shape.
  """
  pass
 def UpdateSolidGeometry(self,newGeometry):
  """
  UpdateSolidGeometry(self: FreeFormElement,newGeometry: Solid)

   Updates the geometry of the FreeForm element to the given shape preserving 

    References to the existing geometry where possible (see remarks for rules).

  

  

   newGeometry: The new geometry to set in the FreeForm element.
  """
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
