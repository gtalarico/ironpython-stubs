# encoding: utf-8
# module Rhino.Geometry.Collections calls itself Collections
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BrepCurveList(object, IEnumerable[Curve], IEnumerable, IRhinoTable[Curve]):
    """ Provides access to all the underlying curves in a Brep object. """
    def Add(self, curve):
        """
        Add(self: BrepCurveList, curve: Curve) -> int
        
            Adds a curve
        
            curve: A copy of the curve is added to this brep
            Returns: Index that should be used to reference the geometry.
                    -1 is returned if the input is 
             not acceptable.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepCurveList) -> IEnumerator[Curve]
        
            Get an enumerator that visits all curves.
            Returns: The enumerator.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Curve](enumerable: IEnumerable[Curve], value: Curve) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of curves in this list.

Get: Count(self: BrepCurveList) -> int

"""



class BrepEdgeList(object, IEnumerable[BrepEdge], IEnumerable, IRhinoTable[BrepEdge]):
    """ Provides access to all the Edges in a Brep object. """
    def Add(self, *__args):
        """
        Add(self: BrepEdgeList, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge
        
            Create and add a new edge to this list
        Add(self: BrepEdgeList, startVertexIndex: int, endVertexIndex: int, curve3dIndex: int, edgeTolerance: float) -> BrepEdge
        
            Create and add a new edge to this list
        Add(self: BrepEdgeList, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, edgeTolerance: float) -> BrepEdge
        
            Create and add a new edge to this list
        Add(self: BrepEdgeList, curve3dIndex: int) -> BrepEdge
        
            Create and add a new edge to this list
        Add(self: BrepEdgeList, startVertex: BrepVertex, endVertex: BrepVertex, curve3dIndex: int, subDomain: Interval, edgeTolerance: float) -> BrepEdge
        
            Create and add a new edge to this list
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepEdgeList) -> IEnumerator[BrepEdge]
        
            Gets an enumerator that visits all edges.
            Returns: The enumerator.
        """
        pass

    def SplitEdgeAtParameters(self, edgeIndex, edgeParameters):
        """ SplitEdgeAtParameters(self: BrepEdgeList, edgeIndex: int, edgeParameters: IEnumerable[float]) -> int """
        pass

    def SplitKinkyEdge(self, edgeIndex, kinkToleranceRadians):
        """
        SplitKinkyEdge(self: BrepEdgeList, edgeIndex: int, kinkToleranceRadians: float) -> bool
        
            Splits the edge into G1 pieces.
        
            edgeIndex: Index of edge to test and split.
            kinkToleranceRadians: The split tolerance in radians.
            Returns: true if successful.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepEdge](enumerable: IEnumerable[BrepEdge], value: BrepEdge) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of brep edges.

Get: Count(self: BrepEdgeList) -> int

"""



class BrepFaceList(object, IEnumerable[BrepFace], IEnumerable, IRhinoTable[BrepFace]):
    """ Provides access to all the Faces in a Brep object. """
    def Add(self, *__args):
        """
        Add(self: BrepFaceList, surface: Surface) -> BrepFace
        
            Add a new face to a brep.  This creates a complete face with
                    new vertices at the 
             surface corners, new edges along the surface
                    boundary, etc.  The loop of the 
             returned face has four trims that
                    correspond to the south, east, north, and west 
             side of the 
                    surface in that order.  If you use this version of Add to
                    
             add an exiting brep, then you are responsible for using a tool
                    like JoinEdges() to 
             hook the new face to its neighbors.
        
        
            surface: surface is copied
        Add(self: BrepFaceList, surfaceIndex: int) -> BrepFace
        
            Create and add a new face to this list. An incomplete face is added.
                    The caller 
             must create and fill in the loops used by the face.
        
        
            surfaceIndex: index of surface in brep's Surfaces list
        """
        pass

    def AddConeFace(self, vertex, edge, revEdge):
        """
        AddConeFace(self: BrepFaceList, vertex: BrepVertex, edge: BrepEdge, revEdge: bool) -> BrepFace
        
            Add a new face to the brep whose surface geometry is a 
                    ruled cone with the edge as 
             the base and the vertex as
                    the apex point.
        
        
            vertex: The apex of the cone will be at this vertex.
                    The north side of the surface's 
             parameter
                    space will be a singular point at the vertex.
        
            edge: The south side of the face's surface will run along this edge.
            revEdge: true if the new face's outer boundary orientation along
                    the edge is opposite the 
             orientation of edge.
        """
        pass

    def AddRuledFace(self, edgeA, revEdgeA, edgeB, revEdgeB):
        """
        AddRuledFace(self: BrepFaceList, edgeA: BrepEdge, revEdgeA: bool, edgeB: BrepEdge, revEdgeB: bool) -> BrepFace
        
            Add a new face to the brep whose surface geometry is a 
                    ruled surface between two 
             edges.
        
        
            edgeA: The south side of the face's surface will run along edgeA.
            revEdgeA: true if the new face's outer boundary orientation along
                    edgeA is opposite the 
             orientation of edgeA.
        
            edgeB: The north side of the face's surface will run along edgeA
            revEdgeB: true if the new face's outer boundary orientation along
                    edgeB is opposite the 
             orientation of edgeB
        """
        pass

    def ExtractFace(self, faceIndex):
        """
        ExtractFace(self: BrepFaceList, faceIndex: int) -> Brep
        
            Extracts a face from a Brep.
        
            faceIndex: A face index
            Returns: A brep. This can be null.
        """
        pass

    def Flip(self, onlyReversedFaces):
        """
        Flip(self: BrepFaceList, onlyReversedFaces: bool)
            Flips the orientation of faces.
        
            onlyReversedFaces: If true, clears all BrepFace.OrientationIsReversed flags by calling BrepFace.Transpose()
               
                  on each face with a true OrientationIsReversed setting.
                    If false, all of the 
             faces are flipped regardless of their orientation.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepFaceList) -> IEnumerator[BrepFace]
        
            Gets an enumerators that yields Rhino.Geometry.BrepFace objects.
            Returns: The enumerator.
        """
        pass

    def RemoveAt(self, faceIndex):
        """
        RemoveAt(self: BrepFaceList, faceIndex: int)
            Deletes a face at a specified index.
        
            faceIndex: The index of the mesh face.
        """
        pass

    def RemoveSlits(self):
        """
        RemoveSlits(self: BrepFaceList) -> bool
        
            Remove slit trims and slit boundaries from each face.
            Returns: true if any slits were removed
        """
        pass

    def ShrinkFaces(self):
        """
        ShrinkFaces(self: BrepFaceList) -> bool
        
            Shrinks all the faces in this Brep. Sometimes the surfaces extend far beyond the trimming 
             
                    boundaries of the Brep Face. This function will remove those portions of the surfaces 
          
                       that are not used.
        
            Returns: true on success, false on failure.
        """
        pass

    def SplitBipolarFaces(self):
        """
        SplitBipolarFaces(self: BrepFaceList) -> bool
        
            Splits surfaces with two singularities, like spheres, so the results
                    have at most 
             one singularity.
        
            Returns: true if successful.
        """
        pass

    def SplitClosedFaces(self, minimumDegree):
        """
        SplitClosedFaces(self: BrepFaceList, minimumDegree: int) -> bool
        
            Splits closed surfaces so they are not closed.
        
            minimumDegree: If the degree of the surface < min_degree, the surface is not split.
                    In some cases, 
             minimumDegree = 2 is useful to preserve piecewise linear
                    surfaces.
        
            Returns: true if successful.
        """
        pass

    def SplitKinkyFace(self, faceIndex, kinkTolerance):
        """
        SplitKinkyFace(self: BrepFaceList, faceIndex: int, kinkTolerance: float) -> bool
        
            Splits a single face into G1 pieces.
        
            faceIndex: The index of the face to split.
            kinkTolerance: Tolerance (in radians) to use for crease detection.
            Returns: true on success, false on failure.
        """
        pass

    def SplitKinkyFaces(self, kinkTolerance=None, compact=None):
        """
        SplitKinkyFaces(self: BrepFaceList, kinkTolerance: float, compact: bool) -> bool
        
            Splits any faces with creases into G1 pieces.
        
            kinkTolerance: Tolerance (in radians) to use for crease detection.
            compact: If true, the Brep will be compacted if possible.
            Returns: true on success, false on failure.
        SplitKinkyFaces(self: BrepFaceList, kinkTolerance: float) -> bool
        
            Splits any faces with creases into G1 pieces.
        
            kinkTolerance: Tolerance (in radians) to use for crease detection.
            Returns: true on success, false on failure.
        SplitKinkyFaces(self: BrepFaceList) -> bool
        
            Splits any faces with creases into G1 pieces.
            Returns: true on success, false on failure.
        """
        pass

    def StandardizeFaceSurface(self, faceIndex):
        """
        StandardizeFaceSurface(self: BrepFaceList, faceIndex: int) -> bool
        
            Standardizes the relationship between a BrepFace and the 3d surface it
                    uses.  When 
             done, the face will be the only face that references its 3d
                    surface, and the 
             orientations of the face and 3d surface will be the same.
        
        
            faceIndex: The index of the face.
            Returns: true if successful.
        """
        pass

    def StandardizeFaceSurfaces(self):
        """
        StandardizeFaceSurfaces(self: BrepFaceList)
            Standardize all faces in the brep.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepFace](enumerable: IEnumerable[BrepFace], value: BrepFace) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of brep faces.

Get: Count(self: BrepFaceList) -> int

"""



class BrepLoopList(object, IEnumerable[BrepLoop], IEnumerable, IRhinoTable[BrepLoop]):
    """ Provides access to all the Loops in a Brep object. """
    def Add(self, loopType, face=None):
        """
        Add(self: BrepLoopList, loopType: BrepLoopType, face: BrepFace) -> BrepLoop
        
            Create a new boundary loop on a face.  After you get this
                    BrepLoop, you still need 
             to create the vertices, edges, 
                    and trims that define the loop.
        
            Returns: New loop that needs to be filled in
        Add(self: BrepLoopList, loopType: BrepLoopType) -> BrepLoop
        
            Create a new outer boundary loop that runs along the edges
                    of the underlying 
             surface.
        """
        pass

    def AddOuterLoop(self, faceIndex):
        """
        AddOuterLoop(self: BrepLoopList, faceIndex: int) -> BrepLoop
        
            Create a new outer boundary loop that runs along the sides
                    of the face's surface.  
             All the necessary trims, edges,
                    and vertices are created and added to the brep.
        
        
            faceIndex: index of face that needs an outer boundary
                    that runs along the sides of its surface.
            Returns: New outer boundary loop that is complete.
        """
        pass

    def AddPlanarFaceLoop(self, faceIndex, loopType, boundaryCurves):
        """ AddPlanarFaceLoop(self: BrepLoopList, faceIndex: int, loopType: BrepLoopType, boundaryCurves: IEnumerable[Curve]) -> BrepLoop """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepLoopList) -> IEnumerator[BrepLoop]
        
            Gets an enumerator that visits all edges.
            Returns: The enumerator.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepLoop](enumerable: IEnumerable[BrepLoop], value: BrepLoop) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of brep loops.

Get: Count(self: BrepLoopList) -> int

"""



class BrepSurfaceList(object, IEnumerable[Surface], IEnumerable, IRhinoTable[Surface]):
    """ Provides access to all the underlying surfaces in a Brep object. """
    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepSurfaceList) -> IEnumerator[Surface]
        
            Gets an enumerator that visits all surfaces.
            Returns: The enumerator.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Surface](enumerable: IEnumerable[Surface], value: Surface) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of surfaces in a brep.

Get: Count(self: BrepSurfaceList) -> int

"""



class BrepTrimList(object, IEnumerable[BrepTrim], IEnumerable, IRhinoTable[BrepTrim]):
    """ Provides access to all the Trims in a Brep object """
    def Add(self, *__args):
        """
        Add(self: BrepTrimList, rev3d: bool, edge: BrepEdge, curve2dIndex: int) -> BrepTrim
        
            Add a new trim that will be part of an inner, outer, or slit loop
                    to the brep
        
            rev3d: true if the edge and trim have opposite directions
            edge: 3d edge associated with this trim
            curve2dIndex: index of 2d trimming curve
            Returns: new trim
        Add(self: BrepTrimList, edge: BrepEdge, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim
        
            Add a new trim that will be part of an inner, outer, or slit loop
                    to the brep.
        
            edge: 3d edge associated with this trim
            rev3d: true if the edge and trim have opposite directions
            loop: trim is appended to this loop
            curve2dIndex: index of 2d trimming curve
            Returns: new trim
        Add(self: BrepTrimList, curve2dIndex: int) -> BrepTrim
        
            Add a new trim that will be part of an inner, outer, or slit loop
                    to the brep.
        
            curve2dIndex: index of 2d trimming curve
            Returns: New Trim
        Add(self: BrepTrimList, rev3d: bool, loop: BrepLoop, curve2dIndex: int) -> BrepTrim
        
            Add a new trim that will be part of an inner, outer, or slit loop
                    to the brep
        
            rev3d: true if the edge and trim have opposite directions
            loop: trim is appended to this loop
            curve2dIndex: index of 2d trimming curve
            Returns: new trim
        """
        pass

    def AddCurveOnFace(self, face, edge, rev3d, curve2dIndex):
        """
        AddCurveOnFace(self: BrepTrimList, face: BrepFace, edge: BrepEdge, rev3d: bool, curve2dIndex: int) -> BrepTrim
        
            Add a new curve on face to the brep
        
            face: face that curve lies on
            edge: 3d edge associated with this curve on surface
            rev3d: true if the 3d edge and the 2d parameter space curve have opposite directions.
            curve2dIndex: index of 2d curve in face's parameter space
            Returns: new trim that represents the curve on surface
        """
        pass

    def AddSingularTrim(self, vertex, loop, iso, curve2dIndex):
        """
        AddSingularTrim(self: BrepTrimList, vertex: BrepVertex, loop: BrepLoop, iso: IsoStatus, curve2dIndex: int) -> BrepTrim
        
            Add a new singular trim to the brep.
        
            vertex: vertex along collapsed surface edge
            loop: trim is appended to this loop
            curve2dIndex: index of 2d trimming curve
            Returns: new trim
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepTrimList) -> IEnumerator[BrepTrim]
        
            Gets an enumerator that visits all edges.
            Returns: The enumerator.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepTrim](enumerable: IEnumerable[BrepTrim], value: BrepTrim) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of brep trims.

Get: Count(self: BrepTrimList) -> int

"""



class BrepVertexList(object, IEnumerable[BrepVertex], IEnumerable, IRhinoTable[BrepVertex]):
    """ Provides access to all the Vertices in a Brep object """
    def Add(self, point=None, vertexTolerance=None):
        """
        Add(self: BrepVertexList, point: Point3d, vertexTolerance: float) -> BrepVertex
        
            Create and add a new vertex to this list
        
            vertexTolerance: Use RhinoMath.UnsetTolerance if you are unsure
        Add(self: BrepVertexList) -> BrepVertex
        
            Create and add a new vertex to this list
        """
        pass

    def AddPointOnFace(self, face, s, t):
        """
        AddPointOnFace(self: BrepVertexList, face: BrepFace, s: float, t: float) -> BrepVertex
        
            Adds a new point on face to the brep
        
            face: face that vertex lies on
            s: surface parameters
            t: surface parameters
            Returns: new vertex that represents the point on face
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: BrepVertexList) -> IEnumerator[BrepVertex]
        
            Gets an enumerator that visits all surfaces.
            Returns: The enumerator.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BrepVertex](enumerable: IEnumerable[BrepVertex], value: BrepVertex) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of brep vertices.

Get: Count(self: BrepVertexList) -> int

"""



class MeshFaceList(object, IEnumerable[MeshFace], IEnumerable, IRhinoTable[MeshFace]):
    """ Provides access to the faces and Face related functionality of a Mesh. """
    def AddFace(self, *__args):
        """
        AddFace(self: MeshFaceList, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> int
        
            Appends a new quadragular face to the end of the mesh face list.
        
            vertex1: Index of first face corner.
            vertex2: Index of second face corner.
            vertex3: Index of third face corner.
            vertex4: Index of fourth face corner.
            Returns: The index of the newly added quad.
        AddFace(self: MeshFaceList, vertex1: int, vertex2: int, vertex3: int) -> int
        
            Appends a new triangular face to the end of the mesh face list.
        
            vertex1: Index of first face corner.
            vertex2: Index of second face corner.
            vertex3: Index of third face corner.
            Returns: The index of the newly added triangle.
        AddFace(self: MeshFaceList, face: MeshFace) -> int
        
            Appends a new mesh face to the end of the mesh face list.
        
            face: Face to add.
            Returns: The index of the newly added face.
        """
        pass

    def AddFaces(self, faces):
        """ AddFaces(self: MeshFaceList, faces: IEnumerable[MeshFace]) -> Array[int] """
        pass

    def AdjacentFaces(self, faceIndex):
        """
        AdjacentFaces(self: MeshFaceList, faceIndex: int) -> Array[int]
        
            Gets all faces that share a topological edge with a given face.
        
            faceIndex: A face index.
            Returns: All indices that share an edge.
        """
        pass

    def Clear(self):
        """
        Clear(self: MeshFaceList)
            Clears the Face list on the mesh.
        """
        pass

    def ConvertQuadsToTriangles(self):
        """
        ConvertQuadsToTriangles(self: MeshFaceList) -> bool
        
            Splits all quads along the short diagonal.
            Returns: true on success, false on failure.
        """
        pass

    def ConvertTrianglesToQuads(self, angleToleranceRadians, minimumDiagonalLengthRatio):
        """
        ConvertTrianglesToQuads(self: MeshFaceList, angleToleranceRadians: float, minimumDiagonalLengthRatio: float) -> bool
        
            Joins adjacent triangles into quads if the resulting quad is 'nice'.
        
            angleToleranceRadians: Used to compare adjacent triangles' face normals. For two triangles 
                    to be 
             considered, the angle between their face normals has to 
                    be <= 
             angleToleranceRadians. When in doubt use RhinoMath.PI/90.0 (2 degrees).
        
            minimumDiagonalLengthRatio: ( <= 1.0) For two triangles to be considered the ratio of the 
                    resulting quad's 
             diagonals 
                    (length of the shortest diagonal)/(length of longest diagonal). 
               
                  has to be >= minimumDiagonalLengthRatio. When in doubt us .875.
        
            Returns: true on success, false on failure.
        """
        pass

    def CullDegenerateFaces(self):
        """
        CullDegenerateFaces(self: MeshFaceList) -> int
        
            Attempts to removes degenerate faces from the mesh.
                    Degenerate faces are faces that 
             contains such a combination of indices,
                    that their final shape collapsed in a line 
             or point.Before returning, this method also attempts to repair faces by juggling
                    
             vertex indices.
        
            Returns: The number of degenerate faces that were removed.
        """
        pass

    def DeleteFaces(self, faceIndexes):
        """ DeleteFaces(self: MeshFaceList, faceIndexes: IEnumerable[int]) -> int """
        pass

    def GetConnectedFaces(self, faceIndex, angleRadians, greaterThanAngle):
        """
        GetConnectedFaces(self: MeshFaceList, faceIndex: int, angleRadians: float, greaterThanAngle: bool) -> Array[int]
        
            Find all connected face indices where adjacent face normals meet
                    the criteria of 
             angleRadians and greaterThanAngle
        
        
            faceIndex: face index to start from
            angleRadians: angle to use for comparison of what is connected
            greaterThanAngle: If true angles greater than or equal to are considered connected.
                    If false, angles 
             less than or equal to are considerd connected.
        
            Returns: list of connected face indices
        """
        pass

    def GetConnectedFacesToEdges(self, startFaceIndex, treatNonmanifoldLikeUnwelded):
        """
        GetConnectedFacesToEdges(self: MeshFaceList, startFaceIndex: int, treatNonmanifoldLikeUnwelded: bool) -> Array[int]
        
            Uses startFaceIndex and finds all connected face indexes up to unwelded
                    or naked 
             edges. If treatNonmanifoldLikeUnwelded is true then non-manifold
                    edges will be 
             considered as unwelded or naked
        
        
            startFaceIndex: Initial face index
            treatNonmanifoldLikeUnwelded: True means non-manifold edges will be handled like unwelded edges, 
                    False means 
             they aren't considered
        
            Returns: Array of connected face indexes
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshFaceList) -> IEnumerator[MeshFace]
        
            Gets an enumerator that yields all faces in this collection.
            Returns: The enumerator.
        """
        pass

    def GetFace(self, index):
        """
        GetFace(self: MeshFaceList, index: int) -> MeshFace
        
            Returns the mesh face at the given index.
        
            index: Index of face to get. Must be larger than or equal to zero and 
                    smaller than the 
             Face Count of the mesh.
        
            Returns: The mesh face at the given index on success or MeshFace.Unset if the index is out of range.
        """
        pass

    def GetFaceBoundingBox(self, faceIndex):
        """
        GetFaceBoundingBox(self: MeshFaceList, faceIndex: int) -> BoundingBox
        
            Gets the bounding box of a face.
        
            faceIndex: A face index.
            Returns: A new bounding box, or Rhino.Geometry.BoundingBox.Empty on error.
        """
        pass

    def GetFaceCenter(self, faceIndex):
        """
        GetFaceCenter(self: MeshFaceList, faceIndex: int) -> Point3d
        
            Gets the center point of a face.
                    For a triangular face, this is considered the 
             centroid or barycenter.For a quad, this is considered the bimedians intersection
                    
             (the avarage of four points).
        
        
            faceIndex: A face index.
            Returns: The center point.
        """
        pass

    def GetFaceVertices(self, faceIndex, a, b, c, d):
        """
        GetFaceVertices(self: MeshFaceList, faceIndex: int) -> (bool, Point3f, Point3f, Point3f, Point3f)
        
            Gets the 3D location of the vertices forming a face.
        
            faceIndex: A face index.
            Returns: true if the operation succeeded, otherwise false.
        """
        pass

    def GetTopologicalVertices(self, faceIndex):
        """
        GetTopologicalVertices(self: MeshFaceList, faceIndex: int) -> Array[int]
        
            Gets the topology vertex indices of a face.
        
            faceIndex: A face index.
            Returns: An array of integers.
        """
        pass

    def HasNakedEdges(self, faceIndex):
        """
        HasNakedEdges(self: MeshFaceList, faceIndex: int) -> bool
        
            Returns true if at least one of the face edges are not topologically
                    connected to 
             any other faces.
        
        
            faceIndex: A face index.
            Returns: true if that face makes the mesh open, otherwise false.
        """
        pass

    def Insert(self, index, face):
        """
        Insert(self: MeshFaceList, index: int, face: MeshFace)
            Inserts a mesh face at a defined index in this list.
        
            index: An index.
            face: A face.
        """
        pass

    def IsHidden(self, faceIndex):
        """
        IsHidden(self: MeshFaceList, faceIndex: int) -> bool
        
            Gets a value indicating whether a face is hidden.
                    A face is hidden if, and only if, 
             at least one of its vertices is hidden.
        
        
            faceIndex: A face index.
            Returns: true if hidden, false if fully visible.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: MeshFaceList, index: int)
            Removes a face from the mesh.
        
            index: The index of the face that will be removed.
        """
        pass

    def SetFace(self, index, *__args):
        """
        SetFace(self: MeshFaceList, index: int, vertex1: int, vertex2: int, vertex3: int, vertex4: int) -> bool
        
            Sets a quadrangular face at a specific index of the mesh.
        
            index: A position in the list.
            vertex1: The first vertex index.
            vertex2: The second vertex index.
            vertex3: The third vertex index.
            vertex4: The fourth vertex index.
            Returns: true if the operation succeeded, otherwise false.
        SetFace(self: MeshFaceList, index: int, vertex1: int, vertex2: int, vertex3: int) -> bool
        
            Sets a triangular face at a specific index of the mesh.
        
            index: A position in the list.
            vertex1: The first vertex index.
            vertex2: The second vertex index.
            vertex3: The third vertex index.
            Returns: true if the operation succeeded, otherwise false.
        SetFace(self: MeshFaceList, index: int, face: MeshFace) -> bool
        
            Sets a face at a specific index of the mesh.
        
            index: A position in the list.
            face: A face.
            Returns: true if the operation succeeded, otherwise false.
        """
        pass

    def ToIntArray(self, asTriangles):
        """
        ToIntArray(self: MeshFaceList, asTriangles: bool) -> Array[int]
        
            Copies all of the faces to a linear integer of indices
        
            asTriangles: If set to true as triangles.
            Returns: The int array.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MeshFace](enumerable: IEnumerable[MeshFace], value: MeshFace) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh faces.

Get: Count(self: MeshFaceList) -> int

Set: Count(self: MeshFaceList) = value
"""

    QuadCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of faces that are quads (4 corners).

Get: QuadCount(self: MeshFaceList) -> int

"""

    TriangleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of faces that are triangles (3 corners).

Get: TriangleCount(self: MeshFaceList) -> int

"""



class MeshFaceNormalList(object, IEnumerable[Vector3f], IEnumerable, IRhinoTable[Vector3f]):
    """ Provides access to the Face normals of a Mesh. """
    def AddFaceNormal(self, *__args):
        """
        AddFaceNormal(self: MeshFaceNormalList, normal: Vector3d) -> int
        
            Appends a face normal to the list of mesh face normals.
        
            normal: New face normal.
            Returns: The index of the newly added face normal.
        AddFaceNormal(self: MeshFaceNormalList, normal: Vector3f) -> int
        
            Appends a face normal to the list of mesh face normals.
        
            normal: New face normal.
            Returns: The index of the newly added face normal.
        AddFaceNormal(self: MeshFaceNormalList, x: Single, y: Single, z: Single) -> int
        
            Appends a face normal to the list of mesh face normals.
        
            x: X component of face normal.
            y: Y component of face normal.
            z: Z component of face normal.
            Returns: The index of the newly added face normal.
        AddFaceNormal(self: MeshFaceNormalList, x: float, y: float, z: float) -> int
        
            Appends a face normal to the list of mesh face normals.
        
            x: X component of face normal.
            y: Y component of face normal.
            z: Z component of face normal.
            Returns: The index of the newly added face normal.
        """
        pass

    def Clear(self):
        """
        Clear(self: MeshFaceNormalList)
            Clears the Face Normal list on the mesh.
        """
        pass

    def ComputeFaceNormals(self):
        """
        ComputeFaceNormals(self: MeshFaceNormalList) -> bool
        
            Computes all the face normals for this mesh based on the physical shape of the mesh.
            Returns: true on success, false on failure.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshFaceNormalList) -> IEnumerator[Vector3f]
        
            Gets an enumerator that yields all normals in this collection.
            Returns: The enumerator.
        """
        pass

    def SetFaceNormal(self, index, *__args):
        """
        SetFaceNormal(self: MeshFaceNormalList, index: int, normal: Vector3d) -> bool
        
            Sets a face normal vector at an index using a single-precision vector.
        
            index: An index.
            normal: A normal vector.
            Returns: true on success; false on error.
        SetFaceNormal(self: MeshFaceNormalList, index: int, normal: Vector3f) -> bool
        
            Sets a face normal vector at an index using a single-precision vector.
        
            index: An index.
            normal: A normal vector.
            Returns: true on success; false on error.
        SetFaceNormal(self: MeshFaceNormalList, index: int, x: Single, y: Single, z: Single) -> bool
        
            Sets a face normal vector at an index using three single-precision numbers.
        
            index: An index.
            x: A x component.
            y: A y component.
            z: A z component.
            Returns: true on success; false on error.
        SetFaceNormal(self: MeshFaceNormalList, index: int, x: float, y: float, z: float) -> bool
        
            Sets a face normal vector at an index using three double-precision numbers.
        
            index: An index.
            x: A x component.
            y: A y component.
            z: A z component.
            Returns: true on success; false on error.
        """
        pass

    def UnitizeFaceNormals(self):
        """
        UnitizeFaceNormals(self: MeshFaceNormalList) -> bool
        
            Unitizes all the existing face normals.
            Returns: true on success, false on failure.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vector3f](enumerable: IEnumerable[Vector3f], value: Vector3f) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh face normals.

Get: Count(self: MeshFaceNormalList) -> int

Set: Count(self: MeshFaceNormalList) = value
"""



class MeshTextureCoordinateList(object, IEnumerable[Point2f], IEnumerable, IRhinoTable[Point2f]):
    """ Provides access to the Vertex Texture coordinates of a Mesh. """
    def Add(self, *__args):
        """
        Add(self: MeshTextureCoordinateList, tc: Point2f) -> int
        
            Adds a new texture coordinate to the end of the Texture list.
        
            tc: Texture coordinate to add.
            Returns: The index of the newly added texture coordinate.
        Add(self: MeshTextureCoordinateList, tc: Point3d) -> int
        
            Adds a new texture coordinate to the end of the Texture list.
        
            tc: Texture coordinate to add.
            Returns: The index of the newly added texture coordinate.
        Add(self: MeshTextureCoordinateList, s: Single, t: Single) -> int
        
            Adds a new texture coordinate to the end of the Texture list.
        
            s: S component of new texture coordinate.
            t: T component of new texture coordinate.
            Returns: The index of the newly added texture coordinate.
        Add(self: MeshTextureCoordinateList, s: float, t: float) -> int
        
            Adds a new texture coordinate to the end of the Texture list.
        
            s: S component of new texture coordinate.
            t: T component of new texture coordinate.
            Returns: The index of the newly added texture coordinate.
        """
        pass

    def AddRange(self, textureCoordinates):
        """
        AddRange(self: MeshTextureCoordinateList, textureCoordinates: Array[Point2f]) -> bool
        
            Appends an array of texture coordinates.
        
            textureCoordinates: Texture coordinates to append.
            Returns: true on success, false on failure.
        """
        pass

    def Clear(self):
        """
        Clear(self: MeshTextureCoordinateList)
            Clears the Texture Coordinate list on the mesh.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshTextureCoordinateList) -> IEnumerator[Point2f]
        
            Gets an enumerator that yields all texture coordinates in this collection.
            Returns: The enumerator.
        """
        pass

    def NormalizeTextureCoordinates(self):
        """
        NormalizeTextureCoordinates(self: MeshTextureCoordinateList) -> bool
        
            Scales the texture coordinates so the texture domains are [0,1] 
                    and eliminate any 
             texture rotations.
        
            Returns: true on success, false on failure.
        """
        pass

    def ReverseTextureCoordinates(self, direction):
        """
        ReverseTextureCoordinates(self: MeshTextureCoordinateList, direction: int) -> bool
        
            Reverses one coordinate direction of the texture coordinates.
                    The region of the 
             bitmap the texture uses does not change.
                    Either Us or Vs direction is flipped.
        
        
            direction: 0 = first texture coordinate is reversed.1 = second texture coordinate is reversed.
            Returns: true if operation succeeded; otherwise, false.
        """
        pass

    def SetTextureCoordinate(self, index, *__args):
        """
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, tc: Point2f) -> bool
        
            Sets or adds a texture coordinate to the Texture Coordinate List.
                    If [index] is 
             less than [Count], the existing coordinate at [index] will be modified.If [index] equals 
             [Count], a new coordinate is appended to the end of the coordinate list.If [index] is larger 
             than [Count], the function will return false.
        
        
            index: Index of texture coordinate to set.
            tc: Texture coordinate point.
            Returns: true on success, false on failure.
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, tc: Point3f) -> bool
        
            Sets or adds a texture coordinate to the Texture Coordinate List.
                    If [index] is 
             less than [Count], the existing coordinate at [index] will be modified.If [index] equals 
             [Count], a new coordinate is appended to the end of the coordinate list.If [index] is larger 
             than [Count], the function will return false.
        
        
            index: Index of texture coordinate to set.
            tc: Texture coordinate point.
            Returns: true on success, false on failure.
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, s: Single, t: Single) -> bool
        
            Sets or adds a texture coordinate to the Texture Coordinate List.
                    If [index] is 
             less than [Count], the existing coordinate at [index] will be modified.If [index] equals 
             [Count], a new coordinate is appended to the end of the coordinate list.If [index] is larger 
             than [Count], the function will return false.
        
        
            index: Index of texture coordinate to set.
            s: S component of texture coordinate.
            t: T component of texture coordinate.
            Returns: true on success, false on failure.
        SetTextureCoordinate(self: MeshTextureCoordinateList, index: int, s: float, t: float) -> bool
        
            Sets or adds a texture coordinate to the Texture Coordinate List.
                    If [index] is 
             less than [Count], the existing coordinate at [index] will be modified.If [index] equals 
             [Count], a new coordinate is appended to the end of the coordinate list.If [index] is larger 
             than [Count], the function will return false.
        
        
            index: Index of texture coordinate to set.
            s: S component of texture coordinate.
            t: T component of texture coordinate.
            Returns: true on success, false on failure.
        """
        pass

    def SetTextureCoordinates(self, *__args):
        """
        SetTextureCoordinates(self: MeshTextureCoordinateList, mapping: TextureMapping) -> bool
        
            Set all texture coordinates based on a texture mapping function
        
            mapping: The new mapping type.
            Returns: true on success, false on failure.
        SetTextureCoordinates(self: MeshTextureCoordinateList, textureCoordinates: Array[Point2f]) -> bool
        
            Sets all texture coordinates in one go.
        
            textureCoordinates: Texture coordinates to assign to the mesh.
            Returns: true on success, false on failure.
        """
        pass

    def TransposeTextureCoordinates(self):
        """
        TransposeTextureCoordinates(self: MeshTextureCoordinateList) -> bool
        
            Transposes texture coordinates.
                    The region of the bitmap the texture uses does not 
             change.
                    All texture coordinates rows (Us) become columns (Vs), and vice versa.
        
            Returns: true on success, false on failure.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point2f](enumerable: IEnumerable[Point2f], value: Point2f) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of texture coordinates.

Get: Count(self: MeshTextureCoordinateList) -> int

Set: Count(self: MeshTextureCoordinateList) = value
"""



class MeshTopologyEdgeList(object):
    """ Represents an entry point to the list of edges in a mesh topology. """
    def CollapseEdge(self, topologyEdgeIndex):
        """
        CollapseEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool
        
            Replaces a mesh edge with a vertex at its center and update adjacent faces as needed.
        
            topologyEdgeIndex: An index of a topology edge in Rhino.Geometry.Mesh.TopologyEdges.
            Returns: true if successful.
        """
        pass

    def EdgeLine(self, topologyEdgeIndex):
        """
        EdgeLine(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> Line
        
            Gets the 3d line along an edge.
        
            topologyEdgeIndex: The topology edge index.
            Returns: Line along edge. If input is not valid, an Invalid Line is returned.
        """
        pass

    def GetConnectedFaces(self, topologyEdgeIndex, faceOrientationMatchesEdgeDirection=None):
        """
        GetConnectedFaces(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> (Array[int], Array[bool])
        
            Gets indices of faces connected to an edge.
        
            topologyEdgeIndex: An index of a topology edge that is queried.
            Returns: An array of face indices the edge borders. This might be empty on error.
        GetConnectedFaces(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> Array[int]
        
            Gets indices of faces connected to an edge.
        
            topologyEdgeIndex: An index of a topology edge that is queried.
            Returns: An array of face indices the edge borders. This might be empty on error.
        """
        pass

    def GetEdgeIndex(self, topologyVertex1, topologyVertex2):
        """
        GetEdgeIndex(self: MeshTopologyEdgeList, topologyVertex1: int, topologyVertex2: int) -> int
        
            Returns index of edge that connects topological vertices. 
                    returns -1 if no edge is 
             found.
        
        
            topologyVertex1: The first topology vertex index.
            topologyVertex2: The second topology vertex index.
            Returns: The edge index.
        """
        pass

    def GetEdgesForFace(self, faceIndex, sameOrientation=None):
        """
        GetEdgesForFace(self: MeshTopologyEdgeList, faceIndex: int) -> (Array[int], Array[bool])
        
            Gets indices of edges that surround a given face.
        
            faceIndex: A face index.
            Returns: A new array of indices to the topological edges that are connected with the specified face.
        GetEdgesForFace(self: MeshTopologyEdgeList, faceIndex: int) -> Array[int]
        
            Gets indices of edges that surround a given face.
        
            faceIndex: A face index.
            Returns: A new array of indices to the topological edges that are connected with the specified face.
        """
        pass

    def GetTopologyVertices(self, topologyEdgeIndex):
        """
        GetTopologyVertices(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> IndexPair
        
            Gets the two topology vertices for a given topology edge.
        
            topologyEdgeIndex: An index of a topology edge.
            Returns: The pair of vertex indices the edge connects.
        """
        pass

    def IsHidden(self, topologyEdgeIndex):
        """
        IsHidden(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool
        
            Returns true if the topological edge is hidden. The mesh topology
                    edge is hidden 
             only if either of its mesh topology vertices is hidden.
        
        
            topologyEdgeIndex: An index of a topology edge in Rhino.Geometry.Mesh.TopologyEdges.
            Returns: true if mesh topology edge is hidden.
        """
        pass

    def IsSwappableEdge(self, topologyEdgeIndex):
        """
        IsSwappableEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool
        
            Determines if a mesh edge index is valid input for 
             Rhino.Geometry.Collections.MeshTopologyEdgeList.SwapEdge(System.Int32).
        
        
            topologyEdgeIndex: An index of a topology edge in Rhino.Geometry.Mesh.TopologyEdges.
            Returns: true if edge can be swapped.
        """
        pass

    def SplitEdge(self, topologyEdgeIndex, *__args):
        """
        SplitEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int, point: Point3d) -> bool
        
            Divides a mesh edge to create two or more triangles
        
            topologyEdgeIndex: Edge to divide
            point: Location to perform the split
            Returns: true if successful
        SplitEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int, t: float) -> bool
        
            Divides a mesh edge to create two or more triangles
        
            topologyEdgeIndex: Edge to divide
            t: Parameter along edge. This is the same as getting an EdgeLine and calling PointAt(t) on that line
            Returns: true if successful
        """
        pass

    def SwapEdge(self, topologyEdgeIndex):
        """
        SwapEdge(self: MeshTopologyEdgeList, topologyEdgeIndex: int) -> bool
        
            If the edge is shared by two triangular face, then the edge is swapped.
        
            topologyEdgeIndex: An index of a topology edge in Rhino.Geometry.Mesh.TopologyEdges.
            Returns: true if successful.
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the amount of edges in this list.

Get: Count(self: MeshTopologyEdgeList) -> int

"""



class MeshTopologyVertexList(object, IEnumerable[Point3f], IEnumerable, IRhinoTable[Point3f]):
    """
    Provides access to the mesh topology vertices of a mesh. Topology vertices are
                sets of vertices in the MeshVertexList that can topologically be considered the
                same vertex.
    """
    def ConnectedFaces(self, topologyVertexIndex):
        """
        ConnectedFaces(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int]
        
            Gets all faces that are connected to a given vertex.
        
            topologyVertexIndex: Index of a topology vertex in Mesh.TopologyVertices.
            Returns: Indices of all faces in Mesh.Faces that are connected to this topological vertex.
                    
             null if no faces are connected to this vertex.
        """
        pass

    def ConnectedTopologyVertices(self, topologyVertexIndex, sorted=None):
        """
        ConnectedTopologyVertices(self: MeshTopologyVertexList, topologyVertexIndex: int, sorted: bool) -> Array[int]
        
            Gets all topological vertices that are connected to a given vertex.
        
            topologyVertexIndex: index of a topology vertex in Mesh.TopologyVertices.
            sorted: if true, thr vertices are returned in a radially sorted order.
            Returns: Indices of all topological vertices that are connected to this topological vertex.
                    
             null if no vertices are connected to this vertex.
        
        ConnectedTopologyVertices(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int]
        
            Gets all topological vertices that are connected to a given vertex.
        
            topologyVertexIndex: index of a topology vertex in Mesh.TopologyVertices.
            Returns: Indices of all topological vertices that are connected to this topological vertex.
                    
             null if no vertices are connected to this vertex.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshTopologyVertexList) -> IEnumerator[Point3f]
        
            Gets an enumerator that yields all topology vertices in this collection.
            Returns: The enumerator.
        """
        pass

    def IndicesFromFace(self, faceIndex):
        """
        IndicesFromFace(self: MeshTopologyVertexList, faceIndex: int) -> Array[int]
        
            Returns TopologyVertexIndices for a given mesh face index.
        
            faceIndex: The index of a face to query.
            Returns: An array of vertex indices.
        """
        pass

    def IsHidden(self, topologyVertexIndex):
        """
        IsHidden(self: MeshTopologyVertexList, topologyVertexIndex: int) -> bool
        
            Returns true if the topological vertex is hidden. The mesh topology
                    vertex is 
             hidden if and only if all the ON_Mesh vertices it represents is hidden.
        
        
            topologyVertexIndex: index of a topology vertex in Mesh.TopologyVertices.
            Returns: true if mesh topology vertex is hidden.
        """
        pass

    def MeshVertexIndices(self, topologyVertexIndex):
        """
        MeshVertexIndices(self: MeshTopologyVertexList, topologyVertexIndex: int) -> Array[int]
        
            Gets all indices of the mesh vertices that a given topology vertex represents.
        
            topologyVertexIndex: Index of a topology vertex in Mesh.TopologyVertices to query.
            Returns: Indices of all vertices that in Mesh.Vertices that a topology vertex represents.
        """
        pass

    def SortEdges(self, topologyVertexIndex=None):
        """
        SortEdges(self: MeshTopologyVertexList, topologyVertexIndex: int) -> bool
        
            Sorts the edge list for as single mesh topology vertex so that
                    the edges are in 
             radial order when you call ConnectedTopologyVertices.
                    A nonmanifold edge is treated 
             as a boundary edge with respect
                    to sorting.  If any boundary or nonmanifold edges 
             end at the
                    vertex, then the first edge will be a boundary or nonmanifold edge.
        
        
            topologyVertexIndex: index of a topology vertex in Mesh.TopologyVertices>
            Returns: true on success.
        SortEdges(self: MeshTopologyVertexList) -> bool
        
            Sorts the edge list for the mesh topology vertex list so that
                    the edges are in 
             radial order when you call ConnectedTopologyVertices.
                    A nonmanifold edge is treated 
             as a boundary edge with respect
                    to sorting.  If any boundary or nonmanifold edges 
             end at the
                    vertex, then the first edge will be a boundary or nonmanifold edge.
        
            Returns: true on success.
        """
        pass

    def TopologyVertexIndex(self, vertexIndex):
        """
        TopologyVertexIndex(self: MeshTopologyVertexList, vertexIndex: int) -> int
        
            Gets the topology vertex index for an existing mesh vertex in the mesh's
                    VertexList.
        
            vertexIndex: Index of a vertex in the Mesh.Vertices.
            Returns: Index of a topology vertex in the Mesh.TopologyVertices.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point3f](enumerable: IEnumerable[Point3f], value: Point3f) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh topology vertices.

Get: Count(self: MeshTopologyVertexList) -> int

"""



class MeshVertexColorList(object, IEnumerable[Color], IEnumerable, IRhinoTable[Color]):
    """ Provides access to the vertex colors of a mesh object. """
    def Add(self, *__args):
        """
        Add(self: MeshVertexColorList, color: Color) -> int
        
            Adds a new vertex color to the end of the color list.
        
            color: Color to append, Alpha channels will be ignored.
            Returns: The index of the newly added color.
        Add(self: MeshVertexColorList, red: int, green: int, blue: int) -> int
        
            Adds a new vertex color to the end of the color list.
        
            red: Red component of color, must be in the 0~255 range.
            green: Green component of color, must be in the 0~255 range.
            blue: Blue component of color, must be in the 0~255 range.
            Returns: The index of the newly added color.
        """
        pass

    def AppendColors(self, colors):
        """
        AppendColors(self: MeshVertexColorList, colors: Array[Color]) -> bool
        
            Appends a collection of colors to the vertex color list. 
                    For the Mesh to be valid, 
             the number of colors must match the number of vertices.
        
        
            colors: Colors to append.
            Returns: true on success, false on failure.
        """
        pass

    def Clear(self):
        """
        Clear(self: MeshVertexColorList)
            Clears the vertex color list on the mesh.
        """
        pass

    def CreateMonotoneMesh(self, baseColor):
        """
        CreateMonotoneMesh(self: MeshVertexColorList, baseColor: Color) -> bool
        
            Constructs a valid vertex color list consisting of a single color.
        
            baseColor: Color to apply to every vertex.
            Returns: true on success, false on failure.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshVertexColorList) -> IEnumerator[Color]
        
            Gets an enumerator that yields all colors in this collection.
            Returns: The enumerator.
        """
        pass

    def SetColor(self, *__args):
        """
        SetColor(self: MeshVertexColorList, face: MeshFace, color: Color) -> bool
        
            Sets a color at the three or four vertex indices of a specified face.
        
            face: A face to use to retrieve indices.
            color: A color.
            Returns: true on success; false on error.
        SetColor(self: MeshVertexColorList, index: int, color: Color) -> bool
        
            Sets or adds a vertex to the Vertex List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex color to set. 
                    If index equals Count, then the color will be 
             appended.
        
            color: Color to set, Alpha channels will be ignored.
            Returns: true on success, false on failure.
        SetColor(self: MeshVertexColorList, index: int, red: int, green: int, blue: int) -> bool
        
            Sets or adds a vertex color to the color List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex color to set. 
                    If index equals Count, then the color will be 
             appended.
        
            red: Red component of vertex color. Value must be in the 0~255 range.
            green: Green component of vertex color. Value must be in the 0~255 range.
            blue: Blue component of vertex color. Value must be in the 0~255 range.
            Returns: true on success, false on failure.
        """
        pass

    def SetColors(self, colors):
        """
        SetColors(self: MeshVertexColorList, colors: Array[Color]) -> bool
        
            Sets all the vertex colors in one go. For the Mesh to be valid, the number 
                    of 
             colors must match the number of vertices.
        
        
            colors: Colors to set.
            Returns: true on success, false on failure.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Color](enumerable: IEnumerable[Color], value: Color) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh colors.

Get: Count(self: MeshVertexColorList) -> int

Set: Count(self: MeshVertexColorList) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a mapping information for the mesh associated with these vertex colors.

Get: Tag(self: MeshVertexColorList) -> MappingTag

Set: Tag(self: MeshVertexColorList) = value
"""



class MeshVertexList(object, IEnumerable[Point3f], IEnumerable, IRhinoTable[Point3f]):
    """ Provides access to the vertices and vertex-related functionality of a mesh. """
    def Add(self, *__args):
        """
        Add(self: MeshVertexList, vertex: Point3f) -> int
        
            Adds a new vertex to the end of the Vertex list.
        
            vertex: Location of new vertex.
            Returns: The index of the newly added vertex.
        Add(self: MeshVertexList, vertex: Point3d) -> int
        
            Adds a new vertex to the end of the Vertex list.
        
            vertex: Location of new vertex.
            Returns: The index of the newly added vertex.
        Add(self: MeshVertexList, x: Single, y: Single, z: Single) -> int
        
            Adds a new vertex to the end of the Vertex list.
        
            x: X component of new vertex coordinate.
            y: Y component of new vertex coordinate.
            z: Z component of new vertex coordinate.
            Returns: The index of the newly added vertex.
        Add(self: MeshVertexList, x: float, y: float, z: float) -> int
        
            Adds a new vertex to the end of the Vertex list.
        
            x: X component of new vertex coordinate.
            y: Y component of new vertex coordinate.
            z: Z component of new vertex coordinate.
            Returns: The index of the newly added vertex.
        """
        pass

    def AddVertices(self, vertices):
        """ AddVertices(self: MeshVertexList, vertices: IEnumerable[Point3f])AddVertices(self: MeshVertexList, vertices: IEnumerable[Point3d]) """
        pass

    def Clear(self):
        """
        Clear(self: MeshVertexList)
            Clear the Vertex list on the mesh.
        """
        pass

    def CombineIdentical(self, ignoreNormals, ignoreAdditional):
        """
        CombineIdentical(self: MeshVertexList, ignoreNormals: bool, ignoreAdditional: bool) -> bool
        
            Merges identical vertices.
        
            ignoreNormals: If true, vertex normals will not be taken into consideration when comparing vertices.
            ignoreAdditional: If true, texture coordinates, colors, and principal curvatures 
                    will not be taken 
             into consideration when comparing vertices.
        
            Returns: true if the mesh is changed, in which case the mesh will have fewer vertices than before.
        """
        pass

    def CullUnused(self):
        """
        CullUnused(self: MeshVertexList) -> int
        
            Removes all vertices that are currently not used by the Face list.
            Returns: The number of unused vertices that were removed.
        """
        pass

    def GetConnectedVertices(self, vertexIndex):
        """
        GetConnectedVertices(self: MeshVertexList, vertexIndex: int) -> Array[int]
        
            Gets indices of all vertices that form "edges" with a given vertex index.
        
            vertexIndex: The index of a vertex to query.
            Returns: An array of vertex indices that are connected with the specified vertex.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshVertexList) -> IEnumerator[Point3f]
        
            Gets an enumerator that yields all mesh vertices (points) in this collection.
            Returns: The enumerator.
        """
        pass

    def GetTopologicalIndenticalVertices(self, vertexIndex):
        """
        GetTopologicalIndenticalVertices(self: MeshVertexList, vertexIndex: int) -> Array[int]
        
            Gets a list of other vertices which are "topologically" identical
                    to this vertex.
        
            vertexIndex: A vertex index in the mesh.
            Returns: Array of indices of vertices that are topoligically the same as this vertex. The
                    
             array includes vertexIndex. Returns null on failure.
        """
        pass

    def GetVertexFaces(self, vertexIndex):
        """
        GetVertexFaces(self: MeshVertexList, vertexIndex: int) -> Array[int]
        
            Gets a list of all of the faces that share a given vertex.
        
            vertexIndex: The index of a vertex in the mesh.
            Returns: An array of indices of faces on success, null on failure.
        """
        pass

    def Hide(self, vertexIndex):
        """
        Hide(self: MeshVertexList, vertexIndex: int)
            Hides the vertex at the given index.
        
            vertexIndex: Index of vertex to hide.
        """
        pass

    def HideAll(self):
        """
        HideAll(self: MeshVertexList)
            Hides all vertices in the mesh.
        """
        pass

    def IsHidden(self, vertexIndex):
        """
        IsHidden(self: MeshVertexList, vertexIndex: int) -> bool
        
            Gets a value indicating whether or not a vertex is hidden.
        
            vertexIndex: Index of vertex to query.
            Returns: true if the vertex is hidden, false if it is not.
        """
        pass

    def Remove(self, *__args):
        """
        Remove(self: MeshVertexList, indices: IEnumerable[int], shrinkFaces: bool) -> bool
        Remove(self: MeshVertexList, index: int, shrinkFaces: bool) -> bool
        
            Removes the vertex at the given index and all faces that reference that index.
        
            index: Index of vertex to remove.
            shrinkFaces: If true, quads that reference the deleted vertex will be converted to triangles.
            Returns: true on success, false on failure.
        """
        pass

    def SetVertex(self, index, *__args):
        """
        SetVertex(self: MeshVertexList, index: int, vertex: Point3f) -> bool
        
            Sets or adds a vertex to the Vertex List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex to set.
            vertex: Vertex location.
            Returns: true on success, false on failure.
        SetVertex(self: MeshVertexList, index: int, vertex: Point3d) -> bool
        
            Sets or adds a vertex to the Vertex List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex to set.
            vertex: Vertex location.
            Returns: true on success, false on failure.
        SetVertex(self: MeshVertexList, index: int, x: Single, y: Single, z: Single) -> bool
        
            Sets or adds a vertex to the Vertex List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex to set.
            x: X component of vertex location.
            y: Y component of vertex location.
            z: Z component of vertex location.
            Returns: true on success, false on failure.
        SetVertex(self: MeshVertexList, index: int, x: float, y: float, z: float) -> bool
        
            Sets or adds a vertex to the Vertex List.
                    If [index] is less than [Count], the 
             existing vertex at [index] will be modified.If [index] equals [Count], a new vertex is appended 
             to the end of the vertex list.If [index] is larger than [Count], the function will return false.
        
        
            index: Index of vertex to set.
            x: X component of vertex location.
            y: Y component of vertex location.
            z: Z component of vertex location.
            Returns: true on success, false on failure.
        """
        pass

    def Show(self, vertexIndex):
        """
        Show(self: MeshVertexList, vertexIndex: int)
            Shows the vertex at the given index.
        
            vertexIndex: Index of vertex to show.
        """
        pass

    def ShowAll(self):
        """
        ShowAll(self: MeshVertexList)
            Shows all vertices in the mesh.
        """
        pass

    def ToFloatArray(self):
        """
        ToFloatArray(self: MeshVertexList) -> Array[Single]
        
            Copies all vertices to a linear array of float in x,y,z order
            Returns: The float array.
        """
        pass

    def ToPoint3dArray(self):
        """
        ToPoint3dArray(self: MeshVertexList) -> Array[Point3d]
        
            Copies all vertices to a new array of Rhino.Geometry.Point3d.
            Returns: A new array.
        """
        pass

    def ToPoint3fArray(self):
        """
        ToPoint3fArray(self: MeshVertexList) -> Array[Point3f]
        
            Copies all vertices to a new array of Rhino.Geometry.Point3f.
            Returns: A new array.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point3f](enumerable: IEnumerable[Point3f], value: Point3f) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh vertices.

Get: Count(self: MeshVertexList) -> int

Set: Count(self: MeshVertexList) = value
"""



class MeshVertexNormalList(object, IEnumerable[Vector3f], IEnumerable, IRhinoTable[Vector3f]):
    """ Provides access to the Vertex Normals of a Mesh. """
    def Add(self, *__args):
        """
        Add(self: MeshVertexNormalList, normal: Vector3f) -> int
        
            Adds a new vertex normal at the end of the list.
        
            normal: new vertex normal.
            Returns: The index of the newly added vertex normal.
        Add(self: MeshVertexNormalList, normal: Vector3d) -> int
        
            Adds a new vertex normal at the end of the list.
        
            normal: new vertex normal.
            Returns: The index of the newly added vertex normal.
        Add(self: MeshVertexNormalList, x: Single, y: Single, z: Single) -> int
        
            Adds a new vertex normal at the end of the list.
        
            x: X component of new vertex normal.
            y: Y component of new vertex normal.
            z: Z component of new vertex normal.
            Returns: The index of the newly added vertex normal.
        Add(self: MeshVertexNormalList, x: float, y: float, z: float) -> int
        
            Adds a new vertex normal at the end of the list.
        
            x: X component of new vertex normal.
            y: Y component of new vertex normal.
            z: Z component of new vertex normal.
            Returns: The index of the newly added vertex normal.
        """
        pass

    def AddRange(self, normals):
        """
        AddRange(self: MeshVertexNormalList, normals: Array[Vector3f]) -> bool
        
            Appends a collection of normal vectors.
        
            normals: Normals to append.
            Returns: true on success, false on failure.
        """
        pass

    def Clear(self):
        """
        Clear(self: MeshVertexNormalList)
            Clears the vertex normal collection on the mesh.
        """
        pass

    def ComputeNormals(self):
        """
        ComputeNormals(self: MeshVertexNormalList) -> bool
        
            Computes the vertex normals based on the physical shape of the mesh.
            Returns: true on success, false on failure.
        """
        pass

    def Flip(self):
        """
        Flip(self: MeshVertexNormalList)
            Reverses direction of all vertex normals
                    This is the same as Mesh.Flip(true, false, 
             false)
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: MeshVertexNormalList) -> IEnumerator[Vector3f]
        
            Gets an enumerator that yields all normals (vectors) in this collection.
            Returns: The enumerator.
        """
        pass

    def SetNormal(self, index, *__args):
        """
        SetNormal(self: MeshVertexNormalList, index: int, normal: Vector3f) -> bool
        
            Sets or adds a vertex normal to the list.
                    If [index] is less than [Count], the 
             existing vertex normal at [index] will be modified.If [index] equals [Count], a new vertex 
             normal is appended to the end of the vertex list.If [index] is larger than [Count], the function 
             will return false.
        
        
            index: Index of vertex normal to set.
            normal: The new normal at the index.
            Returns: true on success, false on failure.
        SetNormal(self: MeshVertexNormalList, index: int, normal: Vector3d) -> bool
        
            Sets or adds a vertex normal to the list.
                    If [index] is less than [Count], the 
             existing vertex normal at [index] will be modified.If [index] equals [Count], a new vertex 
             normal is appended to the end of the list.If [index] is larger than [Count], the function will 
             return false.
        
        
            index: Index of vertex normal to set.
            normal: The new normal at the index.
            Returns: true on success, false on failure.
        SetNormal(self: MeshVertexNormalList, index: int, x: Single, y: Single, z: Single) -> bool
        
            Sets or adds a normal to the list.
                    If [index] is less than [Count], the existing 
             vertex normal at [index] will be modified.If [index] equals [Count], a new vertex normal is 
             appended to the end of the list.If [index] is larger than [Count], the function will return 
             false.
        
        
            index: Index of vertex normal to set.
            x: X component of vertex normal.
            y: Y component of vertex normal.
            z: Z component of vertex normal.
            Returns: true on success, false on failure.
        SetNormal(self: MeshVertexNormalList, index: int, x: float, y: float, z: float) -> bool
        
            Sets or adds a vertex normal to the list.
                    If [index] is less than [Count], the 
             existing vertex normal at [index] will be modified.If [index] equals [Count], a new vertex 
             normal is appended to the end of the list.If [index] is larger than [Count], the function will 
             return false.
        
        
            index: Index of vertex normal to set.
            x: X component of vertex normal.
            y: Y component of vertex normal.
            z: Z component of vertex normal.
            Returns: true on success, false on failure.
        """
        pass

    def SetNormals(self, normals):
        """
        SetNormals(self: MeshVertexNormalList, normals: Array[Vector3f]) -> bool
        
            Sets all normal vectors in one go. This method destroys the current normal array if it exists.
        
            normals: Normals for the entire mesh.
            Returns: true on success, false on failure.
        """
        pass

    def UnitizeNormals(self):
        """
        UnitizeNormals(self: MeshVertexNormalList) -> bool
        
            Unitizes all vertex normals.
            Returns: true on success, false on failure.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vector3f](enumerable: IEnumerable[Vector3f], value: Vector3f) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of mesh vertex normals.

Get: Count(self: MeshVertexNormalList) -> int

Set: Count(self: MeshVertexNormalList) = value
"""



class NurbsCurveKnotList(object, IEnumerable[float], IEnumerable, IRhinoTable[float], IEpsilonComparable[NurbsCurveKnotList]):
    """ Provides access to the knot vector of a nurbs curve. """
    def ClampEnd(self, end):
        """
        ClampEnd(self: NurbsCurveKnotList, end: CurveEnd) -> bool
        
            Clamp end knots. Does not modify control point locations.
        
            end: Curve end to clamp.
            Returns: true on success, false on failure.
        """
        pass

    def CreatePeriodicKnots(self, knotSpacing):
        """
        CreatePeriodicKnots(self: NurbsCurveKnotList, knotSpacing: float) -> bool
        
            Compute a clamped, uniform, periodic knot vector based on the current
                    degree and 
             control point count. Does not change values of control
                    vertices.
        
        
            knotSpacing: Spacing of subsequent knots.
            Returns: true on success, false on failure.
        """
        pass

    def CreateUniformKnots(self, knotSpacing):
        """
        CreateUniformKnots(self: NurbsCurveKnotList, knotSpacing: float) -> bool
        
            Compute a clamped, uniform knot vector based on the current
                    degree and control 
             point count. Does not change values of control
                    vertices.
        
        
            knotSpacing: Spacing of subsequent knots.
            Returns: true on success, false on failure.
        """
        pass

    def EnsurePrivateCopy(self):
        """
        EnsurePrivateCopy(self: NurbsCurveKnotList)
            If you want to keep a copy of this class around by holding onto it in a variable after a command
             
                    completes, call EnsurePrivateCopy to make sure that this class is not tied to the 
             document. You can
                    call this function as many times as you want.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsCurveKnotList, other: NurbsCurveKnotList, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def InsertKnot(self, value, multiplicity=None):
        """
        InsertKnot(self: NurbsCurveKnotList, value: float, multiplicity: int) -> bool
        
            Inserts a knot and update control point locations.
                    Does not change parameterization 
             or locus of curve.
        
        
            value: Knot value to insert.
            multiplicity: Multiplicity of knot to insert.
            Returns: true on success, false on failure.
        InsertKnot(self: NurbsCurveKnotList, value: float) -> bool
        
            Inserts a knot and update control point locations.
                    Does not change parameterization 
             or locus of curve.
        
        
            value: Knot value to insert.
            Returns: true on success, false on failure.
        """
        pass

    def KnotMultiplicity(self, index):
        """
        KnotMultiplicity(self: NurbsCurveKnotList, index: int) -> int
        
            Get knot multiplicity.
        
            index: Index of knot to query.
            Returns: The multiplicity (valence) of the knot.
        """
        pass

    def SuperfluousKnot(self, start):
        """
        SuperfluousKnot(self: NurbsCurveKnotList, start: bool) -> float
        
            Computes the knots that are superfluous because they are not used in NURBs evaluation.
                 
                These make it appear so that the first and last curve spans are different from interior 
             spans.
                    http://wiki.mcneel.com/developer/onsuperfluousknot
        
        
            start: true if the query targets the first knot. Otherwise, the last knot.
            Returns: A component.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[float](enumerable: IEnumerable[float], value: float) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total number of knots in this curve.

Get: Count(self: NurbsCurveKnotList) -> int

"""

    IsClampedEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the knot vector is clamped at the end of the curve. 
            Clamped curves are coincident with the first and last control-point. This requires fully multiple knots.

Get: IsClampedEnd(self: NurbsCurveKnotList) -> bool

"""

    IsClampedStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether or not the knot vector is clamped at the start of the curve. 
            Clamped curves start at the first control-point. This requires fully multiple knots.

Get: IsClampedStart(self: NurbsCurveKnotList) -> bool

"""



class NurbsCurvePointList(object, IEnumerable[ControlPoint], IEnumerable, IRhinoTable[ControlPoint], IEpsilonComparable[NurbsCurvePointList]):
    """ Provides access to the control points of a nurbs curve. """
    def ChangeEndWeights(self, w0, w1):
        """
        ChangeEndWeights(self: NurbsCurvePointList, w0: float, w1: float) -> bool
        
            Use a combination of scaling and reparameterization to change the end weights to the specified 
             values.
        
        
            w0: Weight for first control point.
            w1: Weight for last control point.
            Returns: true on success, false on failure.
        """
        pass

    def ControlPolygon(self):
        """
        ControlPolygon(self: NurbsCurvePointList) -> Polyline
        
            Constructs a polyline through all the control points. 
                    Note that periodic curves 
             generate a closed polyline with fewer 
                    points than control-points.
        
            Returns: A polyline connecting all control points.
        """
        pass

    def EnsurePrivateCopy(self):
        """
        EnsurePrivateCopy(self: NurbsCurvePointList)
            If you want to keep a copy of this class around by holding onto it in a variable after a command
             
                    completes, call EnsurePrivateCopy to make sure that this class is not tied to the 
             document. You can
                    call this function as many times as you want.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsCurvePointList, other: NurbsCurvePointList, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def MakeNonRational(self):
        """
        MakeNonRational(self: NurbsCurvePointList) -> bool
        
            Sets all the control points to 1.0.
            Returns: true on success, false on failure.
        """
        pass

    def MakeRational(self):
        """
        MakeRational(self: NurbsCurvePointList) -> bool
        
            Turns the curve into a Rational nurbs curve.
            Returns: true on success, false on failure.
        """
        pass

    def SetPoint(self, index, *__args):
        """
        SetPoint(self: NurbsCurvePointList, index: int, point: Point4d) -> bool
        
            Sets a specific weighted control-point.
        
            index: Index of control-point to set.
            point: Coordinate and weight of control-point.
        SetPoint(self: NurbsCurvePointList, index: int, point: Point3d) -> bool
        
            Sets a specific control-point.
        
            index: Index of control-point to set.
            point: Coordinate of control-point.
        SetPoint(self: NurbsCurvePointList, index: int, x: float, y: float, z: float, weight: float) -> bool
        
            Sets a specific control-point.
        
            index: Index of control-point to set.
            x: X coordinate of control-point.
            y: Y coordinate of control-point.
            z: Z coordinate of control-point.
            weight: Weight of control-point.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ControlPoint](enumerable: IEnumerable[ControlPoint], value: ControlPoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ControlPolygonLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the polyline connecting all control points.

Get: ControlPolygonLength(self: NurbsCurvePointList) -> float

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of control points in this curve.

Get: Count(self: NurbsCurvePointList) -> int

"""



class NurbsSurfaceKnotList(object, IEnumerable[float], IEnumerable, IRhinoTable[float], IEpsilonComparable[NurbsSurfaceKnotList]):
    """ Provides access to the knot vector of a nurbs surface. """
    def CreatePeriodicKnots(self, knotSpacing):
        """
        CreatePeriodicKnots(self: NurbsSurfaceKnotList, knotSpacing: float) -> bool
        
            Compute a clamped, uniform, periodic knot vector based on the current
                    degree and 
             control point count. Does not change values of control
                    vertices.
        
        
            knotSpacing: Spacing of subsequent knots.
            Returns: true on success, false on failure.
        """
        pass

    def CreateUniformKnots(self, knotSpacing):
        """
        CreateUniformKnots(self: NurbsSurfaceKnotList, knotSpacing: float) -> bool
        
            Compute a clamped, uniform knot vector based on the current
                    degree and control 
             point count. Does not change values of control
                    vertices.
        
        
            knotSpacing: Spacing of subsequent knots.
            Returns: true on success, false on failure.
        """
        pass

    def EnsurePrivateCopy(self):
        """
        EnsurePrivateCopy(self: NurbsSurfaceKnotList)
            If you want to keep a copy of this class around by holding onto it in a variable after a command
             
                    completes, call EnsurePrivateCopy to make sure that this class is not tied to the 
             document. You can
                    call this function as many times as you want.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsSurfaceKnotList, other: NurbsSurfaceKnotList, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def InsertKnot(self, value, multiplicity=None):
        """
        InsertKnot(self: NurbsSurfaceKnotList, value: float, multiplicity: int) -> bool
        
            Inserts a knot and update control point locations.
                    Does not change parameterization 
             or locus of curve.
        
        
            value: Knot value to insert.
            multiplicity: Multiplicity of knot to insert.
            Returns: true on success, false on failure.
        InsertKnot(self: NurbsSurfaceKnotList, value: float) -> bool
        
            Inserts a knot and update control point locations.
                    Does not change parameterization 
             or locus of curve.
        
        
            value: Knot value to insert.
            Returns: true on success, false on failure.
        """
        pass

    def KnotMultiplicity(self, index):
        """
        KnotMultiplicity(self: NurbsSurfaceKnotList, index: int) -> int
        
            Get knot multiplicity.
        
            index: Index of knot to query.
            Returns: The multiplicity (valence) of the knot.
        """
        pass

    def SuperfluousKnot(self, start):
        """
        SuperfluousKnot(self: NurbsSurfaceKnotList, start: bool) -> float
        
            Computes the knots that are superfluous because they are not used in NURBs evaluation.
                 
                These make it appear so that the first and last surface spans are different from interior 
             spans.
                    http://wiki.mcneel.com/developer/onsuperfluousknot
        
        
            start: true if the query targets the first knot. Otherwise, the last knot.
            Returns: A component.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[float](enumerable: IEnumerable[float], value: float) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ClampedAtEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if a knot vector is clamped.

Get: ClampedAtEnd(self: NurbsSurfaceKnotList) -> bool

"""

    ClampedAtStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if a knot vector is clamped.

Get: ClampedAtStart(self: NurbsSurfaceKnotList) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total number of knots in this curve.

Get: Count(self: NurbsSurfaceKnotList) -> int

"""



class NurbsSurfacePointList(object, IEnumerable[ControlPoint], IEnumerable, IEpsilonComparable[NurbsSurfacePointList]):
    """ Provides access to the control points of a nurbs surface. """
    def EnsurePrivateCopy(self):
        """
        EnsurePrivateCopy(self: NurbsSurfacePointList)
            If you want to keep a copy of this class around by holding onto it in a variable after a command
             
                    completes, call EnsurePrivateCopy to make sure that this class is not tied to the 
             document. You can
                    call this function as many times as you want.
        """
        pass

    def EpsilonEquals(self, other, epsilon):
        """
        EpsilonEquals(self: NurbsSurfacePointList, other: NurbsSurfacePointList, epsilon: float) -> bool
        
            Check that all values in other are within epsilon of the values in this
        """
        pass

    def GetControlPoint(self, u, v):
        """
        GetControlPoint(self: NurbsSurfacePointList, u: int, v: int) -> ControlPoint
        
            Gets the control point at the given (u, v) index.
        
            u: Index of control-point along surface U direction.
            v: Index of control-point along surface V direction.
            Returns: The control point at the given (u, v) index.
        """
        pass

    def GetGrevillePoint(self, u, v):
        """
        GetGrevillePoint(self: NurbsSurfacePointList, u: int, v: int) -> Point2d
        
            Gets the Greville point (u, v) coordinates associated with the control point at the given 
             indices.
        
        
            u: Index of control-point along surface U direction.
            v: Index of control-point along surface V direction.
            Returns: A Surface UV coordinate on success, Point2d.Unset on failure.
        """
        pass

    def SetControlPoint(self, u, v, cp):
        """
        SetControlPoint(self: NurbsSurfacePointList, u: int, v: int, cp: ControlPoint) -> bool
        
            Sets the control point at the given (u, v) index.
        
            u: Index of control-point along surface U direction.
            v: Index of control-point along surface V direction.
            cp: The control point to set.
            Returns: true on success, false on failure.
        SetControlPoint(self: NurbsSurfacePointList, u: int, v: int, cp: Point3d) -> bool
        
            Sets the control point at the given (u, v) index.
        
            u: Index of control-point along surface U direction.
            v: Index of control-point along surface V direction.
            cp: The control point location to set (weight is assumed to be 1.0).
            Returns: true on success, false on failure.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ControlPoint](enumerable: IEnumerable[ControlPoint], value: ControlPoint) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CountU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of control points in the U direction of this surface.

Get: CountU(self: NurbsSurfacePointList) -> int

"""

    CountV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of control points in the V direction of this surface.

Get: CountV(self: NurbsSurfacePointList) -> int

"""



