class Floor(CeilingAndFloor,IDisposable):
 """ An object that represents a Floor within the Autodesk Revit project. """
 def Dispose(self):
  """ Dispose(self: CeilingAndFloor,A_0: bool) """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def GetNormalAtVerticalProjectionPoint(self,modelLocation,floorFace):
  """
  GetNormalAtVerticalProjectionPoint(self: Floor,modelLocation: XYZ,floorFace: FloorFace) -> XYZ

  

   Return a surface normal on either the top or bottom face of a floor slab at a 

    point corresponding to the vertical 

  projection of an arbitrary point in 

    project space.

  

  

   modelLocation: A point in project coordinates whose vertical projection will determine the 

    location at which

  the normal will be taken.

  

   floorFace: A flag determining whether the top or bottom face of the floor should be used.

   Returns: Normal vector on the slab at the projection point.
  """
  pass
 def GetSpanDirectionSymbolIds(self):
  """
  GetSpanDirectionSymbolIds(self: Floor) -> ICollection[ElementId]

  

   Retrieves span direction symbol ElementIds.

   Returns: A collection of Element Ids of span direction symbol elements
  """
  pass
 def GetVerticalProjectionPoint(self,modelLocation,floorFace):
  """
  GetVerticalProjectionPoint(self: Floor,modelLocation: XYZ,floorFace: FloorFace) -> XYZ

  

   Return a surface point on either the top or bottom face of a floor slab 

    corresponding to the vertical projection

  of an arbitrary point in project 

    space.

  

  

   modelLocation: A point in project coordinates that will be projected to the slab top or bottom 

    face.

  

   floorFace: A flag determining whether the top or bottom face of the floor should be used.

   Returns: Slab surface point for the vertically projected model point.
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
 FloorType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves/set an object that represents the type of the floor.



Get: FloorType(self: Floor) -> FloorType



Set: FloorType(self: Floor)=value

"""

 SlabShapeEditor=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get the SlabShapeEditor used for slab shape editing.



Get: SlabShapeEditor(self: Floor) -> SlabShapeEditor



"""

 SpanDirectionAngle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the span direction angle of the floor



Get: SpanDirectionAngle(self: Floor) -> float



Set: SpanDirectionAngle(self: Floor)=value

"""


