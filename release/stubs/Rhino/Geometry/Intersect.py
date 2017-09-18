# encoding: utf-8
# module Rhino.Geometry.Intersect calls itself Intersect
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class CurveIntersections(object, IDisposable, IList[IntersectionEvent], ICollection[IntersectionEvent], IEnumerable[IntersectionEvent], IEnumerable):
    """ Maintains an ordered list of Curve Intersection results. """
    def CopyTo(self, array, arrayIndex):
        """
        CopyTo(self: CurveIntersections, array: Array[IntersectionEvent], arrayIndex: int)
            Copies all intersection results into another array, departing at an index in the target array.
        
            array: The target array. This value cannot be null.
            arrayIndex: Zero-based index in which to start the copy.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: CurveIntersections)
            Actively reclaims unmanaged resources that this instance uses.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: CurveIntersections) -> IEnumerator[IntersectionEvent]
        
            Returns an enumerator that is capable of yielding all IntersectionEvents in the collection.
            Returns: The constructed enumerator.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[IntersectionEvent], item: IntersectionEvent) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
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

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of recorded intersection events.

Get: Count(self: CurveIntersections) -> int

"""



class Intersection(object):
    """ Provides static methods for the computation of intersections, projections, sections and similar. """
    @staticmethod
    def BrepBrep(brepA, brepB, tolerance, intersectionCurves, intersectionPoints):
        """
        BrepBrep(brepA: Brep, brepB: Brep, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects two Breps.
        
            brepA: First Brep for intersection.
            brepB: Second Brep for intersection.
            tolerance: Intersection tolerance.
            Returns: true on success; false on failure.
        """
        pass

    @staticmethod
    def BrepPlane(brep, plane, tolerance, intersectionCurves, intersectionPoints):
        """
        BrepPlane(brep: Brep, plane: Plane, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects a Brep with an (infinite) plane.
        
            brep: Brep to intersect.
            plane: Plane to intersect with.
            tolerance: Tolerance to use for intersections.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def BrepSurface(brep, surface, tolerance, intersectionCurves, intersectionPoints):
        """
        BrepSurface(brep: Brep, surface: Surface, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects a Brep and a Surface.
        
            brep: A brep to be intersected.
            surface: A surface to be intersected.
            tolerance: A tolerance value.
            Returns: true on success; false on failure.
        """
        pass

    @staticmethod
    def CurveBrep(curve, brep, tolerance, overlapCurves, intersectionPoints):
        """
        CurveBrep(curve: Curve, brep: Brep, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects a curve with a Brep. This function returns the 3D points of intersection
                    
             and 3D overlap curves. If an error occurs while processing overlap curves, this function 
              
                   will return false, but it will still provide partial results.
        
        
            curve: Curve for intersection.
            brep: Brep for intersection.
            tolerance: Fitting and near miss tolerance.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def CurveBrepFace(curve, face, tolerance, overlapCurves, intersectionPoints):
        """
        CurveBrepFace(curve: Curve, face: BrepFace, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects a curve with a Brep face.
        
            curve: A curve.
            face: A brep face.
            tolerance: Fitting and near miss tolerance.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def CurveCurve(curveA, curveB, tolerance, overlapTolerance):
        """
        CurveCurve(curveA: Curve, curveB: Curve, tolerance: float, overlapTolerance: float) -> CurveIntersections
        
            Finds the intersections between two curves.
        
            curveA: First curve for intersection.
            curveB: Second curve for intersection.
            tolerance: Intersection tolerance. If the curves approach each other to within tolerance, 
                    an 
             intersection is assumed.
        
            overlapTolerance: The tolerance with which the curves are tested.
            Returns: A collection of intersection events.
        """
        pass

    @staticmethod
    def CurvePlane(curve, plane, tolerance):
        """
        CurvePlane(curve: Curve, plane: Plane, tolerance: float) -> CurveIntersections
        
            Intersects a curve with an (infinite) plane.
        
            curve: Curve to intersect.
            plane: Plane to intersect with.
            tolerance: Tolerance to use during intersection.
            Returns: A list of intersection events or null if no intersections were recorded.
        """
        pass

    @staticmethod
    def CurveSelf(curve, tolerance):
        """
        CurveSelf(curve: Curve, tolerance: float) -> CurveIntersections
        
            Finds the places where a curve intersects itself.
        
            curve: Curve for self-intersections.
            tolerance: Intersection tolerance. If the curve approaches itself to within tolerance, 
                    an 
             intersection is assumed.
        
            Returns: A collection of intersection events.
        """
        pass

    @staticmethod
    def CurveSurface(curve, *__args):
        """
        CurveSurface(curve: Curve, curveDomain: Interval, surface: Surface, tolerance: float, overlapTolerance: float) -> CurveIntersections
        
            Intersects a (sub)curve and a surface.
        
            curve: Curve for intersection.
            curveDomain: Domain of surbcurve to take into consideration for Intersections.
            surface: Surface for intersection.
            tolerance: Intersection tolerance. If the curve approaches the surface to within tolerance, 
                    
             an intersection is assumed.
        
            overlapTolerance: The tolerance with which the curves are tested.
            Returns: A collection of intersection events.
        CurveSurface(curve: Curve, surface: Surface, tolerance: float, overlapTolerance: float) -> CurveIntersections
        
            Intersects a curve and a surface.
        
            curve: Curve for intersection.
            surface: Surface for intersection.
            tolerance: Intersection tolerance. If the curve approaches the surface to within tolerance, 
                    
             an intersection is assumed.
        
            overlapTolerance: The tolerance with which the curves are tested.
            Returns: A collection of intersection events.
        """
        pass

    @staticmethod
    def LineBox(line, box, tolerance, lineParameters):
        """
        LineBox(line: Line, box: Box, tolerance: float) -> (bool, Interval)
        
            Intersects an infinite line with a box volume.
        
            line: Line for intersection.
            box: Box to intersect.
            tolerance: If tolerance > 0.0, then the intersection is performed against a box 
                    that has each 
             side moved out by tolerance.
        
            Returns: true if the line intersects the box, false if no intersection occurs.
        LineBox(line: Line, box: BoundingBox, tolerance: float) -> (bool, Interval)
        
            Intersects an infinite line and an axis aligned bounding box.
        
            line: Line for intersection.
            box: BoundingBox to intersect.
            tolerance: If tolerance > 0.0, then the intersection is performed against a box 
                    that has each 
             side moved out by tolerance.
        
            Returns: true if the line intersects the box, false if no intersection occurs.
        """
        pass

    @staticmethod
    def LineCircle(line, circle, t1, point1, t2, point2):
        """
        LineCircle(line: Line, circle: Circle) -> (LineCircleIntersection, float, Point3d, float, Point3d)
        
            Intersects a line with a circle using exact calculations.
        
            line: Line for intersection.
            circle: Circle for intersection.
            Returns: If Rhino.Geometry.Intersect.LineCircleIntersection.Single is returned, only t1 and point1 will 
             have valid values. 
                    If Rhino.Geometry.Intersect.LineCircleIntersection.Multiple is 
             returned, t2 and point2 will also be filled out.
        """
        pass

    @staticmethod
    def LineCylinder(line, cylinder, intersectionPoint1, intersectionPoint2):
        """
        LineCylinder(line: Line, cylinder: Cylinder) -> (LineCylinderIntersection, Point3d, Point3d)
        
            Intersects a line with a cylinder using exact calculations.
        
            line: Line for intersection.
            cylinder: Cylinder for intersection.
            Returns: If None is returned, the first point is the point on the line closest
                    to the 
             cylinder and the second point is the point on the cylinder closest to
                    the line. 
          
                       If Rhino.Geometry.Intersect.LineCylinderIntersection.Single is returned, the first 
             point
                    is the point on the line and the second point is the  same point on the
             
                    cylinder.
        """
        pass

    @staticmethod
    def LineLine(lineA, lineB, a, b, tolerance=None, finiteSegments=None):
        """
        LineLine(lineA: Line, lineB: Line) -> (bool, float, float)
        
            Finds the closest point between two infinite lines.
        
            lineA: First line.
            lineB: Second line.
            Returns: true if points are found and false if the lines are numerically parallel. 
                    
             Numerically parallel means the 2x2 matrix:
                    +AoA  -AoB-AoB  +BoB
                    is 
             numerically singular, where A = (lineA.To - lineA.From) and B = (lineB.To-lineB.From)
        
        LineLine(lineA: Line, lineB: Line, tolerance: float, finiteSegments: bool) -> (bool, float, float)
        
            Intersects two lines.
        
            lineA: First line for intersection.
            lineB: Second line for intersection.
            tolerance: If tolerance > 0.0, then an intersection is reported only if the distance between the points is 
             <= tolerance. 
                    If tolerance <= 0.0, then the closest point between the lines is 
             reported.
        
            finiteSegments: If true, the input lines are treated as finite segments. 
                    If false, the input lines 
             are treated as infinite lines.
        
            Returns: true if a closest point can be calculated and the result passes the tolerance parameter test; 
             otherwise false.
        """
        pass

    @staticmethod
    def LinePlane(line, plane, lineParameter):
        """
        LinePlane(line: Line, plane: Plane) -> (bool, float)
        
            Intersects a line and a plane. This function only returns true if the 
                    intersection 
             result is a single point (i.e. if the line is coincident with 
                    the plane then no 
             intersection is assumed).
        
        
            line: Line for intersection.
            plane: Plane to intersect.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def LineSphere(line, sphere, intersectionPoint1, intersectionPoint2):
        """
        LineSphere(line: Line, sphere: Sphere) -> (LineSphereIntersection, Point3d, Point3d)
        
            Intersects a line with a sphere using exact calculations.
        
            line: Line for intersection.
            sphere: Sphere for intersection.
            Returns: If Rhino.Geometry.Intersect.LineSphereIntersection.None is returned, the first point is the 
             point on the line closest to the sphere and 
                    the second point is the point on the 
             sphere closest to the line. 
                    If 
             Rhino.Geometry.Intersect.LineSphereIntersection.Single is returned, the first point is the point 
             on the line and the second point is the 
                    same point on the sphere.
        """
        pass

    @staticmethod
    def MeshLine(mesh, line, faceIds):
        """
        MeshLine(mesh: Mesh, line: Line) -> (Array[Point3d], Array[int])
        
            Finds the intersection of a mesh and a line
        
            mesh: A mesh to intersect
            line: The line to intersect with the mesh
            Returns: An array of points: one for each face that was passed by the faceIds out reference.
        """
        pass

    @staticmethod
    def MeshMeshAccurate(meshA, meshB, tolerance):
        """
        MeshMeshAccurate(meshA: Mesh, meshB: Mesh, tolerance: float) -> Array[Polyline]
        
            Intersects two meshes. Overlaps and near misses are handled.
        
            meshA: First mesh for intersection.
            meshB: Second mesh for intersection.
            tolerance: Intersection tolerance.
            Returns: An array of intersection polylines.
        """
        pass

    @staticmethod
    def MeshMeshFast(meshA, meshB):
        """
        MeshMeshFast(meshA: Mesh, meshB: Mesh) -> Array[Line]
        
            Quickly intersects two meshes. Overlaps and near misses are ignored.
        
            meshA: First mesh for intersection.
            meshB: Second mesh for intersection.
            Returns: An array of intersection line segments.
        """
        pass

    @staticmethod
    def MeshPlane(mesh, *__args):
        """
        MeshPlane(mesh: Mesh, planes: IEnumerable[Plane]) -> Array[Polyline]
        MeshPlane(mesh: Mesh, plane: Plane) -> Array[Polyline]
        
            Intersects a mesh with an (infinite) plane.
        
            mesh: Mesh to intersect.
            plane: Plane to intersect with.
            Returns: An array of polylines describing the intersection loops or null (Nothing in Visual Basic) if no 
             intersections could be found.
        """
        pass

    @staticmethod
    def MeshPolyline(mesh, curve, faceIds):
        """
        MeshPolyline(mesh: Mesh, curve: PolylineCurve) -> (Array[Point3d], Array[int])
        
            Finds the intersection of a mesh and a polyline.
        
            mesh: A mesh to intersect.
            curve: A polyline curves to intersect.
            Returns: An array of points: one for each face that was passed by the faceIds out reference.
        """
        pass

    @staticmethod
    def MeshRay(mesh, ray, meshFaceIndices=None):
        """
        MeshRay(mesh: Mesh, ray: Ray3d) -> (float, Array[int])
        
            Finds the first intersection of a ray with a mesh.
        
            mesh: A mesh to intersect.
            ray: A ray to be casted.
            Returns: >= 0.0 parameter along ray if successful.
                    < 0.0 if no intersection found.
        MeshRay(mesh: Mesh, ray: Ray3d) -> float
        
            Finds the first intersection of a ray with a mesh.
        
            mesh: A mesh to intersect.
            ray: A ray to be casted.
            Returns: >= 0.0 parameter along ray if successful.
                    < 0.0 if no intersection found.
        """
        pass

    @staticmethod
    def PlaneCircle(plane, circle, firstCircleParameter, secondCircleParameter):
        """
        PlaneCircle(plane: Plane, circle: Circle) -> (PlaneCircleIntersection, float, float)
        
            Intersects a plane with a circle using exact calculations.
        
            plane: Plane to intersect.
            circle: Circe to intersect.
            Returns: The type of intersection that occured.
        """
        pass

    @staticmethod
    def PlanePlane(planeA, planeB, intersectionLine):
        """
        PlanePlane(planeA: Plane, planeB: Plane) -> (bool, Line)
        
            Intersects two planes and return the intersection line. If the planes are 
                    parallel 
             or coincident, no intersection is assumed.
        
        
            planeA: First plane for intersection.
            planeB: Second plane for intersection.
            Returns: true on success, false on failure.
        """
        pass

    @staticmethod
    def PlanePlanePlane(planeA, planeB, planeC, intersectionPoint):
        """
        PlanePlanePlane(planeA: Plane, planeB: Plane, planeC: Plane) -> (bool, Point3d)
        
            Intersects three planes to find the single point they all share.
        
            planeA: First plane for intersection.
            planeB: Second plane for intersection.
            planeC: Third plane for intersection.
            Returns: true on success, false on failure. If at least two out of the three planes 
                    are 
             parallel or coincident, failure is assumed.
        """
        pass

    @staticmethod
    def PlaneSphere(plane, sphere, intersectionCircle):
        """
        PlaneSphere(plane: Plane, sphere: Sphere) -> (PlaneSphereIntersection, Circle)
        
            Intersects a plane with a sphere using exact calculations.
        
            plane: Plane to intersect.
            sphere: Sphere to intersect.
            Returns: If Rhino.Geometry.Intersect.PlaneSphereIntersection.None is returned, the intersectionCircle has 
             a radius of zero and the center point 
                    is the point on the plane closest to the 
             sphere.
        """
        pass

    @staticmethod
    def ProjectPointsToBreps(breps, points, direction, tolerance):
        """ ProjectPointsToBreps(breps: IEnumerable[Brep], points: IEnumerable[Point3d], direction: Vector3d, tolerance: float) -> Array[Point3d] """
        pass

    @staticmethod
    def ProjectPointsToBrepsEx(breps, points, direction, tolerance, indices):
        """ ProjectPointsToBrepsEx(breps: IEnumerable[Brep], points: IEnumerable[Point3d], direction: Vector3d, tolerance: float) -> (Array[Point3d], Array[int]) """
        pass

    @staticmethod
    def ProjectPointsToMeshes(meshes, points, direction, tolerance):
        """ ProjectPointsToMeshes(meshes: IEnumerable[Mesh], points: IEnumerable[Point3d], direction: Vector3d, tolerance: float) -> Array[Point3d] """
        pass

    @staticmethod
    def ProjectPointsToMeshesEx(meshes, points, direction, tolerance, indices):
        """ ProjectPointsToMeshesEx(meshes: IEnumerable[Mesh], points: IEnumerable[Point3d], direction: Vector3d, tolerance: float) -> (Array[Point3d], Array[int]) """
        pass

    @staticmethod
    def RayShoot(ray, geometry, maxReflections):
        """ RayShoot(ray: Ray3d, geometry: IEnumerable[GeometryBase], maxReflections: int) -> Array[Point3d] """
        pass

    @staticmethod
    def SphereSphere(sphereA, sphereB, intersectionCircle):
        """
        SphereSphere(sphereA: Sphere, sphereB: Sphere) -> (SphereSphereIntersection, Circle)
        
            Intersects two spheres using exact calculations.
        
            sphereA: First sphere to intersect.
            sphereB: Second sphere to intersect.
            Returns: The intersection type.
        """
        pass

    @staticmethod
    def SurfaceSurface(surfaceA, surfaceB, tolerance, intersectionCurves, intersectionPoints):
        """
        SurfaceSurface(surfaceA: Surface, surfaceB: Surface, tolerance: float) -> (bool, Array[Curve], Array[Point3d])
        
            Intersects two Surfaces.
        
            surfaceA: First Surface for intersection.
            surfaceB: Second Surface for intersection.
            tolerance: Intersection tolerance.
            Returns: true on success, false on failure.
        """
        pass

    __all__ = [
        'BrepBrep',
        'BrepPlane',
        'BrepSurface',
        'CurveBrep',
        'CurveBrepFace',
        'CurveCurve',
        'CurvePlane',
        'CurveSelf',
        'CurveSurface',
        'LineBox',
        'LineCircle',
        'LineCylinder',
        'LineLine',
        'LinePlane',
        'LineSphere',
        'MeshLine',
        'MeshMeshAccurate',
        'MeshMeshFast',
        'MeshPlane',
        'MeshPolyline',
        'MeshRay',
        'PlaneCircle',
        'PlanePlane',
        'PlanePlanePlane',
        'PlaneSphere',
        'ProjectPointsToBreps',
        'ProjectPointsToBrepsEx',
        'ProjectPointsToMeshes',
        'ProjectPointsToMeshesEx',
        'RayShoot',
        'SphereSphere',
        'SurfaceSurface',
    ]


class IntersectionEvent(object):
    """
    Provides all the information for a single Curve Intersection event.
    
    IntersectionEvent()
    """
    def SurfaceOverlapParameter(self, uDomain, vDomain):
        """
        SurfaceOverlapParameter(self: IntersectionEvent) -> (Interval, Interval)
        
            If this instance records a Curve|Surface intersection event, 
                    and the intersection 
             type if overlap, then use this function 
                    to get the U and V domains on the surface 
             where the overlap occurs.
        """
        pass

    def SurfacePointParameter(self, u, v):
        """
        SurfacePointParameter(self: IntersectionEvent) -> (float, float)
        
            If this instance records a Curve|Surface intersection event, 
                    and the intersection 
             type is point, then use this function 
                    to get the U and V parameters on the surface 
             where the intersection occurs.
        """
        pass

    IsOverlap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All curve intersection events are either a single point or an overlap.

Get: IsOverlap(self: IntersectionEvent) -> bool

"""

    IsPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All curve intersection events are either a single point or an overlap.

Get: IsPoint(self: IntersectionEvent) -> bool

"""

    OverlapA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the interval on curve A where the overlap occurs. 
            If the intersection type is not overlap, this value is meaningless.

Get: OverlapA(self: IntersectionEvent) -> Interval

"""

    OverlapB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the interval on curve B where the overlap occurs. 
            If the intersection type is not overlap, this value is meaningless.

Get: OverlapB(self: IntersectionEvent) -> Interval

"""

    ParameterA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameter on Curve A where the intersection occured. 
            If the intersection type is overlap, then this will return the 
            start of the overlap region.

Get: ParameterA(self: IntersectionEvent) -> float

"""

    ParameterB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parameter on Curve A where the intersection occured. 
            If the intersection type is overlap, then this will return the 
            start of the overlap region.

Get: ParameterB(self: IntersectionEvent) -> float

"""

    PointA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point on Curve A where the intersection occured. 
            If the intersection type is overlap, then this will return the 
            start of the overlap region.

Get: PointA(self: IntersectionEvent) -> Point3d

"""

    PointA2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end point of the overlap on Curve A. 
            If the intersection type is not overlap, this value is meaningless.

Get: PointA2(self: IntersectionEvent) -> Point3d

"""

    PointB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the point on Curve B (or Surface B) where the intersection occured. 
            If the intersection type is overlap, then this will return the 
            start of the overlap region.

Get: PointB(self: IntersectionEvent) -> Point3d

"""

    PointB2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the end point of the overlap on Curve B (or Surface B). 
            If the intersection type is not overlap, this value is meaningless.

Get: PointB2(self: IntersectionEvent) -> Point3d

"""



class LineCircleIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Line|Circle intersection event.
    
    enum LineCircleIntersection, values: Multiple (2), None (0), Single (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Single = None
    value__ = None


class LineCylinderIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Line|Cylinder intersection event.
    
    enum LineCylinderIntersection, values: Multiple (2), None (0), Overlap (3), Single (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Overlap = None
    Single = None
    value__ = None


class LineSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Line|Sphere intersection event.
    
    enum LineSphereIntersection, values: Multiple (2), None (0), Single (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Multiple = None
    None = None
    Single = None
    value__ = None


class MeshClash(object):
    """ Represents a particular instance of a clash or intersection between two meshes. """
    @staticmethod
    def Search(*__args):
        """
        Search(meshA: Mesh, meshB: Mesh, distance: float, maxEventCount: int) -> Array[MeshClash]
        
            Searches the locations where the distance from the first mesh to the second mesh
                    is 
             less than the provided value.
        
        
            meshA: The first mesh.
            meshB: The second mesh.
            distance: The largest distance at which there is a clash.
                    All values smaller than this cause 
             a clash as well.
        
            maxEventCount: The maximum number of clash objects.
            Returns: An array of clash objects.
        Search(meshA: Mesh, setB: IEnumerable[Mesh], distance: float, maxEventCount: int) -> Array[MeshClash]
        Search(setA: IEnumerable[Mesh], setB: IEnumerable[Mesh], distance: float, maxEventCount: int) -> Array[MeshClash]
        """
        pass

    ClashPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If valid, then the sphere centered at ClashPoint of ClashRadius
            distance interesects the clashing meshes.

Get: ClashPoint(self: MeshClash) -> Point3d

"""

    ClashRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the clash, or intersection, radius.

Get: ClashRadius(self: MeshClash) -> float

"""

    MeshA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the first mesh.

Get: MeshA(self: MeshClash) -> Mesh

"""

    MeshB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the second mesh.

Get: MeshB(self: MeshClash) -> Mesh

"""



class PlaneCircleIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Plane|Circle intersection event.
    
    enum PlaneCircleIntersection, values: Coincident (4), None (0), Parallel (3), Secant (2), Tangent (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Coincident = None
    None = None
    Parallel = None
    Secant = None
    Tangent = None
    value__ = None


class PlaneSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Plane|Sphere intersection event.
    
    enum PlaneSphereIntersection, values: Circle (2), None (0), Point (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    None = None
    Point = None
    value__ = None


class SphereSphereIntersection(Enum, IComparable, IFormattable, IConvertible):
    """
    Represents all possible cases of a Sphere|Sphere intersection event.
    
    enum SphereSphereIntersection, values: Circle (2), None (0), Overlap (3), Point (1)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Circle = None
    None = None
    Overlap = None
    Point = None
    value__ = None


