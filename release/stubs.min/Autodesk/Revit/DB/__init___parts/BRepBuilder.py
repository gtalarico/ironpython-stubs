class BRepBuilder(ShapeBuilder,IDisposable):
 """
 A class that allows direct construction of geometry objects (solids,open shells,etc.).

 

 BRepBuilder(geomType: BRepType)
 """
 def AddCoEdge(self,loopId,edgeId,bCoEdgeIsReversed):
  """
  AddCoEdge(self: BRepBuilder,loopId: BRepBuilderGeometryId,edgeId: BRepBuilderGeometryId,bCoEdgeIsReversed: bool) -> BRepBuilderGeometryId

  

   Add a co-edge associated to a previously added edge. A co-edge represents the 

    use of an edge on one

     of the edge's faces. BrepBuilder allows at most two 

    faces per edge,hence at most two co-edges per edge,

     and the co-edges must 

    have opposite bCoEdgeIsReversed flags. The co-edges in a loop must be added in 

    the

     order in which they occur in loop (i.e.,in their topological order).

  

  

   loopId: Id of the loop containing the new co-edge.

   edgeId: Id of the co-edge's edge,previously created by a call to addEdge().

   bCoEdgeIsReversed: True if the co-edge's topological direction in its face is opposite to the 

    edge's parametric direction,false otherwise.

     The topological directions of 

    the co-edges in a loop must be consistent with the direction in which the loop 

    co-edges

     appear in the loop,and the loop orientations so defined must 

    follow the convention that outer loops are oriented

     counter-clockwise and 

    inner loops are oriented clockwise,with respect to the face's orientation.

  

   Returns: Id of the edge,to be used in calls to other BRepBuilder methods such as 

    AddCoEdge().
  """
  pass
 def AddEdge(self,edgeGeom):
  """
  AddEdge(self: BRepBuilder,edgeGeom: BRepBuilderEdgeGeometry) -> BRepBuilderGeometryId

  

   Add a new edge to the geometry being built. The BRepBuilder uses edges only to 

    store edge geometry and to track

     pairs of co-edges that share an edge.

  

  

   edgeGeom: Information specifying the edge's geometry.

   Returns: Id of the edge,to be used in calls to other BRepBuilder methods such as 

    AddCoEdge().
  """
  pass
 def AddFace(self,surfaceGeom,bFaceIsReversed):
  """
  AddFace(self: BRepBuilder,surfaceGeom: BRepBuilderSurfaceGeometry,bFaceIsReversed: bool) -> BRepBuilderGeometryId

  

   Creates an empty face in the geometry being built. Other BRepBuilder methods 

    are used to add loops to the face.

  

  

   surfaceGeom: The face's support surface.

   bFaceIsReversed: True if the face's orientation is opposite to that of the surface,false if the 

    orientations agree.

     The faces of each shell must be consistently oriented. 

    For a solid (BRepType == Solid),the oriented face normals

     must point out 

    of the solid; for a void (BRepType == Void),the face normals must point into 

    the void.

     See the description of the bCoEdgeIsReversed input for 

    AddCoEdge() for a discussion of the loop and co-edge orientation conventions

    

     to use with the BRepBuilder.

  

   Returns: An id that can be used to identify the face while the BRepBuilder is actively 

    building geometry (e.g.,to add a loop to a face).
  """
  pass
 def AddLoop(self,faceId):
  """
  AddLoop(self: BRepBuilder,faceId: BRepBuilderGeometryId) -> BRepBuilderGeometryId

  

   Creates an empty loop in a given face of the geometry being built. Other 

    BRepBuilder methods are used to add co-edges to the loop.

  

  

   faceId: Id of the face to which the loop should be added. faceId was returned by a call 

    to AddFace().

  

   Returns: An id that can be used to identify the loop while the BRepBuilder is actively 

    building geometry (e.g.,to add co-edges to the loop).
  """
  pass
 def CanAddGeometry(self):
  """
  CanAddGeometry(self: BRepBuilder) -> bool

  

   A validator function that checks the state of this BRepBuilder object. Returns 

    true if this BRepBuilder object is accepting b-rep data,false otherwise.

  

   Returns: True if this BRepBuilder object is accepting b-rep data,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: ShapeBuilder,A_0: bool) """
  pass
 def Finish(self):
  """
  Finish(self: BRepBuilder) -> BRepBuilderOutcome

  

   Complete construction of the geometry. The geometry will be validated and,if 

    valid,stored in this Builder. Otherwise it will be deleted.

  

   Returns: BRepBuilderOutcome.Success if successful,BRepBuilderOutcome.Failure otherwise.
  """
  pass
 def FinishFace(self,faceId):
  """
  FinishFace(self: BRepBuilder,faceId: BRepBuilderGeometryId)

   Indicates that the caller has finished defining the given face.

  

   faceId: Id of the face.
  """
  pass
 def FinishLoop(self,loopId):
  """
  FinishLoop(self: BRepBuilder,loopId: BRepBuilderGeometryId)

   Indicates that the caller has finished defining the given loop.

  

   loopId: Id of the loop.
  """
  pass
 def GetResult(self):
  """
  GetResult(self: BRepBuilder) -> Solid

  

   Get the Geometry object built by this BRepBuilder. This will clear the built 

    Geometry stored in the BRepBuilder.

     This function will throw if this 

    BRepBuilder hasn't completed building the b-rep. Use IsResultAvailable() to 

    verify that this BRepBuilder contains a valid result.

  

   Returns: The Geometry object built by this BRepBuilder. This will clear the built 

    Geometry stored in the BRepBuilder.
  """
  pass
 @staticmethod
 def IsPermittedSurfaceType(surface):
  """
  IsPermittedSurfaceType(surface: Surface) -> bool

  

   A validator function that checks whether the surface object is of type 

    supported as face surface by BRepBuilder.

  

  

   surface: Surface object intended to be used as a face surface.

   Returns: True if surface of this type may be used as a face surface,false otherwise.
  """
  pass
 def IsResultAvailable(self):
  """
  IsResultAvailable(self: BRepBuilder) -> bool

  

   A validator function that checks the state of this BRepBuilder object. Returns 

    true if this BRepBuilder object has successfully built a b-rep.

  

   Returns: True if this BRepBuilder object has successfully built a b-rep.
  """
  pass
 def IsValidEdgeId(self,edgeId):
  """
  IsValidEdgeId(self: BRepBuilder,edgeId: BRepBuilderGeometryId) -> bool

  

   A validator function that checks whether the edge id corresponds to an edge 

    previously added to this BRepBuilder object.

  

  

   edgeId: Edge id to be validated.

   Returns: True if edgeId corresponds to an edge previously added to this BRepBuilder,

    false otherwise.
  """
  pass
 def IsValidFaceId(self,faceId):
  """
  IsValidFaceId(self: BRepBuilder,faceId: BRepBuilderGeometryId) -> bool

  

   A validator function that checks whether the face id corresponds to a face 

    previously added to this BRepBuilder object.

  

  

   faceId: Face id to be validated.

   Returns: True if faceId corresponds to a face previously added to this BRepBuilder,

    false otherwise.
  """
  pass
 def IsValidLoopId(self,loopId):
  """
  IsValidLoopId(self: BRepBuilder,loopId: BRepBuilderGeometryId) -> bool

  

   A validator function that checks whether the loop id corresponds to a loop 

    previously added to this BRepBuilder object.

  

  

   loopId: Loop id to be validated.

   Returns: True if loopId corresponds to a loop previously added to this BRepBuilder,

    false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: ShapeBuilder,disposing: bool) """
  pass
 def SetFaceMaterialId(self,faceId,materialId):
  """
  SetFaceMaterialId(self: BRepBuilder,faceId: BRepBuilderGeometryId,materialId: ElementId)

   Sets material id to a face.

  

   faceId: Id of the face to which material id will be added. faceId was returned by a 

    call to AddFace().

  

   materialId: The material id associated with the face,or invalidElementId if none.

     It 

    is not verified that materialId corresponds to a valid Material element.
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
 @staticmethod
 def __new__(self,geomType):
  """ __new__(cls: type,geomType: BRepType) """
  pass
