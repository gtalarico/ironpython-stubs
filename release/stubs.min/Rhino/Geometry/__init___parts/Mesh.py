class Mesh(GeometryBase,IDisposable,ISerializable):
 """
 Represents a geometry type that is defined by vertices and faces.

    This is often called a face-vertex mesh.

 

 Mesh()
 """
 def Append(self,other):
  """
  Append(self: Mesh,other: Mesh)

   Appends a copy of another mesh to this one and updates indices of appended mesh parts.

  

   other: Mesh to append to this one.
  """
  pass
 def ClearTextureData(self):
  """
  ClearTextureData(self: Mesh)

   Remove all texture coordinate information from this mesh.
  """
  pass
 def ClosestMeshPoint(self,testPoint,maximumDistance):
  """
  ClosestMeshPoint(self: Mesh,testPoint: Point3d,maximumDistance: float) -> MeshPoint

  

   Gets the point on the mesh that is closest to a given test point. Similar to the 

     

    ClosestPoint function except this returns a MeshPoint class which includes

     extra 

    information beyond just the location of the closest point.

  

  

   testPoint: The source of the search.

   maximumDistance: Optional upper bound on the distance from test point to the mesh. 

     If you are only 

    interested in finding a point Q on the mesh when 

     testPoint.DistanceTo(Q) < 

    maximumDistance,

     then set maximumDistance to that value. 

     This 

    parameter is ignored if you pass 0.0 for a maximumDistance.

  

   Returns: closest point information on success. null on failure.
  """
  pass
 def ClosestPoint(self,testPoint,pointOnMesh=None,*__args):
  """
  ClosestPoint(self: Mesh,testPoint: Point3d,maximumDistance: float) -> (int,Point3d,Vector3d)

  

   Gets the point on the mesh that is closest to a given test point.

  

   testPoint: Point to seach for.

   maximumDistance: Optional upper bound on the distance from test point to the mesh. 

     If you are only 

    interested in finding a point Q on the mesh when 

     testPoint.DistanceTo(Q) < 

    maximumDistance,

     then set maximumDistance to that value. 

     This 

    parameter is ignored if you pass 0.0 for a maximumDistance.

  

   Returns: Index of face that the closest point lies on if successful. 

     -1 if not successful; 

    the value of pointOnMesh is undefined.

  

  ClosestPoint(self: Mesh,testPoint: Point3d,maximumDistance: float) -> (int,Point3d)

  

   Gets the point on the mesh that is closest to a given test point.

  

   testPoint: Point to seach for.

   maximumDistance: Optional upper bound on the distance from test point to the mesh. 

     If you are only 

    interested in finding a point Q on the mesh when 

     testPoint.DistanceTo(Q) < 

    maximumDistance,

     then set maximumDistance to that value. 

     This 

    parameter is ignored if you pass 0.0 for a maximumDistance.

  

   Returns: Index of face that the closest point lies on if successful. 

     -1 if not successful; 

    the value of pointOnMesh is undefined.

  

  ClosestPoint(self: Mesh,testPoint: Point3d) -> Point3d

  

   Gets the point on the mesh that is closest to a given test point.

  

   testPoint: Point to seach for.

   Returns: The point on the mesh closest to testPoint,or Point3d.Unset on failure.
  """
  pass
 def ColorAt(self,*__args):
  """
  ColorAt(self: Mesh,faceIndex: int,t0: float,t1: float,t2: float,t3: float) -> Color

  

   Evaluate a mesh normal at a set of barycentric coordinates. Barycentric coordinates must 

     

       be assigned in accordance with the rules as defined by MeshPoint.T.

  

  

   faceIndex: Index of triangle or quad to evaluate.

   t0: First barycentric coordinate.

   t1: Second barycentric coordinate.

   t2: Third barycentric coordinate.

   t3: Fourth barycentric coordinate. If the face is a triangle,this coordinate will be ignored.

   Returns: The interpolated vertex color on the mesh or Color.Transparent if the faceIndex is not valid,

   

      if the barycentric coordinates could not be evaluated,or if there are no colors 

    defined on the mesh.

  

  ColorAt(self: Mesh,meshPoint: MeshPoint) -> Color

  

   Evaluate a mesh color at a set of barycentric coordinates.

  

   meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.

   Returns: The interpolated vertex color on the mesh or Color.Transparent if the faceIndex is not valid,

   

      if the barycentric coordinates could not be evaluated,or if there are no colors 

    defined on the mesh.
  """
  pass
 def Compact(self):
  """
  Compact(self: Mesh) -> bool

  

   Removes any unreferenced objects from arrays,reindexes as needed 

     and shrinks 

    arrays to minimum required size.

  

   Returns: true on success,false on failure.
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
 def CopyFrom(self,other):
  """
  CopyFrom(self: Mesh,other: Mesh)

   Copies mesh values into this mesh from another mesh.

  

   other: The other mesh to copy from.
  """
  pass
 @staticmethod
 def CreateBooleanDifference(firstSet,secondSet):
  """ CreateBooleanDifference(firstSet: IEnumerable[Mesh],secondSet: IEnumerable[Mesh]) -> Array[Mesh] """
  pass
 @staticmethod
 def CreateBooleanIntersection(firstSet,secondSet):
  """ CreateBooleanIntersection(firstSet: IEnumerable[Mesh],secondSet: IEnumerable[Mesh]) -> Array[Mesh] """
  pass
 @staticmethod
 def CreateBooleanSplit(meshesToSplit,meshSplitters):
  """ CreateBooleanSplit(meshesToSplit: IEnumerable[Mesh],meshSplitters: IEnumerable[Mesh]) -> Array[Mesh] """
  pass
 @staticmethod
 def CreateBooleanUnion(meshes):
  """ CreateBooleanUnion(meshes: IEnumerable[Mesh]) -> Array[Mesh] """
  pass
 @staticmethod
 def CreateContourCurves(meshToContour,*__args):
  """
  CreateContourCurves(meshToContour: Mesh,sectionPlane: Plane) -> Array[Curve]

  

   Constructs contour curves for a mesh,sectioned at a plane.

  

   meshToContour: A mesh to contour.

   sectionPlane: A cutting plane.

   Returns: An array of curves. This array can be empty.

  CreateContourCurves(meshToContour: Mesh,contourStart: Point3d,contourEnd: Point3d,interval: float) -> Array[Curve]

  

   Constructs contour curves for a mesh,sectioned along a linear axis.

  

   meshToContour: A mesh to contour.

   contourStart: A start point of the contouring axis.

   contourEnd: An end point of the contouring axis.

   interval: An interval distance.

   Returns: An array of curves. This array can be empty.
  """
  pass
 @staticmethod
 def CreateFromBox(*__args):
  """
  CreateFromBox(corners: IEnumerable[Point3d],xCount: int,yCount: int,zCount: int) -> Mesh

  CreateFromBox(box: Box,xCount: int,yCount: int,zCount: int) -> Mesh

  

   Constructs new mesh that matches an aligned box.

  

   box: Box to match.

   xCount: Number of faces in x-direction.

   yCount: Number of faces in y-direction.

   zCount: Number of faces in z-direction.

  CreateFromBox(box: BoundingBox,xCount: int,yCount: int,zCount: int) -> Mesh

  

   Constructs new mesh that matches a bounding box.

  

   box: A box to use for creation.

   xCount: Number of faces in x-direction.

   yCount: Number of faces in y-direction.

   zCount: Number of faces in z-direction.

   Returns: A new brep,or null on failure.
  """
  pass
 @staticmethod
 def CreateFromBrep(brep,meshingParameters=None):
  """
  CreateFromBrep(brep: Brep,meshingParameters: MeshingParameters) -> Array[Mesh]

  

   Constructs a mesh from a brep.

  

   brep: Brep to approximate.

   meshingParameters: Parameters to use during meshing.

   Returns: An array of meshes.

  CreateFromBrep(brep: Brep) -> Array[Mesh]

  

   Constructs a mesh from a brep.

  

   brep: Brep to approximate.

   Returns: An array of meshes.
  """
  pass
 @staticmethod
 def CreateFromClosedPolyline(polyline):
  """
  CreateFromClosedPolyline(polyline: Polyline) -> Mesh

  

   Attempts to create a Mesh that is a triangulation of a closed polyline

  

   polyline: must be closed

   Returns: New mesh on success or null on failure.
  """
  pass
 @staticmethod
 def CreateFromCone(cone,vertical,around):
  """
  CreateFromCone(cone: Cone,vertical: int,around: int) -> Mesh

  

   Constructs a mesh cone

  

   vertical: Number of faces in the top-to-bottom direction

   around: Number of faces around the cone
  """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder,vertical,around):
  """
  CreateFromCylinder(cylinder: Cylinder,vertical: int,around: int) -> Mesh

  

   Constructs a mesh cylinder

  

   vertical: Number of faces in the top-to-bottom direction

   around: Number of faces around the cylinder
  """
  pass
 @staticmethod
 def CreateFromPlanarBoundary(boundary,parameters):
  """
  CreateFromPlanarBoundary(boundary: Curve,parameters: MeshingParameters) -> Mesh

  

   Attempts to construct a mesh from a closed planar curve.

  

   boundary: must be a closed planar curve.

   parameters: parameters used for creating the mesh.

   Returns: New mesh on success or null on failure.
  """
  pass
 @staticmethod
 def CreateFromPlane(plane,xInterval,yInterval,xCount,yCount):
  """
  CreateFromPlane(plane: Plane,xInterval: Interval,yInterval: Interval,xCount: int,yCount: int) -> Mesh

  

   Constructs a planar mesh grid.

  

   plane: Plane of mesh.

   xInterval: Interval describing size and extends of mesh along plane x-direction.

   yInterval: Interval describing size and extends of mesh along plane y-direction.

   xCount: Number of faces in x-direction.

   yCount: Number of faces in y-direction.
  """
  pass
 @staticmethod
 def CreateFromSphere(sphere,xCount,yCount):
  """
  CreateFromSphere(sphere: Sphere,xCount: int,yCount: int) -> Mesh

  

   Constructs a mesh sphere.

  

   sphere: Base sphere for mesh.

   xCount: Number of faces in the around direction.

   yCount: Number of faces in the top-to-bottom direction.
  """
  pass
 def CreatePartitions(self,maximumVertexCount,maximumTriangleCount):
  """
  CreatePartitions(self: Mesh,maximumVertexCount: int,maximumTriangleCount: int) -> bool

  

   In ancient times (or modern smartphone times),some rendering engines

     were only 

    able to process small batches of triangles and the

     CreatePartitions() function was 

    provided to partition the mesh into

     subsets of vertices and faces that those 

    rendering engines could handle.

  

   Returns: true on success
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
 def Duplicate(self):
  """
  Duplicate(self: Mesh) -> GeometryBase

  

   Constructs a copy of this mesh.

     This is the same as 

    Rhino.Geometry.Mesh.DuplicateMesh.

  

   Returns: A mesh.
  """
  pass
 def DuplicateMesh(self):
  """
  DuplicateMesh(self: Mesh) -> Mesh

  

   Constructs a copy of this mesh.

     This is the same as Rhino.Geometry.Mesh.Duplicate.
  """
  pass
 def EvaluateMeshGeometry(self,surface):
  """
  EvaluateMeshGeometry(self: Mesh,surface: Surface) -> bool

  

   If the mesh has SurfaceParameters,the surface is evaluated at

     these parameters and 

    the mesh geometry is updated.

  

  

   surface: An input surface.

   Returns: true if the operation succceeded; false otherwise.
  """
  pass
 def ExplodeAtUnweldedEdges(self):
  """
  ExplodeAtUnweldedEdges(self: Mesh) -> Array[Mesh]

  

   Explode the mesh into submeshes where a submesh is a collection of faces that are contained

   

      within a closed loop of "unwelded" edges. Unwelded edges are edges where the faces that 

    share

     the edge have unique mesh vertexes (not mesh topology vertexes) at both ends 

    of the edge.

  

   Returns: Array of submeshes on success; null on error. If the count in the returned array is 1,then

   

      nothing happened and the ouput is essentially a copy of the input.
  """
  pass
 def Flip(self,vertexNormals,faceNormals,faceOrientation):
  """
  Flip(self: Mesh,vertexNormals: bool,faceNormals: bool,faceOrientation: bool)

   Reverses the direction of the mesh.

  

   vertexNormals: If true,vertex normals will be reversed.

   faceNormals: If true,face normals will be reversed.

   faceOrientation: If true,face orientations will be reversed.
  """
  pass
 def GetCachedTextureCoordinates(self,textureMappingId):
  """
  GetCachedTextureCoordinates(self: Mesh,textureMappingId: Guid) -> CachedTextureCoordinates

  

   Call this method to get cached texture coordinates for a texture

     mapping with the 

    specified Id.

  

  

   textureMappingId: Texture mapping Id

   Returns: Object which allows access to coordinates and other props.
  """
  pass
 def GetNakedEdgePointStatus(self):
  """
  GetNakedEdgePointStatus(self: Mesh) -> Array[bool]

  

   Returns an array of bool values equal in length to the number of vertices in this

     

    mesh. Each value corresponds to a mesh vertex and is set to true if the vertex is

     

    not completely surrounded by faces.

  

   Returns: An array of true/false flags that,at each index,reveals if the corresponding

     

    vertex is completely surrounded by faces.
  """
  pass
 def GetNakedEdges(self):
  """
  GetNakedEdges(self: Mesh) -> Array[Polyline]

  

   Returns all edges of a mesh that are considered "naked" in the

     sense that the edge 

    only has one face.

  

   Returns: An array of polylines,or null on error.
  """
  pass
 def GetOutlines(self,*__args):
  """
  GetOutlines(self: Mesh,viewport: RhinoViewport) -> Array[Polyline]

  

   Constructs the outlines of a mesh. The projection information in the

     viewport is 

    used to determine how the outlines are projected.

  

  

   viewport: A viewport to determine projection direction.

   Returns: An array of polylines,or null on error.

  GetOutlines(self: Mesh,plane: Plane) -> Array[Polyline]

  

   Constructs the outlines of a mesh projected against a plane.

  

   plane: A plane to project against.

   Returns: An array of polylines,or null on error.
  """
  pass
 def GetPartition(self,which):
  """
  GetPartition(self: Mesh,which: int) -> MeshPart

  

   Retrieves a partition. See Rhino.Geometry.Mesh.CreatePartitions(System.Int32,System.Int32) for 

    details.

  

  

   which: The partition index.
  """
  pass
 def IsManifold(self,topologicalTest,isOriented,hasBoundary):
  """
  IsManifold(self: Mesh,topologicalTest: bool) -> (bool,bool,bool)

  

   Gets a value indicating whether or not the mesh is manifold. 

     A manifold mesh does 

    not have any edge that borders more than two faces.

  

  

   topologicalTest: If true,the query treats coincident vertices as the same.

   Returns: true if every mesh "edge" has at most two adjacent faces.
  """
  pass
 def IsPointInside(self,point,tolerance,strictlyIn):
  """
  IsPointInside(self: Mesh,point: Point3d,tolerance: float,strictlyIn: bool) -> bool

  

   Determines if a point is inside a solid mesh.

  

   point: 3d point to test.

   tolerance: (>=0) 3d distance tolerance used for ray-mesh intersection

     and determining strict 

    inclusion.

  

   strictlyIn: If strictlyIn is true,then point must be inside mesh by at least

     tolerance in 

    order for this function to return true.

     If strictlyIn is false,then this function 

    will return true if

     point is inside or the distance from point to a mesh face is <= 

    tolerance.

  

   Returns: true if point is inside the solid mesh,false if not.
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
 def NormalAt(self,*__args):
  """
  NormalAt(self: Mesh,faceIndex: int,t0: float,t1: float,t2: float,t3: float) -> Vector3d

  

   Evaluate a mesh normal at a set of barycentric coordinates. Barycentric coordinates must 

     

       be assigned in accordance with the rules as defined by MeshPoint.T.

  

  

   faceIndex: Index of triangle or quad to evaluate.

   t0: First barycentric coordinate.

   t1: Second barycentric coordinate.

   t2: Third barycentric coordinate.

   t3: Fourth barycentric coordinate. If the face is a triangle,this coordinate will be ignored.

   Returns: A Normal vector to the mesh or Vector3d.Unset if the faceIndex is not valid or if the 

    barycentric coordinates could not be evaluated.

  

  NormalAt(self: Mesh,meshPoint: MeshPoint) -> Vector3d

  

   Evaluate a mesh normal at a set of barycentric coordinates.

  

   meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.

   Returns: A Normal vector to the mesh or Vector3d.Unset if the faceIndex is not valid or if the 

    barycentric coordinates could not be evaluated.
  """
  pass
 def Offset(self,distance,solidify=None):
  """
  Offset(self: Mesh,distance: float,solidify: bool) -> Mesh

  

   Makes a new mesh with vertices offset a distance in the opposite direction of the existing 

    vertex normals.

     Optionally,based on the value of solidify,adds the input mesh and 

    a ribbon of faces along any naked edges.

     If solidify is false it acts exactly as 

    the Offset(distance) function.

  

  

   distance: A distance value.

   solidify: true if the mesh should be solidified.

   Returns: A new mesh on success,or null on failure.

  Offset(self: Mesh,distance: float) -> Mesh

  

   Makes a new mesh with vertices offset a distance in the opposite direction of the existing 

    vertex normals.

     Same as Mesh.Offset(distance,false)

  

  

   distance: A distance value to use for offsetting.

   Returns: A new mesh on success,or null on failure.
  """
  pass
 def OnSwitchToNonConst(self,*args):
  """
  OnSwitchToNonConst(self: Mesh)

   Performs some memory cleanup if necessary
  """
  pass
 def PointAt(self,*__args):
  """
  PointAt(self: Mesh,faceIndex: int,t0: float,t1: float,t2: float,t3: float) -> Point3d

  

   Evaluates a mesh at a set of barycentric coordinates. Barycentric coordinates must 

     

    be assigned in accordance with the rules as defined by MeshPoint.T.

  

  

   faceIndex: Index of triangle or quad to evaluate.

   t0: First barycentric coordinate.

   t1: Second barycentric coordinate.

   t2: Third barycentric coordinate.

   t3: Fourth barycentric coordinate. If the face is a triangle,this coordinate will be ignored.

   Returns: A Point on the mesh or Point3d.Unset if the faceIndex is not valid or if the barycentric 

    coordinates could not be evaluated.

  

  PointAt(self: Mesh,meshPoint: MeshPoint) -> Point3d

  

   Evaluate a mesh at a set of barycentric coordinates.

  

   meshPoint: MeshPoint instance contiaining a valid Face Index and Barycentric coordinates.

   Returns: A Point on the mesh or Point3d.Unset if the faceIndex is not valid or if the barycentric 

    coordinates could not be evaluated.
  """
  pass
 def PullPointsToMesh(self,points):
  """ PullPointsToMesh(self: Mesh,points: IEnumerable[Point3d]) -> Array[Point3d] """
  pass
 def Reduce(self,desiredPolygonCount,allowDistortion,accuracy,normalizeSize):
  """
  Reduce(self: Mesh,desiredPolygonCount: int,allowDistortion: bool,accuracy: int,normalizeSize: bool) -> bool

  

   Reduce polygon count

  

   desiredPolygonCount: desired or target number of faces

   allowDistortion: If true mesh appearance is not changed even if the target polygon count is not reached

   accuracy: Integer from 1 to 10 telling how accurate reduction algorithm

      to use. Greater 

    number gives more accurate results

  

   normalizeSize: If true mesh is fitted to an axis aligned unit cube until reduction is complete

   Returns: True if mesh is successfully reduced and false if mesh could not be reduced for some reason.
  """
  pass
 def SetCachedTextureCoordinates(self,tm,xf):
  """
  SetCachedTextureCoordinates(self: Mesh,tm: TextureMapping,xf: Transform) -> Transform

  

   Set cached texture coordinates using the specified mapping.
  """
  pass
 def SolidOrientation(self):
  """
  SolidOrientation(self: Mesh) -> int

  

   Determines orientation of a "solid" mesh.

   Returns: +1=mesh is solid with outward facing normals.-1=mesh is solid with inward facing normals.0=

    mesh is not solid.
  """
  pass
 def Split(self,*__args):
  """
  Split(self: Mesh,meshes: IEnumerable[Mesh]) -> Array[Mesh]

  Split(self: Mesh,mesh: Mesh) -> Array[Mesh]

  

   Split a mesh with another mesh.

  

   mesh: Mesh to split with.

   Returns: An array of mesh segments representing the split result.

  Split(self: Mesh,plane: Plane) -> Array[Mesh]

  

   Split a mesh by an infinite plane.

  

   plane: The splitting plane.

   Returns: A new mesh array with the split result. This can be null if no result was found.
  """
  pass
 def SplitDisjointPieces(self):
  """
  SplitDisjointPieces(self: Mesh) -> Array[Mesh]

  

   Splits up the mesh into its unconnected pieces.

   Returns: An array containing all the disjoint pieces that make up this Mesh.
  """
  pass
 def UnifyNormals(self):
  """
  UnifyNormals(self: Mesh) -> int

  

   Attempts to fix inconsistencies in the directions of meshfaces for a mesh. This function

      

      does not modify the vertex normals,but rather rearranges the mesh face winding and face

    

        normals to make them all consistent. You may want to call 

    Mesh.Normals.ComputeNormals()

     to recompute vertex normals after calling this 

    functions.

  

   Returns: number of faces that were modified.
  """
  pass
 def Unweld(self,angleToleranceRadians,modifyNormals):
  """
  Unweld(self: Mesh,angleToleranceRadians: float,modifyNormals: bool)

   Makes sure that faces sharing an edge and having a difference of normal greater

     

    than or equal to angleToleranceRadians have unique vertexes along that edge,

     adding 

    vertices if necessary.

  

  

   angleToleranceRadians: Angle at which to make unique vertices.

   modifyNormals: Determines whether new vertex normals will have the same vertex normal as the original (false)

   

      or vertex normals made from the corrsponding face normals (true)
  """
  pass
 def Weld(self,angleToleranceRadians):
  """
  Weld(self: Mesh,angleToleranceRadians: float)

   Makes sure that faces sharing an edge and having a difference of normal greater

     

    than or equal to angleToleranceRadians share vertexes along that edge,vertex normals

      

      are averaged.

  

  

   angleToleranceRadians: Angle at which to weld vertices.
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
 @staticmethod
 def __new__(self):
  """
  __new__(cls: type)

  __new__(cls: type,info: SerializationInfo,context: StreamingContext)
  """
  pass
 def __reduce_ex__(self,*args):
  pass
 DisjointMeshCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of disjoint (topologically unconnected) pieces in this mesh.



Get: DisjointMeshCount(self: Mesh) -> int



"""

 FaceNormals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the face normal collection in this mesh.



Get: FaceNormals(self: Mesh) -> MeshFaceNormalList



"""

 Faces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the faces collection in this mesh.



Get: Faces(self: Mesh) -> MeshFaceList



"""

 HasCachedTextureCoordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Will return true if SetCachedTextureCoordinates has been called;

   otherwise will return false.



Get: HasCachedTextureCoordinates(self: Mesh) -> bool



"""

 IsClosed=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether a mesh is considered to be closed (solid).

   A mesh is considered solid when every mesh edge borders two or more faces.



Get: IsClosed(self: Mesh) -> bool



"""

 Normals=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the vertex normal collection in this mesh.



Get: Normals(self: Mesh) -> MeshVertexNormalList



"""

 PartitionCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of partition information chunks stored on this mesh based

   on the last call to CreatePartitions



Get: PartitionCount(self: Mesh) -> int



"""

 TextureCoordinates=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the vertex texture coordinate collection in this mesh.



Get: TextureCoordinates(self: Mesh) -> MeshTextureCoordinateList



"""

 TopologyEdges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Rhino.Geometry.Collections.MeshTopologyEdgeList object associated with this mesh.

   This object stores edge connectivity.



Get: TopologyEdges(self: Mesh) -> MeshTopologyEdgeList



"""

 TopologyVertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Rhino.Geometry.Collections.MeshTopologyVertexList object associated with this mesh.

   This object stores vertex connectivity and the indices of vertices

   that were unified while computing the edge topology.



Get: TopologyVertices(self: Mesh) -> MeshTopologyVertexList



"""

 VertexColors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the (optional) vertex color collection in this mesh.



Get: VertexColors(self: Mesh) -> MeshVertexColorList



"""

 Vertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets access to the vertices set of this mesh.



Get: Vertices(self: Mesh) -> MeshVertexList



"""


