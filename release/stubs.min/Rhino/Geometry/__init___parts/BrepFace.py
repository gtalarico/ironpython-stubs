class BrepFace(SurfaceProxy,IDisposable,ISerializable):
 """
 Provides strongly-typed access to brep faces.

    A Brep face is composed of one surface and trimming curves.
 """
 def AdjacentEdges(self):
  """
  AdjacentEdges(self: BrepFace) -> Array[int]

  

   Gets the indices of all the BrepEdges that delineate this Face.
  """
  pass
 def AdjacentFaces(self):
  """
  AdjacentFaces(self: BrepFace) -> Array[int]

  

   Gets the indices of all the BrepFaces that surround (are adjacent to) this face.
  """
  pass
 def ChangeSurface(self,surfaceIndex):
  """
  ChangeSurface(self: BrepFace,surfaceIndex: int) -> bool

  

   Expert user tool that replaces the 3d surface geometry use by the face.

  

   surfaceIndex: brep surface index of new surface.

   Returns: true if successful.
  """
  pass
 def ConstructConstObject(self,*args):
  """
  ConstructConstObject(self: CommonObject,parentObject: object,subobject_index: int)

   Assigns a parent object and a subobject index to this.

  

   parentObject: The parent object.

   subobject_index: The subobject index.
  """
  pass
 def CreateExtrusion(self,pathCurve,cap):
  """
  CreateExtrusion(self: BrepFace,pathCurve: Curve,cap: bool) -> Brep

  

   Extrude a face in a Brep.

  

   pathCurve: The path to extrude along.

   cap: If true,the extrusion is capped with a translation of the face being extruded

   Returns: A Brep on success or null on failure.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: CommonObject,disposing: bool)

   For derived class implementers.

     This method is called with argument true when class 

    user calls Dispose(),while with argument false when

     the Garbage Collector invokes 

    the finalizer,or Finalize() method.You must reclaim all used unmanaged resources in both cases,

    and can use this chance to call Dispose on disposable fields if the argument is true.Also,you 

    must call the base virtual method within your overriding method.

  

  

   disposing: true if the call comes from the Dispose() method; false if it comes from the Garbage Collector 

    finalizer.
  """
  pass
 def DuplicateFace(self,duplicateMeshes):
  """
  DuplicateFace(self: BrepFace,duplicateMeshes: bool) -> Brep

  

   Duplicate a face from the brep to create new single face brep.

  

   duplicateMeshes: If true,shading meshes will be copied as well.

   Returns: A new single-face brep synonymous with the current Face.
  """
  pass
 def DuplicateSurface(self):
  """
  DuplicateSurface(self: BrepFace) -> Surface

  

   Gets a copy to the untrimmed surface that this face is based on.

   Returns: A copy of this face's underlying surface.
  """
  pass
 def GetMesh(self,meshType):
  """
  GetMesh(self: BrepFace,meshType: MeshType) -> Mesh

  

   Obtains a reference to a specified type of mesh for this brep face.

  

   meshType: The mesh type.

   Returns: A mesh.
  """
  pass
 def IsPointOnFace(self,u,v):
  """
  IsPointOnFace(self: BrepFace,u: float,v: float) -> PointFaceRelation

  

   Tests if a parameter space point is on the interior of a trimmed face.

  

   u: Parameter space point u value.

   v: Parameter space point v value.

   Returns: A value describing the spatial relationship between the point and the face.
  """
  pass
 def NonConstOperation(self,*args):
  """
  NonConstOperation(self: CommonObject)

   For derived classes implementers.

     Defines the necessary implementation to free the 

    instance from being const.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: GeometryBase)

   Is called when a non-const operation occurs.
  """
  pass
 def PullPointsToFace(self,points,tolerance):
  """ PullPointsToFace(self: BrepFace,points: IEnumerable[Point3d],tolerance: float) -> Array[Point3d] """
  pass
 def RebuildEdges(self,tolerance,rebuildSharedEdges,rebuildVertices):
  """
  RebuildEdges(self: BrepFace,tolerance: float,rebuildSharedEdges: bool,rebuildVertices: bool) -> bool

  

   Rebuild the edges used by a face so they lie on the surface.

  

   tolerance: tolerance for fitting 3d edge curves.

   rebuildSharedEdges: if false and and edge is used by this face and a neighbor,then the edge

     will be 

    skipped.

  

   rebuildVertices: if true,vertex locations are updated to lie on the surface.

   Returns: true on success.
  """
  pass
 def SetDomain(self,direction,domain):
  """
  SetDomain(self: BrepFace,direction: int,domain: Interval) -> bool

  

   Sets the surface domain of this face.

  

   direction: Direction of face to set (0=U,1=V).

   domain: Domain to apply.

   Returns: true on success,false on failure.
  """
  pass
 def SetMesh(self,meshType,mesh):
  """
  SetMesh(self: BrepFace,meshType: MeshType,mesh: Mesh) -> bool

  

   Sets a reference to a specified type of mesh for this brep face.

  

   meshType: The mesh type.

   mesh: The new mesh.

   Returns: true if the operation succeeded; otherwise false.
  """
  pass
 def Split(self,*__args):
  """ Split(self: BrepFace,curves: IEnumerable[Curve],tolerance: float) -> Brep """
  pass
 def TrimAwareIsoCurve(self,direction,constantParameter):
  """
  TrimAwareIsoCurve(self: BrepFace,direction: int,constantParameter: float) -> Array[Curve]

  

   Similar to IsoCurve function,except this function pays attention to trims on faces 

       

     and may return multiple curves.

  

  

   direction: Direction of isocurve.

     0=Isocurve connects all points with a constant U value.1=

    Isocurve connects all points with a constant V value.

  

   constantParameter: Surface parameter that remains identical along the isocurves.

   Returns: Isoparametric curves connecting all points with the constantParameter value.
  """
  pass
 def TrimAwareIsoIntervals(self,direction,constantParameter):
  """
  TrimAwareIsoIntervals(self: BrepFace,direction: int,constantParameter: float) -> Array[Interval]

  

   Gets intervals where the iso curve exists on a BrepFace (trimmed surface)

  

   direction: Direction of isocurve.

     0=Isocurve connects all points with a constant U value.1=

    Isocurve connects all points with a constant V value.

  

   constantParameter: Surface parameter that remains identical along the isocurves.

   Returns: If direction=0,the parameter space iso interval connects the 2d points

     

    (intervals[i][0],iso_constant) and (intervals[i][1],iso_constant).

     If direction=

    1,the parameter space iso interval connects the 2d points

     

    (iso_constant,intervals[i][0]) and (iso_constant,intervals[i][1]).
  """
  pass
 def UnderlyingSurface(self):
  """
  UnderlyingSurface(self: BrepFace) -> Surface

  

   Gets the untrimmed surface that is the base of this face.

   Returns: A surface,or null on error.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 FaceIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index of face in Brep.Faces array.



Get: FaceIndex(self: BrepFace) -> int



"""

 IsSurface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the face is synonymous with the underlying surface. 

   If a Face has no trimming curves then it is considered a Surface.



Get: IsSurface(self: BrepFace) -> bool



"""

 Loops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Loops in this face.



Get: Loops(self: BrepFace) -> BrepLoopList



"""

 OrientationIsReversed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """true if face orientation is opposite of natural surface orientation.



Get: OrientationIsReversed(self: BrepFace) -> bool



Set: OrientationIsReversed(self: BrepFace)=value

"""

 OuterLoop=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Every face has a single outer loop.



Get: OuterLoop(self: BrepFace) -> BrepLoop



"""

 SurfaceIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Surface index of the 3d surface geometry used by this face or -1



Get: SurfaceIndex(self: BrepFace) -> int



"""


