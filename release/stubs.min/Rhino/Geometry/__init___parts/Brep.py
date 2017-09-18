class Brep(GeometryBase,IDisposable,ISerializable):
 """
 Boundary Representation. A surface or polysurface along with trim curve information.

 

 Brep()
 """
 def AddEdgeCurve(self,curve):
  """
  AddEdgeCurve(self: Brep,curve: Curve) -> int

  

   Add a 3d curve used by the brep edges

   Returns: Index used to reference this geometry in the edge curve list
  """
  pass
 def AddSurface(self,surface):
  """
  AddSurface(self: Brep,surface: Surface) -> int

  

   Adds a 3D surface used by BrepFace.

  

   surface: A copy of the surface is added to this brep.

   Returns: Index that should be used to reference the geometry.

     -1 is returned if the input is 

    not acceptable.
  """
  pass
 def AddTrimCurve(self,curve):
  """
  AddTrimCurve(self: Brep,curve: Curve) -> int

  

   Add a 2d curve used by the brep trims

   Returns: Index used to reference this geometry in the trimming curve list
  """
  pass
 def Append(self,other):
  """
  Append(self: Brep,other: Brep)

   Appends a copy of another brep to this and updates indices of appended

     brep parts.  

    Duplicates are not removed
  """
  pass
 def CapPlanarHoles(self,tolerance):
  """
  CapPlanarHoles(self: Brep,tolerance: float) -> Brep

  

   Returns a new Brep that is equivalent to this Brep with all planar holes capped.

  

   tolerance: Tolerance to use for capping.

   Returns: New brep on success. null on error.
  """
  pass
 def ClosestPoint(self,testPoint,closestPoint=None,ci=None,s=None,t=None,maximumDistance=None,normal=None):
  """
  ClosestPoint(self: Brep,testPoint: Point3d,maximumDistance: float) -> (bool,Point3d,ComponentIndex,float,float,Vector3d)

  

   Finds a point on a brep that is closest to testPoint.

  

   testPoint: base point to project to surface.

   maximumDistance: If maximumDistance > 0,then only points whose distance

     is <= maximumDistance will 

    be returned. Using a positive

     value of maximumDistance can substantially speed up 

    the search.

  

   Returns: true if the operation succeeded; otherwise,false.

  ClosestPoint(self: Brep,testPoint: Point3d) -> Point3d

  

   Finds a point on the brep that is closest to testPoint.

  

   testPoint: Base point to project to brep.

   Returns: The point on the Brep closest to testPoint or Point3d.Unset if the operation failed.
  """
  pass
 def Compact(self):
  """
  Compact(self: Brep)

   Deletes any unreferenced objects from arrays,reindexes as needed,and

     shrinks 

    arrays to minimum required size. Uses CUllUnused* members to

     delete any 

    unreferenced objects from arrays.
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
 @staticmethod
 def CopyTrimCurves(trimSource,surfaceSource,tolerance):
  """
  CopyTrimCurves(trimSource: BrepFace,surfaceSource: Surface,tolerance: float) -> Brep

  

   Copy all trims from a Brep face onto a surface.

  

   trimSource: Brep face which defines the trimming curves.

   surfaceSource: The surface to trim.

   tolerance: Tolerance to use for rebuilding 3D trim curves.

   Returns: A brep with the shape of surfaceSource and the trims of trimSource or null on failure.
  """
  pass
 @staticmethod
 def CreateBooleanDifference(*__args):
  """
  CreateBooleanDifference(firstBrep: Brep,secondBrep: Brep,tolerance: float) -> Array[Brep]

  

   Compute the Solid Difference of two Breps.

  

   firstBrep: First Brep for boolean difference.

   secondBrep: Second Brep for boolean difference.

   tolerance: Tolerance to use for difference operation.

   Returns: An array of Brep results or null on failure.

  CreateBooleanDifference(firstSet: IEnumerable[Brep],secondSet: IEnumerable[Brep],tolerance: float) -> Array[Brep]
  """
  pass
 @staticmethod
 def CreateBooleanIntersection(*__args):
  """
  CreateBooleanIntersection(firstBrep: Brep,secondBrep: Brep,tolerance: float) -> Array[Brep]

  

   Compute the Solid Intersection of two Breps.

  

   firstBrep: First Brep for boolean intersection.

   secondBrep: Second Brep for boolean intersection.

   tolerance: Tolerance to use for intersection operation.

   Returns: An array of Brep results or null on failure.

  CreateBooleanIntersection(firstSet: IEnumerable[Brep],secondSet: IEnumerable[Brep],tolerance: float) -> Array[Brep]
  """
  pass
 @staticmethod
 def CreateBooleanUnion(breps,tolerance):
  """ CreateBooleanUnion(breps: IEnumerable[Brep],tolerance: float) -> Array[Brep] """
  pass
 @staticmethod
 def CreateContourCurves(brepToContour,*__args):
  """
  CreateContourCurves(brepToContour: Brep,sectionPlane: Plane) -> Array[Curve]

  

   Constructs the contour curves for a brep,using a slicing plane.

  

   brepToContour: A brep or polysurface.

   sectionPlane: A plane.

   Returns: An array with intersected curves. This array can be empty.

  CreateContourCurves(brepToContour: Brep,contourStart: Point3d,contourEnd: Point3d,interval: float) -> Array[Curve]

  

   Constructs the contour curves for a brep at a specified interval.

  

   brepToContour: A brep or polysurface.

   contourStart: A point to start.

   contourEnd: A point to use as the end.

   interval: The interaxial offset in world units.

   Returns: An array with intersected curves. This array can be empty.
  """
  pass
 @staticmethod
 def CreateEdgeSurface(curves):
  """ CreateEdgeSurface(curves: IEnumerable[Curve]) -> Brep """
  pass
 @staticmethod
 def CreateFromBox(*__args):
  """
  CreateFromBox(corners: IEnumerable[Point3d]) -> Brep

  CreateFromBox(box: Box) -> Brep

  

   Constructs new brep that matches an aligned box.

  

   box: Box to match.

   Returns: A Brep with 6 faces that is similar to the Box.

  CreateFromBox(box: BoundingBox) -> Brep

  

   Constructs new brep that matches a bounding box.

  

   box: A box to use for creation.

   Returns: A new brep; or null on failure.
  """
  pass
 @staticmethod
 def CreateFromCone(cone,capBottom):
  """
  CreateFromCone(cone: Cone,capBottom: bool) -> Brep

  

   Constructs a Brep representation of the cone with a single

     face for the cone,an 

    edge along the cone seam,

     and vertices at the base and apex ends of this seam 

    edge.

     The optional cap is a single face with one circular edge 

     

    starting and ending at the base vertex.

  

  

   cone: A cone value.

   capBottom: if true the base of the cone should be capped.

   Returns: A new brep,on null on error.
  """
  pass
 @staticmethod
 def CreateFromCornerPoints(corner1,corner2,corner3,*__args):
  """
  CreateFromCornerPoints(corner1: Point3d,corner2: Point3d,corner3: Point3d,corner4: Point3d,tolerance: float) -> Brep

  

   make a Brep with one face.

  

   corner1: A first corner.

   corner2: A second corner.

   corner3: A third corner.

   corner4: A fourth corner.

   tolerance: Minimum edge length allowed before collapsing the side into a singularity.

   Returns: A boundary representation,or null on error.

  CreateFromCornerPoints(corner1: Point3d,corner2: Point3d,corner3: Point3d,tolerance: float) -> Brep

  

   Makes a brep with one face.

  

   corner1: A first corner.

   corner2: A second corner.

   corner3: A third corner.

   tolerance: Minimum edge length without collapsing to a singularity.

   Returns: A boundary representation,or null on error.
  """
  pass
 @staticmethod
 def CreateFromCylinder(cylinder,capBottom,capTop):
  """
  CreateFromCylinder(cylinder: Cylinder,capBottom: bool,capTop: bool) -> Brep

  

   Constructs a Brep definition of a cylinder.

  

   cylinder: cylinder.IsFinite() must be true.

   capBottom: if true end at cylinder.m_height[0] should be capped.

   capTop: if true end at cylinder.m_height[1] should be capped.

   Returns: A Brep representation of the cylinder with a single face for the cylinder,

     an edge 

    along the cylinder seam,and vertices at the bottom and top ends of this

     seam edge. 

    The optional bottom/top caps are single faces with one circular edge

     starting and 

    ending at the bottom/top vertex.
  """
  pass
 @staticmethod
 def CreateFromLoft(curves,start,end,loftType,closed):
  """ CreateFromLoft(curves: IEnumerable[Curve],start: Point3d,end: Point3d,loftType: LoftType,closed: bool) -> Array[Brep] """
  pass
 @staticmethod
 def CreateFromLoftRebuild(curves,start,end,loftType,closed,rebuildPointCount):
  """ CreateFromLoftRebuild(curves: IEnumerable[Curve],start: Point3d,end: Point3d,loftType: LoftType,closed: bool,rebuildPointCount: int) -> Array[Brep] """
  pass
 @staticmethod
 def CreateFromLoftRefit(curves,start,end,loftType,closed,refitTolerance):
  """ CreateFromLoftRefit(curves: IEnumerable[Curve],start: Point3d,end: Point3d,loftType: LoftType,closed: bool,refitTolerance: float) -> Array[Brep] """
  pass
 @staticmethod
 def CreateFromMesh(mesh,trimmedTriangles):
  """
  CreateFromMesh(mesh: Mesh,trimmedTriangles: bool) -> Brep

  

   Create a brep representation of a mesh

  

   trimmedTriangles: if true,triangles in the mesh will be represented by trimmed planes in

     the brep. 

    If false,triangles in the mesh will be represented by

     untrimmed singular bilinear 

    NURBS surfaces in the brep.
  """
  pass
 @staticmethod
 def CreateFromOffsetFace(face,offsetDistance,offsetTolerance,bothSides,createSolid):
  """
  CreateFromOffsetFace(face: BrepFace,offsetDistance: float,offsetTolerance: float,bothSides: bool,createSolid: bool) -> Brep

  

   Offsets a face including trim information to create a new brep.

  

   face: the face to offset.

   offsetDistance: An offset distance.

   offsetTolerance: Use 0.0 to make a loose offset. Otherwise,the document's absolute tolerance is usually 

    sufficient.

  

   bothSides: When true,offset to both sides of the input face.

   createSolid: When true,make a solid object.

   Returns: A new brep if successful. The brep can be disjoint if bothSides is true and createSolid is 

    false,

     or if createSolid is true and connecting the offsets with side surfaces 

    fails.

     null if unsuccessful.
  """
  pass
 @staticmethod
 def CreateFromRevSurface(surface,capStart,capEnd):
  """
  CreateFromRevSurface(surface: RevSurface,capStart: bool,capEnd: bool) -> Brep

  

   Constructs a brep form of a surface of revolution.

  

   surface: The surface of revolution.

   capStart: if true,the start of the revolute is not on the axis of revolution,

     and the 

    surface of revolution is closed,then a circular cap will be

     added to close of the 

    hole at the start of the revolute.

  

   capEnd: if true,the end of the revolute is not on the axis of revolution,

     and the surface 

    of revolution is closed,then a circular cap will be

     added to close of the hole at 

    the end of the revolute.

  

   Returns: A new brep,on null on error.
  """
  pass
 @staticmethod
 def CreateFromSphere(sphere):
  """
  CreateFromSphere(sphere: Sphere) -> Brep

  

   Constructs a Brep definition of a sphere.
  """
  pass
 @staticmethod
 def CreateFromSurface(surface):
  """
  CreateFromSurface(surface: Surface) -> Brep

  

   Constructs a Brep from a surface. The resulting Brep has an outer boundary made

     

    from four trims. The trims are ordered so that they run along the south,east,

     

    north,and then west side of the surface's parameter space.

  

  

   surface: A surface to convert.

   Returns: Resulting brep or null on failure.
  """
  pass
 @staticmethod
 def CreateFromSweep(*__args):
  """
  CreateFromSweep(rail1: Curve,rail2: Curve,shape: Curve,closed: bool,tolerance: float) -> Array[Brep]

  

   General 2 rail sweep. If you are not producing the sweep results that you are after,then

     

       use the SweepTwoRail class with options to generate the swept geometry

  

  

   rail1: Rail to sweep shapes along

   rail2: Rail to sweep shapes along

   shape: Shape curve

   closed: Only matters if shape is closed

   tolerance: Tolerance for fitting surface and rails

   Returns: Array of Brep sweep results

  CreateFromSweep(rail1: Curve,rail2: Curve,shapes: IEnumerable[Curve],closed: bool,tolerance: float) -> Array[Brep]

  CreateFromSweep(rail: Curve,shape: Curve,closed: bool,tolerance: float) -> Array[Brep]

  

   General 1 rail sweep. If you are not producing the sweep results that you are after,then

     

       use the SweepOneRail class with options to generate the swept geometry

  

  

   rail: Rail to sweep shapes along

   shape: Shape curve

   closed: Only matters if shape is closed

   tolerance: Tolerance for fitting surface and rails

   Returns: Array of Brep sweep results

  CreateFromSweep(rail: Curve,shapes: IEnumerable[Curve],closed: bool,tolerance: float) -> Array[Brep]
  """
  pass
 @staticmethod
 def CreateFromTaperedExtrude(curveToExtrude,distance,direction,basePoint,draftAngleRadians,cornerType):
  """
  CreateFromTaperedExtrude(curveToExtrude: Curve,distance: float,direction: Vector3d,basePoint: Point3d,draftAngleRadians: float,cornerType: ExtrudeCornerType) -> Array[Brep]

  

   Extrude a curve to a taper making a brep (potentially more than 1)

  

   curveToExtrude: the curve to extrude

   distance: the distance to extrude

   direction: the direction of the extrusion

   basePoint: the basepoint of the extrusion

   draftAngleRadians: angle of the extrusion

   Returns: array of breps on success
  """
  pass
 @staticmethod
 def CreatePatch(geometry,*__args):
  """
  CreatePatch(geometry: IEnumerable[GeometryBase],startingSurface: Surface,uSpans: int,vSpans: int,trim: bool,tangency: bool,pointSpacing: float,flexibility: float,surfacePull: float,fixEdges: Array[bool],tolerance: float) -> Brep

  CreatePatch(geometry: IEnumerable[GeometryBase],uSpans: int,vSpans: int,tolerance: float) -> Brep

  CreatePatch(geometry: IEnumerable[GeometryBase],startingSurface: Surface,tolerance: float) -> Brep
  """
  pass
 @staticmethod
 def CreatePipe(rail,*__args):
  """
  CreatePipe(rail: Curve,railRadiiParameters: IEnumerable[float],radii: IEnumerable[float],localBlending: bool,cap: PipeCapMode,fitRail: bool,absoluteTolerance: float,angleToleranceRadians: float) -> Array[Brep]

  CreatePipe(rail: Curve,radius: float,localBlending: bool,cap: PipeCapMode,fitRail: bool,absoluteTolerance: float,angleToleranceRadians: float) -> Array[Brep]

  

   Creates a single walled pipe

  

   rail: the path curve for the pipe

   radius: radius of the pipe

   localBlending: If True,Local (pipe radius stays constant at the ends and changes more rapidly in the middle) 

    is applied.

     If False,Global (radius is linearly blended from one end to the other,

    creating pipes that taper from one radius to the other) is applied

  

   cap: end cap mode

   fitRail: If the curve is a polycurve of lines and arcs,the curve is fit and a single surface is created;


    
     otherwise the result is a polysurface with joined surfaces created from the 

    polycurve segments.

  

   absoluteTolerance: The sweeping and fitting tolerance. If you are unsure what to use,then use the document's 

    absolute tolerance

  

   angleToleranceRadians: The angle tolerance. If you are unsure what to use,then either use the document's angle 

    tolerance in radians

  

   Returns: Array of created pipes on success
  """
  pass
 @staticmethod
 def CreatePlanarBreps(*__args):
  """
  CreatePlanarBreps(inputLoops: CurveList) -> Array[Brep]

  

   Constructs a set of planar Breps as outlines by the loops.

  

   inputLoops: Curve loops that delineate the planar boundaries.

   Returns: An array of Planar Breps or null on error.

  CreatePlanarBreps(inputLoop: Curve) -> Array[Brep]

  

   Constructs a set of planar breps as outlines by the loops.

  

   inputLoop: A curve that should form the boundaries of the surfaces or polysurfaces.

   Returns: An array of Planar Breps.

  CreatePlanarBreps(inputLoops: IEnumerable[Curve]) -> Array[Brep]
  """
  pass
 @staticmethod
 def CreateShell(brep,facesToRemove,distance,tolerance):
  """ CreateShell(brep: Brep,facesToRemove: IEnumerable[int],distance: float,tolerance: float) -> Array[Brep] """
  pass
 @staticmethod
 def CreateSolid(breps,tolerance):
  """ CreateSolid(breps: IEnumerable[Brep],tolerance: float) -> Array[Brep] """
  pass
 @staticmethod
 def CreateTrimmedSurface(trimSource,surfaceSource):
  """
  CreateTrimmedSurface(trimSource: BrepFace,surfaceSource: Surface) -> Brep

  

   Constructs a Brep using the trimming information of a brep face and a surface. 

     

    Surface must be roughly the same shape and in the same location as the trimming brep face.

  

  

   trimSource: BrepFace which contains trimmingSource brep.

   surfaceSource: Surface that trims of BrepFace will be applied to.

   Returns: A brep with the shape of surfaceSource and the trims of trimSource or null on failure.
  """
  pass
 def CullUnused2dCurves(self):
  """
  CullUnused2dCurves(self: Brep) -> bool

  

   Culls 3d curves not referenced by an edge.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnused3dCurves(self):
  """
  CullUnused3dCurves(self: Brep) -> bool

  

   Culls 2d curves not referenced by a trim.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedEdges(self):
  """
  CullUnusedEdges(self: Brep) -> bool

  

   Culls edges with m_edge_index == -1.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedFaces(self):
  """
  CullUnusedFaces(self: Brep) -> bool

  

   Culls faces with m_face_index == -1.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedLoops(self):
  """
  CullUnusedLoops(self: Brep) -> bool

  

   Culls loops with m_loop_index == -1.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedSurfaces(self):
  """
  CullUnusedSurfaces(self: Brep) -> bool

  

   Culls surfaces not referenced by a face.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedTrims(self):
  """
  CullUnusedTrims(self: Brep) -> bool

  

   Culls trims with m_trim_index == -1.

   Returns: true if operation succeeded; false otherwise.
  """
  pass
 def CullUnusedVertices(self):
  """
  CullUnusedVertices(self: Brep) -> bool

  

   Culls vertices with m_vertex_index == -1.

   Returns: true if operation succeeded; false otherwise.
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
  Duplicate(self: Brep) -> GeometryBase

  

   Copies this brep.

   Returns: A brep.
  """
  pass
 def DuplicateBrep(self):
  """
  DuplicateBrep(self: Brep) -> Brep

  

   Same as Rhino.Geometry.Brep.Duplicate,but already performs a cast to a brep.

     This 

    cast always succeeds.

  

   Returns: A brep.
  """
  pass
 def DuplicateEdgeCurves(self,nakedOnly=None):
  """
  DuplicateEdgeCurves(self: Brep,nakedOnly: bool) -> Array[Curve]

  

   Duplicate edges of this Brep.

  

   nakedOnly: If true,then only the "naked" edges are duplicated.

     If false,then all edges are 

    duplicated.

  

   Returns: Array of edge curves on success.

  DuplicateEdgeCurves(self: Brep) -> Array[Curve]

  

   Duplicate all the edges of this Brep.

   Returns: An array of edge curves.
  """
  pass
 def DuplicateNakedEdgeCurves(self,outer,inner):
  """
  DuplicateNakedEdgeCurves(self: Brep,outer: bool,inner: bool) -> Array[Curve]

  

   Duplicate naked edges of this Brep
  """
  pass
 def DuplicateSubBrep(self,faceIndices):
  """ DuplicateSubBrep(self: Brep,faceIndices: IEnumerable[int]) -> Brep """
  pass
 def DuplicateVertices(self):
  """
  DuplicateVertices(self: Brep) -> Array[Point3d]

  

   Duplicate all the corner vertices of this Brep.

   Returns: An array or corner vertices.
  """
  pass
 def Flip(self):
  """
  Flip(self: Brep)

   Reverses entire brep orientation of all faces.
  """
  pass
 def GetArea(self,relativeTolerance=None,absoluteTolerance=None):
  """
  GetArea(self: Brep) -> float

  

   Compute the Area of the Brep. If you want proper Area data with moments 

     and error 

    information,use the AreaMassProperties class.

  

   Returns: The area of the Brep.

  GetArea(self: Brep,relativeTolerance: float,absoluteTolerance: float) -> float

  

   Compute the Area of the Brep. If you want proper Area data with moments 

     and error 

    information,use the AreaMassProperties class.

  

  

   relativeTolerance: Relative tolerance to use for area calculation.

   absoluteTolerance: Absolute tolerance to use for area calculation.

   Returns: The area of the Brep.
  """
  pass
 def GetRegions(self):
  """
  GetRegions(self: Brep) -> Array[BrepRegion]

  

   Gets an array containing all regions in this brep.

   Returns: An array of regions in this brep. This array can be empty,but not null.
  """
  pass
 def GetVolume(self,relativeTolerance=None,absoluteTolerance=None):
  """
  GetVolume(self: Brep,relativeTolerance: float,absoluteTolerance: float) -> float

  

   Compute the Volume of the Brep. If you want proper Volume data with moments 

     and 

    error information,use the VolumeMassProperties class.

  

  

   relativeTolerance: Relative tolerance to use for area calculation.

   absoluteTolerance: Absolute tolerance to use for area calculation.

   Returns: The volume of the Brep.

  GetVolume(self: Brep) -> float

  

   Compute the Volume of the Brep. If you want proper Volume data with moments 

     and 

    error information,use the VolumeMassProperties class.

  

   Returns: The volume of the Brep.
  """
  pass
 def GetWireframe(self,density):
  """
  GetWireframe(self: Brep,density: int) -> Array[Curve]

  

   Constructs all the Wireframe curves for this Brep.

  

   density: Wireframe density. Valid values range between -1 and 99.

   Returns: An array of Wireframe curves or null on failure.
  """
  pass
 def IsDuplicate(self,other,tolerance):
  """
  IsDuplicate(self: Brep,other: Brep,tolerance: float) -> bool

  

   See if this and other are same brep geometry.

  

   other: other brep.

   tolerance: tolerance to use when comparing control points.

   Returns: true if breps are the same.
  """
  pass
 def IsPointInside(self,point,tolerance,strictlyIn):
  """
  IsPointInside(self: Brep,point: Point3d,tolerance: float,strictlyIn: bool) -> bool

  

   Determines if point is inside Brep.  This question only makes sense when

     the brep 

    is a closed manifold.  This function does not not check for

     closed or manifold,so 

    result is not valid in those cases.  Intersects

     a line through point with brep,

    finds the intersection point Q closest

     to point,and looks at face normal at Q.  If 

    the point Q is on an edge

     or the intersection is not transverse at Q,then another 

    line is used.

  

  

   point: 3d point to test.

   tolerance: 3d distance tolerance used for intersection and determining strict inclusion.

     A 

    good default is RhinoMath.SqrtEpsilon.

  

   strictlyIn: if true,point is in if inside brep by at least tolerance.

     if false,point is in if 

    truly in or within tolerance of boundary.

  

   Returns: true if point is in,false if not.
  """
  pass
 def IsValidGeometry(self,log):
  """
  IsValidGeometry(self: Brep) -> (bool,str)

  

   Expert user function that tests the brep to see if its geometry information is valid.

      

      The value of brep.IsValidTopology() must be true before brep.IsValidGeometry() can be

    

     safely called.

  

   Returns: A value that indicates whether the geometry is valid.
  """
  pass
 def IsValidTolerancesAndFlags(self,log):
  """
  IsValidTolerancesAndFlags(self: Brep) -> (bool,str)

  

   Expert user function that tests the brep to see if its tolerances and

     flags are 

    valid.  The values of brep.IsValidTopology() and

     brep.IsValidGeometry() must be 

    true before brep.IsValidTolerancesAndFlags()

     can be safely called.

  

   Returns: A value that indicates
  """
  pass
 def IsValidTopology(self,log):
  """
  IsValidTopology(self: Brep) -> (bool,str)

  

   Tests the brep to see if its topology information is valid.

   Returns: true if the topology is valid; false otherwise.
  """
  pass
 def Join(self,otherBrep,tolerance,compact):
  """
  Join(self: Brep,otherBrep: Brep,tolerance: float,compact: bool) -> bool

  

   If any edges of this brep overlap edges of otherBrep,merge a copy of otherBrep into this

     

       brep joining all edges that overlap within tolerance.

  

  

   otherBrep: Brep to be added to this brep.

   tolerance: 3d distance tolerance for detecting overlapping edges.

   compact: if true,set brep flags and tolerances,remove unused faces and edges.

   Returns: true if any edges were joined.
  """
  pass
 @staticmethod
 def JoinBreps(brepsToJoin,tolerance):
  """ JoinBreps(brepsToJoin: IEnumerable[Brep],tolerance: float) -> Array[Brep] """
  pass
 def JoinNakedEdges(self,tolerance):
  """
  JoinNakedEdges(self: Brep,tolerance: float) -> int

  

   Joins naked edge pairs within the same brep that overlap within tolerance.

  

   tolerance: The tolerance value.

   Returns: number of joins made.
  """
  pass
 @staticmethod
 def MergeBreps(brepsToMerge,tolerance):
  """ MergeBreps(brepsToMerge: IEnumerable[Brep],tolerance: float) -> Brep """
  pass
 def MergeCoplanarFaces(self,tolerance):
  """
  MergeCoplanarFaces(self: Brep,tolerance: float) -> bool

  

   Merges adjacent coplanar faces into single faces.

  

   tolerance: 3d tolerance for determining when edges are adjacent.

   Returns: true if faces were merged.  false if no faces were merged.
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
 def RebuildTrimsForV2(self,face,nurbsSurface):
  """
  RebuildTrimsForV2(self: Brep,face: BrepFace,nurbsSurface: NurbsSurface)

   No support is available for this function.

     Expert user function used by 

    MakeValidForV2 to convert trim

     curves from one surface to its NURBS form. After 

    calling this function,

     you need to change the surface of the face to a 

    NurbsSurface.

  

  

   face: Face whose underlying surface has a parameterization that is different

     from its 

    NURBS form.

  

   nurbsSurface: NURBS form of the face's underlying surface.
  """
  pass
 def SetTrimIsoFlags(self):
  """
  SetTrimIsoFlags(self: Brep)

   This function can be used to set the BrepTrim::m_iso

     flag. It is intended to be 

    used when creating a Brep from

     a definition that does not include compatible 

    parameter space

     type information.
  """
  pass
 def SetVertices(self):
  """
  SetVertices(self: Brep)

   This function can be used to compute vertex information for a

     b-rep when everything 

    but the Vertices array is properly filled in.

     It is intended to be used when 

    creating a Brep from a 

     definition that does not include explicit vertex 

    information.
  """
  pass
 def Split(self,splitter,intersectionTolerance,toleranceWasRaised=None):
  """
  Split(self: Brep,splitter: Brep,intersectionTolerance: float) -> (Array[Brep],bool)

  

   Splits a Brep into pieces.

  

   splitter: The splitting polysurface.

   intersectionTolerance: The tolerance with which to compute intersections.

   Returns: A new array of breps. This array can be empty.

  Split(self: Brep,splitter: Brep,intersectionTolerance: float) -> Array[Brep]

  

   Splits a Brep into pieces.

  

   splitter: A splitting surface or polysurface.

   intersectionTolerance: The tolerance with which to compute intersections.

   Returns: A new array of breps. This array can be empty.
  """
  pass
 def Standardize(self):
  """
  Standardize(self: Brep)

   Standardizes all trims,edges,and faces in the brep.

     After standardizing,there 

    may be unused curves and surfaces in the

     brep.  Call Brep.Compact to remove these 

    unused curves and surfaces.
  """
  pass
 def Trim(self,cutter,intersectionTolerance):
  """
  Trim(self: Brep,cutter: Plane,intersectionTolerance: float) -> Array[Brep]

  

   Trims a Brep with an oriented cutter.  The parts of Brep that lie inside

     (opposite 

    the normal) of the cutter are retained while the parts to the

     outside ( in the 

    direction of the normal ) are discarded. A connected

     component of Brep that does 

    not intersect the cutter is kept if and only

     if it is contained in the inside of 

    Cutter.  That is the region bounded by

     cutter opposite from the normal of cutter,

    or in the case of a Plane cutter

     the halfspace opposite from the plane normal.

  

  

   cutter: A cutting plane.

   intersectionTolerance: A tolerance value with which to compute intersections.

   Returns: This Brep is not modified,the trim results are returned in an array.

  Trim(self: Brep,cutter: Brep,intersectionTolerance: float) -> Array[Brep]

  

   Trims a brep with an oriented cutter. The parts of the brep that lie inside

     

    (opposite the normal) of the cutter are retained while the parts to the

     outside (in 

    the direction of the normal) are discarded.  If the Cutter is

     closed,then a 

    connected component of the Brep that does not intersect the

     cutter is kept if and 

    only if it is contained in the inside of cutter.

     That is the region bounded by 

    cutter opposite from the normal of cutter,

     If cutter is not closed all these 

    components are kept.

  

  

   cutter: A cutting brep.

   intersectionTolerance: A tolerance value with which to compute intersections.

   Returns: This Brep is not modified,the trim results are returned in an array.
  """
  pass
 @staticmethod
 def TryConvertBrep(geometry):
  """
  TryConvertBrep(geometry: GeometryBase) -> Brep

  

   Attempts to convert a generic Geometry object into a Brep.

  

   geometry: Geometry to convert,not all types of GeometryBase can be represented by BReps.

   Returns: Brep if a brep form could be created or null if this is not possible. If geometry was of type 

    Brep to 

     begin with,the same object is returned,i.e. it is not duplicated.
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
 Curves2D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parameter space trimming curves (used by trims)



Get: Curves2D(self: Brep) -> BrepCurveList



"""

 Curves3D=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Pointers to 3d curves (used by edges)



Get: Curves3D(self: Brep) -> BrepCurveList



"""

 Edges=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the brep edges list accessor.



Get: Edges(self: Brep) -> BrepEdgeList



"""

 Faces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the brep faces list accessor.



Get: Faces(self: Brep) -> BrepFaceList



"""

 IsManifold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether or not the Brep is manifold. 

   Non-Manifold breps have at least one edge that is shared among three or more faces.



Get: IsManifold(self: Brep) -> bool



"""

 IsSolid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines whether this brep is a solid,or a closed oriented manifold.



Get: IsSolid(self: Brep) -> bool



"""

 IsSurface=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns true if the Brep has a single face and that face is geometrically the same

   as the underlying surface.  I.e.,the face has trivial trimming.

   In this case,the surface is the first face surface. The flag

   Brep.Faces[0].OrientationIsReversed records the correspondence between the surface's

   natural parametric orientation and the orientation of the Brep.trivial trimming here means that there is only one loop curve in the brep

   and that loop curve is the same as the underlying surface boundary.



Get: IsSurface(self: Brep) -> bool



"""

 Loops=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the brep loop list accessor.



Get: Loops(self: Brep) -> BrepLoopList



"""

 SolidOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the solid orientation state of this Brep.



Get: SolidOrientation(self: Brep) -> BrepSolidOrientation



"""

 Surfaces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Parametric surfaces used by faces



Get: Surfaces(self: Brep) -> BrepSurfaceList



"""

 Trims=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the brep trims list accessor.



Get: Trims(self: Brep) -> BrepTrimList



"""

 Vertices=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """



Get: Vertices(self: Brep) -> BrepVertexList



"""


