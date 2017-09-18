class PointOnPlane(PointElementReference):
 """ Define a ReferencePoint relative to a planar reference. """
 def GetPlaneReference(self):
  """
  GetPlaneReference(self: PointOnPlane) -> Reference
  
   The geometric plane reference.
   Returns: A copy of the reference stored in the PointOnPlane object.
  """
  pass
 @staticmethod
 def IsValidPlaneReference(doc,planeReference):
  """
  IsValidPlaneReference(doc: Document,planeReference: Reference) -> bool
  
   Check whether a geometry reference
  corresponds to a referenceable plane.
  """
  pass
 @staticmethod
 def NewPointOnPlane(doc,planeReference,position,xvec):
  """
  NewPointOnPlane(doc: Document,planeReference: Reference,position: XYZ,xvec: XYZ) -> PointOnPlane
  
   Construct a PointOnPlane given a reference and a location in space.
  
   doc: The document containing the plane reference.
   position: A 3-dimensional position.
   xvec: The direction of the point's
  X-coordinate vector in the plane's
  coordinates. 
    Optional; default value is the
  X-coordinate vector of the plane.
  
   Returns: A new PointOnPlane object with 2-dimensional Position,XVec,and Offset
  
    properties set to match the given 3-dimensional arguments.
  """
  pass
 def SetPlaneReference(self,planeReference):
  """
  SetPlaneReference(self: PointOnPlane,planeReference: Reference)
   Change the geometric plane reference.
  
   planeReference: A reference to some plane
  in the document. (Note: the reference must satisfy
  
    IsValidPlaneReference(),
  but this is not checked until this PointOnPlane 
    object
  is assigned to a ReferencePoint.)
  """
  pass
 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Signed offset from the plane.

Get: Offset(self: PointOnPlane) -> float

Set: Offset(self: PointOnPlane)=value
"""

 Position=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The coordinates of the point (or its projection)
on the plane.

Get: Position(self: PointOnPlane) -> UV

Set: Position(self: PointOnPlane)=value
"""

 XVec=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The X-coordinate vector of the point,in the
plane's coordinate system.

Get: XVec(self: PointOnPlane) -> UV

Set: XVec(self: PointOnPlane)=value
"""


