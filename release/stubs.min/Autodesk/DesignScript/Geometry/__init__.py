# encoding: utf-8
# module Autodesk.DesignScript.Geometry calls itself Geometry
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Application(object, IExtensionApplication):
    # no doc
    def PreloadAsmLibraries(self, baseDirectory):
        """ PreloadAsmLibraries(self: Application, baseDirectory: str) """
        pass

    def ShutDown(self):
        """ ShutDown(self: Application) """
        pass

    def StartUp(self):
        """ StartUp(self: Application) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsExecuting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExecuting(self: Application) -> bool

"""


    Instance = None


class DesignScriptEntity(object, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DesignScriptEntity) -> int """
        pass

    def Tessellate(self, package, parameters):
        """ Tessellate(self: DesignScriptEntity, package: IRenderPackage, parameters: TessellationParameters) """
        pass

    def ToString(self):
        """ ToString(self: DesignScriptEntity) -> str """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    mConstructor = None
    Tags = None


class Geometry(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ClosestPointTo(self, other):
        """
        ClosestPointTo(self: Geometry, other: Geometry) -> Point
        
            Obtain the closest Point on this Geometry to the other
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    @staticmethod
    def DeserializeFromSAB(buffer):
        """
        DeserializeFromSAB(buffer: Array[Byte]) -> Array[Geometry]
        
            Deserializes the specified Standard ACIS Binary(SAB) format data and returns a list of geometry
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def DistanceTo(self, other):
        """
        DistanceTo(self: Geometry, other: Geometry) -> float
        
            Obtain the distance from this Geometry to another
            Returns: The distance
        """
        pass

    def DoesIntersect(self, other):
        """
        DoesIntersect(self: Geometry, other: Geometry) -> bool
        
            Determine if another Geometry object intersects with this one
        """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Explode(self):
        """
        Explode(self: Geometry) -> Array[Geometry]
        
            Separates compound or non-separated elements into their component
                    parts.
        """
        pass

    def ExportToSAT(self, *__args):
        """
        ExportToSAT(geometry: IEnumerable[Geometry], filePath: str) -> str
        ExportToSAT(geometry: IEnumerable[Geometry], filePath: str, unitsMM: float) -> str
        ExportToSAT(self: Geometry, filePath: str) -> str
        
            Exports the specified geometry to the given SAT file path
        
            filePath: The name of the file to export the geometry to
        ExportToSAT(self: Geometry, filePath: str, unitsMM: float) -> str
        
            Exports the specified geometry to the given SAT file path
        
            filePath: The name of the file to export the geometry to
            unitsMM: The units to use
        """
        pass

    @staticmethod
    def FromNativePointer(nativePointer):
        """ FromNativePointer(nativePointer: IntPtr) -> Array[Geometry] """
        pass

    @staticmethod
    def FromObject(ptr):
        """ FromObject(ptr: Int64) -> Geometry """
        pass

    @staticmethod
    def ImportFromSAT(*__args):
        """
        ImportFromSAT(filePath: str) -> Array[Geometry]
        
            Imports a SAT file and returns an array of imported geometries
        
            filePath: Path to the SAT file
            Returns: List of imported geometries
        ImportFromSAT(file: FileInfo) -> Array[Geometry]
        
            Imports a SAT file and returns an array of imported geometries
        
            file: File object representing the SAT file
            Returns: List of imported geometries
        """
        pass

    def Intersect(self, other):
        """
        Intersect(self: Geometry, other: Geometry) -> Array[Geometry]
        
            Get the intersection Geometry for this object and another
        """
        pass

    def IntersectAll(self, others):
        """ IntersectAll(self: Geometry, others: IEnumerable[Geometry]) -> Array[Geometry] """
        pass

    def IsAlmostEqualTo(self, other):
        """
        IsAlmostEqualTo(self: Geometry, other: Geometry) -> bool
        
            Check if the two objects have the same representational geometry or numerical values
        """
        pass

    def Mirror(self, mirrorPlane):
        """
        Mirror(self: Geometry, mirrorPlane: Plane) -> Geometry
        
            Mirror the object across the input Plane
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Geometry, basePlane: Plane, degrees: float) -> Geometry
        
            Rotates an object around the Plane origin and normal by a specified 
                    degree
        Rotate(self: Geometry, origin: Point, axis: Vector, degrees: float) -> Geometry
        
            Rotates an object around an origin and an axis by a specified 
                    degree
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: Geometry, plane: Plane, xamount: float, yamount: float, zamount: float) -> Geometry
        
            Scale non-uniformly around a given Plane
        Scale(self: Geometry, basePoint: Point, from: Point, to: Point) -> Geometry
        
            Scale uniformly around a given point, using two pick points as scalars
        Scale(self: Geometry, amount: float) -> Geometry
        
            Scale uniformly around the origin
        Scale(self: Geometry, xamount: float, yamount: float, zamount: float) -> Geometry
        
            Scale non-uniformly around the origin
        """
        pass

    def Scale1D(self, basePoint, from, to):
        """
        Scale1D(self: Geometry, basePoint: Point, from: Point, to: Point) -> Geometry
        
            Scale in one dimension by base and 2 pick points.  The scaling axis is defined by the line 
             between base and pick0.
        """
        pass

    def Scale2D(self, basePlane, from, to):
        """
        Scale2D(self: Geometry, basePlane: Plane, from: Point, to: Point) -> Geometry
        
            Scale in two dimension by base and 2 pick points  The two pick points are projected onto the 
             base plane in order to determine the 2d scale factors
        """
        pass

    def SerializeAsSAB(self, geometry=None):
        """
        SerializeAsSAB(geometry: IEnumerable[Geometry]) -> Array[Byte]
        SerializeAsSAB(self: Geometry) -> Array[Byte]
        
            Serializes the specified geometry into Standard ACIS Binary(SAB) format and returns serialized 
             binary stream data
        """
        pass

    def Split(self, other):
        """
        Split(self: Geometry, other: Geometry) -> Array[Geometry]
        
            Split this Geometry using another Geometry as a cutting "tool"
        """
        pass

    @staticmethod
    def ToNativePointer(geometry):
        """ ToNativePointer(geometry: IEnumerable[Geometry]) -> Array[IntPtr] """
        pass

    def Transform(self, *__args):
        """
        Transform(self: Geometry, fromCoordinateSystem: CoordinateSystem, contextCoordinateSystem: CoordinateSystem) -> Geometry
        
            Transforms this geometry from source CoordinateSystem to a new 
                    context 
             CoordinateSystem.
        
            Returns: Transformed Geometry.
        Transform(self: Geometry, cs: CoordinateSystem) -> Geometry
        
            Transforms geometry by the given CoordinateSystem's transform
        """
        pass

    def Translate(self, *__args):
        """
        Translate(self: Geometry, direction: Vector, distance: float) -> Geometry
        
            Translates any geometry type by the given distance in the given 
                    direction.
        
            direction: Displacement direction.
            distance: Displacement distance along given direction.
            Returns: Transformed Geometry.
        Translate(self: Geometry, direction: Vector) -> Geometry
        
            Translate geometry in the given direction by the vector length
        Translate(self: Geometry, xTranslation: float, yTranslation: float, zTranslation: float) -> Geometry
        
            Translates any given geometry by the given displacements in the x, y,
                    and z 
             directions defined in WCS respectively.
        
        
            xTranslation: Displacement along X-axis.
            yTranslation: Displacement along Y-axis.
            zTranslation: Displacement along Z-axis.
            Returns: Transformed Geometry.
        """
        pass

    def Trim(self, other, pick):
        """
        Trim(self: Geometry, other: Geometry, pick: Point) -> Array[Geometry]
        
            Removes elements of the entity closest to the pick point
        """
        pass

    @staticmethod
    def UpdateDisplay():
        """ UpdateDisplay() """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BoundingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the BoundingBox containing the given piece of Geometry

Get: BoundingBox(self: Geometry) -> BoundingBox

"""

    ContextCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the context/reference coordinate system that was used to create this geometry.

Get: ContextCoordinateSystem(self: Geometry) -> CoordinateSystem

"""


    mConstructor = None


class Curve(Geometry, IDisposable, IGraphicItem):
    # no doc
    def ApproximateWithArcAndLineSegments(self):
        """
        ApproximateWithArcAndLineSegments(self: Curve) -> Array[Curve]
        
            Approximate a Curve with a collection of Arcs and Lines
            Returns: An Array of Arcs and Lines approximating the curve
        """
        pass

    @staticmethod
    def ByBlendBetweenCurves(curve1, curve2, endOrStart1, endOrStart2, isG2Continuous):
        """
        ByBlendBetweenCurves(curve1: Curve, curve2: Curve, endOrStart1: bool, endOrStart2: bool, isG2Continuous: bool) -> Curve
        
            Create a curve that blends between two curves
        
            curve1: First curve to blend
            curve2: Second curve to blend
            endOrStart1: flag to indicate which end of curve1 to blend
            endOrStart2: flag to indicate which end of curve1 to blend
            isG2Continuous: flag to indicate if resultant curve is of G1 continuity or G2 continuity
        """
        pass

    @staticmethod
    def ByIsoCurveOnSurface(baseSurface, direction, parameter):
        """
        ByIsoCurveOnSurface(baseSurface: Surface, direction: int, parameter: float) -> Curve
        
            Create a curve by isoline of surface
        
            baseSurface: Base surface
            direction: if 0 isoline is along u direction, if 1 along v direction
            parameter: fixed for the curve value of other surface parameter
        """
        pass

    @staticmethod
    def ByParameterLineOnSurface(baseSurface, startParams, endParams):
        """
        ByParameterLineOnSurface(baseSurface: Surface, startParams: UV, endParams: UV) -> Curve
        
            Create a curve by line of surface in uv space
        
            baseSurface: Surface to use
            startParams: Starting uv at which curve will start
            endParams: Ending uv at which curve will end
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def CoordinateSystemAtDistance(self, segmentLength):
        """ CoordinateSystemAtDistance(self: Curve, segmentLength: float) -> CoordinateSystem """
        pass

    def CoordinateSystemAtParameter(self, param):
        """
        CoordinateSystemAtParameter(self: Curve, param: float) -> CoordinateSystem
        
            Get a CoordinateSystem with origin at the point at the given parameter. The XAxis is aligned 
             with the curve normal,  the YAxis is aligned with the curve tangent at this point, and the ZAxis 
             is aligned with the up-vector or binormal at this point
        
        
            param: The parameter at which to evaluate
            Returns: The aligned CoordinateSystem at the point
        """
        pass

    def CoordinateSystemAtSegmentLength(self, segmentLength):
        """
        CoordinateSystemAtSegmentLength(self: Curve, segmentLength: float) -> CoordinateSystem
        
            Returns a CoordinateSystem at specified distance from Curve start Point. Y Axis lies tangent to 
             the Curve, X Axis is the curvature.
        
        
            segmentLength: The distance along the curve at which to evaluate
            Returns: CoordinateSystem on curve
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def DistanceAtParameter(self, param):
        """ DistanceAtParameter(self: Curve, param: float) -> float """
        pass

    def DivideByDistance(self, divisions):
        """
        DivideByDistance(self: Curve, divisions: int) -> Array[Curve]
        
            Divides curve into given number of curves with equal distances between start and end of each 
             curve (equal chords).
        
        
            divisions: Number of divisions
            Returns: An Array of Curves after dividing
        """
        pass

    def DivideByDistanceFromParameter(self, distance, parameter):
        """
        DivideByDistanceFromParameter(self: Curve, distance: float, parameter: float) -> Array[Curve]
        
            Divides curve into curves of given chord length measured from given parameter location
        
            distance: Chord length of each curve obtained from splitting
            parameter: Parameter location for measuring from
            Returns: An Array of Curves after dividing
        """
        pass

    def DivideByLengthFromParameter(self, length, parameter):
        """
        DivideByLengthFromParameter(self: Curve, length: float, parameter: float) -> Array[Curve]
        
            Divides curve into curves of given length measured from the given parameter location
        
            length: Length of  curves after division
            parameter: Parameter location for measuring from
            Returns: Array of Curves after dividing
        """
        pass

    def DivideEqually(self, divisions):
        """
        DivideEqually(self: Curve, divisions: int) -> Array[Curve]
        
            Divides curve into given number of equal length curves
        
            divisions: Number of divisions
            Returns: An Array of Curves after dividing
        """
        pass

    def EndParameter(self):
        """
        EndParameter(self: Curve) -> float
        
            Get the end of the domain in which the curve can be evaluated
            Returns: The end of the domain in which the curve can be evaluated
        """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Extend(self, distance, pickSide):
        """
        Extend(self: Curve, distance: float, pickSide: Point) -> Curve
        
            Extend a Curve by a given distance at a particular end determined by a pick Point.  The picked 
             side will be extended.  Closed curves like Circles and Ellipses cannot be extended.
        
        
            distance: Distance to extend
            pickSide: A Point on the end to extend
            Returns: The extended Curve
        """
        pass

    def ExtendEnd(self, distance):
        """
        ExtendEnd(self: Curve, distance: float) -> Curve
        
            Extend a Curve by a given distance on its end.  Closed curves like Circles and Ellipses cannot 
             be extended.
        
        
            distance: Distance to extend
            Returns: The extended Curve
        """
        pass

    def ExtendStart(self, distance):
        """
        ExtendStart(self: Curve, distance: float) -> Curve
        
            Extend a Curve by a given distance on its start side.  Closed curves like Circles and Ellipses 
             cannot be extended.
        
        
            distance: Distance to extend
            Returns: The extended Curve
        """
        pass

    def Extrude(self, *__args):
        """
        Extrude(self: Curve, direction: Vector, distance: float) -> Surface
        
            Extrudes a Curve in the specified direction, by the specified distance
        
            direction: Vector to extrude along
            distance: Distance to extrude
            Returns: The extruded Surface
        Extrude(self: Curve, direction: Vector) -> Surface
        
            Extrudes a Curve in the specified direction, by the length of the input Vector
        
            direction: Vector to extrude along
            Returns: The extruded Surface
        Extrude(self: Curve, distance: float) -> Surface
        
            Extrudes a Curve in the normal Vector direction
        
            distance: The distance to extrude the curve
            Returns: The extruded Surface
        """
        pass

    def ExtrudeAsSolid(self, *__args):
        """
        ExtrudeAsSolid(self: Curve, direction: Vector, distance: float) -> Solid
        
            Extrudes a Curve in the specified direction, by the specified distance. Curve must be closed.
        
            direction: Vector to extrude along
            distance: Distance to extrude
            Returns: The extruded Solid
        ExtrudeAsSolid(self: Curve, direction: Vector) -> Solid
        
            Extrudes a Curve in the specified direction, by the length of the input Vector. Curve must be 
             closed.
        
        
            direction: Vector to extrude along
            Returns: The extruded Solid
        ExtrudeAsSolid(self: Curve, distance: float) -> Solid
        
            Extrudes a Curve in the Normal direction by the specified distance. Curve must be closed.
        
            distance: Distance to extrude
            Returns: The extruded Solid
        """
        pass

    def HorizontalFrameAtParameter(self, param):
        """
        HorizontalFrameAtParameter(self: Curve, param: float) -> CoordinateSystem
        
            Get a CoordinateSystem with origin at the point at the given parameter
        
            param: The parameter at which to evaluate
            Returns: The axis-aligned CoordinateSystem at the point
        """
        pass

    def Join(self, *__args):
        """
        Join(self: Curve, curves: IEnumerable[Curve]) -> PolyCurve
        Join(self: Curve, curve: Curve) -> PolyCurve
        
            Join this curve and the input curve into a new PolyCurve, maintaining the original curves 
             exactly.
        
        
            curve: The curve to join to
            Returns: A PolyCurve made up of the two curves
        """
        pass

    def LengthBetweenParameters(self, startParam, endParam):
        """ LengthBetweenParameters(self: Curve, startParam: float, endParam: float) -> float """
        pass

    def NormalAtParameter(self, param):
        """
        NormalAtParameter(self: Curve, param: float) -> Vector
        
            Get a Vector perpendicular to the curve at a specified parameter between StartParameter() and 
             EndParameter()
        
        
            param: The parameter at which to evaluate
            Returns: A Vector perpendicular to the curve at param
        """
        pass

    def Offset(self, distance):
        """
        Offset(self: Curve, distance: float) -> Curve
        
            Offset a Curve by a specified amount. Curve must be planar, and, if a BSplineCurve/NurbsCurve, 
             must have degree > 1.
        
        
            distance: A positive or negative distance to offset
            Returns: new offsetted curves
        """
        pass

    def ParameterAtChordLength(self, chordLength, parameter, forward):
        """
        ParameterAtChordLength(self: Curve, chordLength: float, parameter: float, forward: bool) -> float
        
            Get the parameter at a particular chord length along the curve from given location.
        
            chordLength: The chord length at which to evaluate
            parameter: Parameter on the curve to measure from
            forward: true if move forward along curve
            Returns: The parameter
        """
        pass

    def ParameterAtDistance(self, segmentLength):
        """ ParameterAtDistance(self: Curve, segmentLength: float) -> float """
        pass

    def ParameterAtPoint(self, point):
        """
        ParameterAtPoint(self: Curve, point: Point) -> float
        
            Get the parameter at a particular point along the Curve
        
            point: A Point along or near the Curve
            Returns: The closest parameter along the curve
        """
        pass

    def ParameterAtSegmentLength(self, segmentLength):
        """
        ParameterAtSegmentLength(self: Curve, segmentLength: float) -> float
        
            Get the parameter at a particular arc length along the curve.
        
            segmentLength: The distance along the curve at which to evaluate
            Returns: The parameter
        """
        pass

    def ParameterSplit(self, *__args):
        """
        ParameterSplit(self: Curve, parameters: Array[float]) -> Array[Curve]
        ParameterSplit(self: Curve, parameter: float) -> Array[Curve]
        """
        pass

    def ParameterTrim(self, startParameter, endParameter):
        """ ParameterTrim(self: Curve, startParameter: float, endParameter: float) -> Curve """
        pass

    def ParameterTrimEnd(self, endParameter):
        """ ParameterTrimEnd(self: Curve, endParameter: float) -> Curve """
        pass

    def ParameterTrimInterior(self, startParameter, endParameter):
        """ ParameterTrimInterior(self: Curve, startParameter: float, endParameter: float) -> Array[Curve] """
        pass

    def ParameterTrimSegments(self, parameters):
        """ ParameterTrimSegments(self: Curve, parameters: Array[float]) -> Array[Curve] """
        pass

    def ParameterTrimStart(self, startParameter):
        """ ParameterTrimStart(self: Curve, startParameter: float) -> Curve """
        pass

    def Patch(self):
        """
        Patch(self: Curve) -> Surface
        
            Patch a closed Curve
            Returns: A Surface on the interior of the curve the Curve
        """
        pass

    def PlaneAtDistance(self, segmentLength):
        """ PlaneAtDistance(self: Curve, segmentLength: float) -> Plane """
        pass

    def PlaneAtParameter(self, param):
        """
        PlaneAtParameter(self: Curve, param: float) -> Plane
        
            Returns a Plane whose normal aligns with the tangent of the Curve. Parameters are adjusted such 
             that 0 is always the start Point and 1 is always the end Point.
        """
        pass

    def PlaneAtSegmentLength(self, segmentLength):
        """
        PlaneAtSegmentLength(self: Curve, segmentLength: float) -> Plane
        
            Returns a Plane at the specified distance along the Curve from the  start Point. The normal of 
             the Plane aligns with the tangent of the  Curve.
        
        
            segmentLength: The distance along the curve at which to evaluate
            Returns: Plane on curve
        """
        pass

    def PointAtChordLength(self, chordLength, parameterLocation, forward):
        """
        PointAtChordLength(self: Curve, chordLength: float, parameterLocation: float, forward: bool) -> Point
        
            Get the point at a particular chord length of the curve from given parameter location.
        
            chordLength: The chord length at which to evaluate
            parameterLocation: Parameter on the curve to measure from
            forward: true if move forward along curve
            Returns: Point on curve
        """
        pass

    def PointAtDistance(self, segmentLength):
        """ PointAtDistance(self: Curve, segmentLength: float) -> Point """
        pass

    def PointAtParameter(self, param):
        """
        PointAtParameter(self: Curve, param: float) -> Point
        
            Get a Point on the Curve at a specified parameter between StartParameter() and EndParameter()
        
            param: The parameter at which to evaluate
            Returns: Point
        """
        pass

    def PointAtSegmentLength(self, segmentLength):
        """
        PointAtSegmentLength(self: Curve, segmentLength: float) -> Point
        
            Get a Point at a particular arc length along the curve
        
            segmentLength: The distance along the curve at which to evaluate
            Returns: The point at the given arc length
        """
        pass

    def PointsAtChordLengthFromPoint(self, point, chordLength):
        """
        PointsAtChordLengthFromPoint(self: Curve, point: Point, chordLength: float) -> Array[Point]
        
            Returns points spaced on the curve at given chord length starting from the given point
        
            point: The reference point from where to measure
            Returns: List of points on curve
        """
        pass

    def PointsAtEqualChordLength(self, divisions):
        """
        PointsAtEqualChordLength(self: Curve, divisions: int) -> Array[Point]
        
            Returns points spaced along curve at equal chord length  based on the input number of divisions
            Returns: List of points on curve
        """
        pass

    def PointsAtEqualSegmentLength(self, divisions):
        """
        PointsAtEqualSegmentLength(self: Curve, divisions: int) -> Array[Point]
        
            Returns points spaced equally along the curve length  based on the input number of divisions
            Returns: Points spaced equally along length of curve
        """
        pass

    def PointsAtSegmentLengthFromPoint(self, point, segmentLength):
        """
        PointsAtSegmentLengthFromPoint(self: Curve, point: Point, segmentLength: float) -> Array[Point]
        
            Returns points spaced equally along the curve at given segment length and starting from the 
             given point
        
        
            point: The reference point from where to measure
            segmentLength: The distance along the curve at which to evaluate
            Returns: List of points on curve
        """
        pass

    def Project(self, baseGeometry, projectionDirection):
        """
        Project(self: Curve, baseGeometry: Geometry, projectionDirection: Vector) -> Array[Geometry]
        
            Project another piece of Geometry onto this along a given direction Vector
        """
        pass

    def PullOntoPlane(self, plane):
        """
        PullOntoPlane(self: Curve, plane: Plane) -> Curve
        
            Create a curve by pulling onto plane
        
            plane: The plane on which to pull the curve
            Returns: A Curve on the Plane
        """
        pass

    def PullOntoSurface(self, surface):
        """
        PullOntoSurface(self: Curve, surface: Surface) -> Curve
        
            Pull this Curve onto the input Surface, in the direction of the Surface normals.
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Curve) -> Curve
        
            Reverse the direction of the curve
            Returns: A new Curve with the opposite direction
        """
        pass

    def SegmentLengthAtParameter(self, param):
        """
        SegmentLengthAtParameter(self: Curve, param: float) -> float
        
            Get the arc length along the Curve at the particular parameter.
        
            param: The parameter at which to evaluate
            Returns: The arc length
        """
        pass

    def SegmentLengthBetweenParameters(self, startParam, endParam):
        """
        SegmentLengthBetweenParameters(self: Curve, startParam: float, endParam: float) -> float
        
            Get the arc length between two parameter points on the curve
        
            startParam: The start of the domain
            endParam: The end of the domain
            Returns: The arc length between the two parameters
        """
        pass

    def Simplify(self, tolerance):
        """
        Simplify(self: Curve, tolerance: float) -> Curve
        
            Returns a new Curve approximated with the supplied tolerance
        """
        pass

    def SplitByParameter(self, *__args):
        """
        SplitByParameter(self: Curve, parameters: Array[float]) -> Array[Curve]
        
            Split a Curve into multiple pieces at the given parameters
        
            parameters: A list of parameters at which to split the curve
            Returns: Curves created from splitting
        SplitByParameter(self: Curve, parameter: float) -> Array[Curve]
        
            Split a Curve into two pieces at the given parameter
        
            parameter: The parameter at which to do the split
            Returns: Two Curves remaining after the split
        """
        pass

    def SplitByPoints(self, points):
        """ SplitByPoints(self: Curve, points: IEnumerable[Point]) -> Array[Curve] """
        pass

    def StartParameter(self):
        """
        StartParameter(self: Curve) -> float
        
            Get the start of the domain in which the curve can be evaluated
            Returns: The start of the domain in which the curve can be evaluated
        """
        pass

    def SweepAsSolid(self, path):
        """
        SweepAsSolid(self: Curve, path: Curve) -> Solid
        
            Sweeps this closed Curve along the path Curve, creating a Solid
        """
        pass

    def SweepAsSurface(self, path):
        """
        SweepAsSurface(self: Curve, path: Curve) -> Surface
        
            Sweeps this Curve along the path Curve, creating a Surface
        """
        pass

    def TangentAtParameter(self, param):
        """
        TangentAtParameter(self: Curve, param: float) -> Vector
        
            Get a Vector tangent to the curve at a specified parameter between StartParameter() and 
             EndParameter()
        
        
            param: The parameter at which to evaluate
            Returns: A Vector parallel to the curve at param
        """
        pass

    def ToNurbsCurve(self):
        """
        ToNurbsCurve(self: Curve) -> NurbsCurve
        
            Converts the Curve to a NurbsCurve approximation
            Returns: A NurbsCurve approximating the Curve
        """
        pass

    def ToString(self):
        """ ToString(self: Curve) -> str """
        pass

    def TrimByEndParameter(self, endParameter):
        """
        TrimByEndParameter(self: Curve, endParameter: float) -> Curve
        
            Removes the end of the Curve at the specified parameter
        
            endParameter: The parameter at which to start the trim
            Returns: A new Curve with the end removed
        """
        pass

    def TrimByParameter(self, startParameter, endParameter):
        """
        TrimByParameter(self: Curve, startParameter: float, endParameter: float) -> Curve
        
            Removes the beginning and end of the Curve at the specified parameters.
        
            startParameter: The parameter at which to start the trim
            endParameter: The parameter at which to start the trim
            Returns: A new Curve with the outer segments removed
        """
        pass

    def TrimByStartParameter(self, startParameter):
        """
        TrimByStartParameter(self: Curve, startParameter: float) -> Curve
        
            Removes the start of the Curve at the specified parameter
        
            startParameter: The parameter at which to start the trim
            Returns: A new Curve with the start removed
        """
        pass

    def TrimInteriorByParameter(self, startParameter, endParameter):
        """
        TrimInteriorByParameter(self: Curve, startParameter: float, endParameter: float) -> Array[Curve]
        
            Removes the interior portion of a Curve at the specified parameters
        
            startParameter: The parameter at which to start the trim
            endParameter: The parameter at which to start the trim
            Returns: A new Curve with the interior segment removed
        """
        pass

    def TrimSegmentsByParameter(self, parameters, discardEvenSegments=None):
        """
        TrimSegmentsByParameter(self: Curve, parameters: Array[float], discardEvenSegments: bool) -> Array[Curve]
        
            Removes several segments of the Curve, disgarding 2nd, 4th, 6th ... segments if the bool is true
        
            parameters: A list of parameters at which to split the curve
            discardEvenSegments: Whether to discard even segments or not
            Returns: An Array of curves disgarding 2nd, 4th, 6th ... segments if the bool is true
        TrimSegmentsByParameter(self: Curve, parameters: Array[float]) -> Array[Curve]
        
            Removes several segments of the curve, discarding the 1st, 3rd, 5th ... segments
        
            parameters: A list of parameters at which to split the curve
            Returns: An Array of curves discarding the 1st, 3rd, 5th ... segments
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the end Point along the Curve

Get: EndPoint(self: Curve) -> Point

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine if the Curve is closed or not

Get: IsClosed(self: Curve) -> bool

"""

    IsPlanar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine whether a Curve is planar or not

Get: IsPlanar(self: Curve) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total arc length of the curve

Get: Length(self: Curve) -> float

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The normal to the plane where the curve is contained.  Only            valid for planar curves.

Get: Normal(self: Curve) -> Vector

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the start Point along the Curve

Get: StartPoint(self: Curve) -> Point

"""


    mConstructor = None


class Arc(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Arc """
        pass

    @staticmethod
    def ByCenterPointRadiusAngle(center, radius, startAngle, endAngle, normal):
        """
        ByCenterPointRadiusAngle(center: Point, radius: float, startAngle: float, endAngle: float, normal: Vector) -> Arc
        
            Create an arc by providing it's center point, radius, angle sweep, and normal vector
        
            center: The center of the arc
            radius: Radius of the arc
            startAngle: Start angle in degrees
            endAngle: End angle in degrees
            normal: A vector defining the normal of the arc
            Returns: An Arc
        """
        pass

    @staticmethod
    def ByCenterPointStartPointEndPoint(centerPoint, startPoint, endPoint):
        """
        ByCenterPointStartPointEndPoint(centerPoint: Point, startPoint: Point, endPoint: Point) -> Arc
        
            Create an arc by providing it's center point, start point, and end point
        
            centerPoint: The center of the arc
            startPoint: The start point on the arc
            endPoint: The end point of the arc
            Returns: An Arc
        """
        pass

    @staticmethod
    def ByCenterPointStartPointSweepAngle(centerPoint, startPoint, sweepAngle, normal):
        """
        ByCenterPointStartPointSweepAngle(centerPoint: Point, startPoint: Point, sweepAngle: float, normal: Vector) -> Arc
        
            Create an arc by providing it's center point, start point, sweep point, and normal
        
            centerPoint: The center of the arc
            startPoint: The start point on the arc
            sweepAngle: The angle to sweep out
            normal: The normal to the arc
            Returns: An Arc
        """
        pass

    @staticmethod
    def ByFillet(curve1, curve2, radius):
        """
        ByFillet(curve1: Curve, curve2: Curve, radius: float) -> Arc
        
            Create an arc by filleting twp curves with given radius
        
            curve1: First curve
            curve2: Second curve
            radius: The radius of the fillet arc
            Returns: An Arc
        """
        pass

    @staticmethod
    def ByFilletTangentToCurve(curve1, curveTangentTo, curve2):
        """
        ByFilletTangentToCurve(curve1: Curve, curveTangentTo: Curve, curve2: Curve) -> Arc
        
            Create an arc by filleting two curves tangent to given curve at internal point
        
            curve1: First curve
            curveTangentTo: curve to which the fillet arc is tangent at internal point
            curve2: Second curve
            Returns: An Arc
        """
        pass

    @staticmethod
    def ByStartEndAndTangencies(point1, vector1, point2, vector2):
        """
        ByStartEndAndTangencies(point1: Point, vector1: Vector, point2: Point, vector2: Vector) -> Array[Arc]
        
            Create an arc or tangent bi arc by start and end points and tangencies at start and end
        
            point1: Point for the start of bi-arc
            vector1: Tangent vector for the start of bi-arc
            point2: Point for the end of bi-arc
            vector2: Tangent vector for the end of bi-arc
        """
        pass

    @staticmethod
    def ByStartPointEndPointStartTangent(startPoint, endPoint, startTangent):
        """
        ByStartPointEndPointStartTangent(startPoint: Point, endPoint: Point, startTangent: Vector) -> Arc
        
            Create an Arc from start Point to end Point with start tangent to Vector
        """
        pass

    @staticmethod
    def ByThreePoints(firstPoint, secondPoint, thirdPoint):
        """
        ByThreePoints(firstPoint: Point, secondPoint: Point, thirdPoint: Point) -> Arc
        
            Create an arc by providing three sequential points along its circumference.
        
            firstPoint: First point along the curve
            secondPoint: Second point along the curve
            thirdPoint: Third point along the curve
            Returns: An Arc
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Arc) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The center point of the arc

Get: CenterPoint(self: Arc) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the arc

Get: Radius(self: Arc) -> float

"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start angle in degrees

Get: StartAngle(self: Arc) -> float

"""

    SweepAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total sweep angle in degrees

Get: SweepAngle(self: Arc) -> float

"""


    mConstructor = None


class BoundingBox(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCorners(min, max):
        """
        ByCorners(min: Point, max: Point) -> BoundingBox
        
            Creates the an axis-aligned BoundingBox spanning between the minimum Point and the maximum Point.
        """
        pass

    @staticmethod
    def ByCornersCoordinateSystem(min, max, cs):
        """ ByCornersCoordinateSystem(min: Point, max: Point, cs: CoordinateSystem) -> BoundingBox """
        pass

    @staticmethod
    def ByGeometry(geom):
        """
        ByGeometry(geom: IEnumerable[Geometry]) -> BoundingBox
        ByGeometry(geom: Geometry) -> BoundingBox
        
            Create an axis-aligned BoundingBox around input Geometry.
        """
        pass

    @staticmethod
    def ByGeometryCoordinateSystem(geom, cs):
        """
        ByGeometryCoordinateSystem(geom: IEnumerable[Geometry], cs: CoordinateSystem) -> BoundingBox
        ByGeometryCoordinateSystem(geom: Geometry, cs: CoordinateSystem) -> BoundingBox
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: BoundingBox) -> int """
        pass

    def Contains(self, point):
        """
        Contains(self: BoundingBox, point: Point) -> bool
        
            Determine if a point is inside of the BoundingBox
        
            point: The test point
            Returns: True if the point is inside, otherwise False
        """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: BoundingBox, other: DesignScriptEntity) -> bool """
        pass

    def Intersection(self, other):
        """
        Intersection(self: BoundingBox, other: BoundingBox) -> BoundingBox
        
            Get the intersection of two BoundingBoxes
        """
        pass

    def Intersects(self, other):
        """
        Intersects(self: BoundingBox, other: BoundingBox) -> bool
        
            Determine whether two BoundingBoxes intersect
        """
        pass

    def IsEmpty(self):
        """
        IsEmpty(self: BoundingBox) -> bool
        
            Determine if the BoundingBox is empty
        """
        pass

    def ToCuboid(self):
        """
        ToCuboid(self: BoundingBox) -> Cuboid
        
            Get the BoundingBox as a Solid Cuboid
            Returns: A Cuboid representation of the BoundingBox
        """
        pass

    def ToPolySurface(self):
        """
        ToPolySurface(self: BoundingBox) -> PolySurface
        
            Get the BoundingBox as a collection of Surfaces
            Returns: A PolySurface representation of the BoundingBox
        """
        pass

    def ToString(self):
        """ ToString(self: BoundingBox) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ContextCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContextCoordinateSystem(self: BoundingBox) -> CoordinateSystem

"""

    MaxPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum point

Get: MaxPoint(self: BoundingBox) -> Point

"""

    MinPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum point

Get: MinPoint(self: BoundingBox) -> Point

"""


    mConstructor = None


class Circle(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Circle """
        pass

    @staticmethod
    def ByCenterPointRadius(centerPoint, radius):
        """
        ByCenterPointRadius(centerPoint: Point, radius: float) -> Circle
        
            Creates a Circle with input center Point and radius in the world XY plane, with world Z as 
             normal.
        """
        pass

    @staticmethod
    def ByCenterPointRadiusNormal(centerPoint, radius, normal):
        """
        ByCenterPointRadiusNormal(centerPoint: Point, radius: float, normal: Vector) -> Circle
        
            Creates a Circle with specified center Point, radius, and normal direction.
        """
        pass

    @staticmethod
    def ByPlaneRadius(plane, radius):
        """
        ByPlaneRadius(plane: Plane, radius: float) -> Circle
        
            Create a Circle centered at the input Plane origin (root), lying in  the input Plane, with given 
             radius.
        """
        pass

    @staticmethod
    def ByThreePoints(p1, p2, p3):
        """
        ByThreePoints(p1: Point, p2: Point, p3: Point) -> Circle
        
            Create a Circle passing through three input Points.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Circle) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The center of the circle

Get: CenterPoint(self: Circle) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the circle

Get: Radius(self: Circle) -> float

"""


    mConstructor = None


class CoEdge(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: CoEdge) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: CoEdge) -> Edge

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndVertex(self: CoEdge) -> Vertex

"""

    Loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loop(self: CoEdge) -> Loop

"""

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Next(self: CoEdge) -> CoEdge

"""

    Partner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Partner(self: CoEdge) -> CoEdge

"""

    Previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Previous(self: CoEdge) -> CoEdge

"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: CoEdge) -> bool

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartVertex(self: CoEdge) -> Vertex

"""


    mConstructor = None


class Topology(Geometry, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Topology) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Edges of the Topology

Get: Edges(self: Topology) -> Array[Edge]

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Faces of the Topology

Get: Faces(self: Topology) -> Array[Face]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Vertices of the Topology

Get: Vertices(self: Topology) -> Array[Vertex]

"""


    mConstructor = None


class Solid(Topology, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByJoinedSurfaces(facesOfSolid):
        """ ByJoinedSurfaces(facesOfSolid: IEnumerable[Surface]) -> Solid """
        pass

    @staticmethod
    def ByLoft(crossSections, *__args):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> Solid
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> Solid
        ByLoft(crossSections: IEnumerable[Curve]) -> Solid
        """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle):
        """
        ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float) -> Solid
        
            Create a Surface of revolution, sweeping the profile Curve around the axis Ray formed by the 
             origin and the axis Vector, from the start angle in degrees to the sweep angle in degrees.
        """
        pass

    @staticmethod
    def BySweep(profile, path):
        """
        BySweep(profile: Curve, path: Curve) -> Solid
        
            Sweep a closed Curve along a path.
        """
        pass

    @staticmethod
    def BySweep2Rails(path, guideRail, profile):
        """
        BySweep2Rails(path: Curve, guideRail: Curve, profile: Curve) -> Solid
        
            Sweep a closed profile Curve along two rail Curves.
        
            path: The input path to sweep along.
            guideRail: A rail to guide the orientation of the sweep.
        """
        pass

    @staticmethod
    def ByUnion(solids):
        """ ByUnion(solids: IEnumerable[Solid]) -> Solid """
        pass

    def Centroid(self):
        """
        Centroid(self: Solid) -> Point
        
            The centroid of the Solid
        """
        pass

    def Chamfer(self, edges, offset):
        """ Chamfer(self: Solid, edges: IEnumerable[Edge], offset: float) -> Solid """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Difference(self, other):
        """
        Difference(self: Solid, other: Solid) -> Solid
        
            The boolean difference of this Solid with another
        """
        pass

    def DifferenceAll(self, others):
        """ DifferenceAll(self: Solid, others: IEnumerable[Solid]) -> Solid """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Fillet(self, edges, radius):
        """ Fillet(self: Solid, edges: IEnumerable[Edge], radius: float) -> Solid """
        pass

    def ProjectInputOnto(self, geometryToProject, projectDirection):
        """
        ProjectInputOnto(self: Solid, geometryToProject: Geometry, projectDirection: Vector) -> Array[Geometry]
        
            Projects the input Geometry onto this Solid, in the direction of the input Vector
        """
        pass

    def ThinShell(self, internalFaceThickness, externalFaceThickness):
        """
        ThinShell(self: Solid, internalFaceThickness: float, externalFaceThickness: float) -> Solid
        
            Obtain a solid Shell from the Faces of this Solid
        
            internalFaceThickness: Distance to extend the shell inwards
            externalFaceThickness: Distance to extend she shell outwards
        """
        pass

    def ToString(self):
        """ ToString(self: Solid) -> str """
        pass

    def Union(self, solid):
        """
        Union(self: Solid, solid: Solid) -> Solid
        
            The boolean union of this Solid and another.
        """
        pass

    def UnionAll(self, solids):
        """ UnionAll(self: Solid, solids: IEnumerable[Solid]) -> Solid """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the surface area -- sum of all the areas of all faces

Get: Area(self: Solid) -> float

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total volume of the Solid

Get: Volume(self: Solid) -> float

"""


    mConstructor = None


class Cone(Solid, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCoordinateSystemHeightRadii(cs, height, startRadius, endRadius):
        """
        ByCoordinateSystemHeightRadii(cs: CoordinateSystem, height: float, startRadius: float, endRadius: float) -> Cone
        
            Creates a Cone with base Point at CoordinateSystem origin, extending in the CoordinateSystem Z 
             axis deriction length amount, with a  circular bases in the CoordinateSystem XY Plane.
        """
        pass

    @staticmethod
    def ByCoordinateSystemHeightRadius(cs, height, startRadius):
        """
        ByCoordinateSystemHeightRadius(cs: CoordinateSystem, height: float, startRadius: float) -> Cone
        
            Creates a Cone with base Point at CoordinateSystem origin, extending in the CoordinateSystem Z 
             axis deriction length amount, with a  circular base in the CoordinateSystem XY Plane.
        """
        pass

    @staticmethod
    def ByPointsRadii(startPoint, endPoint, startRadius, endRadius):
        """
        ByPointsRadii(startPoint: Point, endPoint: Point, startRadius: float, endRadius: float) -> Cone
        
            Create a Cone with axis from start Point to end Point, with given  radiuses at start and end. 
             This object does not have an apex, and can be thought of as a trimmed Cone.
        """
        pass

    @staticmethod
    def ByPointsRadius(startPoint, endPoint, startRadius):
        """
        ByPointsRadius(startPoint: Point, endPoint: Point, startRadius: float) -> Cone
        
            Create a Cone with given base radius at start Point, extending to a  apex at end Point.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cone) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The end point

Get: EndPoint(self: Cone) -> Point

"""

    EndRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius at the bottom

Get: EndRadius(self: Cone) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total height

Get: Height(self: Cone) -> float

"""

    RadiusRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ratio between the top and bottom radius

Get: RadiusRatio(self: Cone) -> float

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start point

Get: StartPoint(self: Cone) -> Point

"""

    StartRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius at the base

Get: StartRadius(self: Cone) -> float

"""


    mConstructor = None


class CoordinateSystem(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCylindricalCoordinates(cs, radius, theta, height):
        """
        ByCylindricalCoordinates(cs: CoordinateSystem, radius: float, theta: float, height: float) -> CoordinateSystem
        
            Creates a CoordinateSystem at the specified cylindrical coordinate parameters with respect to 
             the specified coordinate system
        """
        pass

    @staticmethod
    def ByMatrix(matrix):
        """
        ByMatrix(matrix: Array[float]) -> CoordinateSystem
        
            Deprecated -- DO NOT USE
        """
        pass

    @staticmethod
    def ByOrigin(*__args):
        """
        ByOrigin(origin: Point) -> CoordinateSystem
        
            Create a CoordinateSystem with origin at input Point, with X and Y Axes
                    set as WCS 
             X and Y Axes.
        
        ByOrigin(x: float, y: float, z: float) -> CoordinateSystem
        
            Create a CoordinateSystem with origin at X, Y, and Z locations, with
                    X and Y Axes 
             set as WCS X and Y Axes.
        
        ByOrigin(x: float, y: float) -> CoordinateSystem
        
            Create a CoordinateSystem with origin at X and Y locations, with
                    X and Y Axes set 
             as WCS X and Y Axes. Z defaults to 0.
        """
        pass

    @staticmethod
    def ByOriginVectors(origin, xAxis, yAxis, zAxis=None):
        """
        ByOriginVectors(origin: Point, xAxis: Vector, yAxis: Vector, zAxis: Vector) -> CoordinateSystem
        
            Create a CoordinateSystem at the origin with X and Y axis, with Z
                    axis ignored 
             completely. Input Vectors are normalized before creating 
                    the CoordinateSystem.
        
        ByOriginVectors(origin: Point, xAxis: Vector, yAxis: Vector) -> CoordinateSystem
        
            Create a CoordinateSystem at the origin with X and Y axis. 
                    Input Vectors are 
             normalized before creating the CoordinateSystem.
        """
        pass

    @staticmethod
    def ByPlane(plane):
        """
        ByPlane(plane: Plane) -> CoordinateSystem
        
            Create a CoordinateSystem with origin equal to input Plane origin, and 
                    X and Y 
             axes lying in the Plane, aligned with Plane X and Y axes.
        """
        pass

    @staticmethod
    def BySphericalCoordinates(cs, radius, theta, phi):
        """
        BySphericalCoordinates(cs: CoordinateSystem, radius: float, theta: float, phi: float) -> CoordinateSystem
        
            Creates a CoordinateSystem at the specified spherical coordinate parameters with respect to the 
             specified coordinate system
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def Identity():
        """
        Identity() -> CoordinateSystem
        
            Creates a CoordinateSystem as the World Coordinate System: origin at 
                    0, 0, 0; x 
             axis at 1, 0, 0; y axis at 0, 1, 0; z axis at 0, 0, 1
        """
        pass

    def Inverse(self):
        """
        Inverse(self: CoordinateSystem) -> CoordinateSystem
        
            Get the inverse of this CoordinateSystem - applying this CoordinateSystem to a piece of Geometry 
             reverses the original.
        """
        pass

    def IsEqualTo(self, other):
        """
        IsEqualTo(self: CoordinateSystem, other: CoordinateSystem) -> bool
        
            Determine if two CoordinateSystems are equal
        """
        pass

    def Mirror(self, mirrorPlane):
        """
        Mirror(self: CoordinateSystem, mirrorPlane: Plane) -> CoordinateSystem
        
            Mirror the object across the input Plane
        """
        pass

    def PostMultiplyBy(self, other):
        """
        PostMultiplyBy(self: CoordinateSystem, other: CoordinateSystem) -> CoordinateSystem
        
            Apply the argument CoordinateSystem after this one - Result = this * other
        """
        pass

    def PreMultiplyBy(self, other):
        """
        PreMultiplyBy(self: CoordinateSystem, other: CoordinateSystem) -> CoordinateSystem
        
            Apply the argument CoordinateSystem before this one - Result = other * this
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: CoordinateSystem, plane: Plane, degrees: float) -> CoordinateSystem
        
            Rotates an object around the origin and normal of the given Plane by a specified
                    
             degree
        
        Rotate(self: CoordinateSystem, origin: Point, axis: Vector, degrees: float) -> CoordinateSystem
        
            Rotates an object around an origin and an axis by a specified 
                    degree
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: CoordinateSystem, plane: Plane, xamount: float, yamount: float, zamount: float) -> CoordinateSystem
        
            Scale non-uniformly around a given Plane
        Scale(self: CoordinateSystem, basePoint: Point, from: Point, to: Point) -> CoordinateSystem
        
            Scale uniformly around a given point, using
        Scale(self: CoordinateSystem, amount: float) -> CoordinateSystem
        
            Scale uniformly around the origin
        Scale(self: CoordinateSystem, xamount: float, yamount: float, zamount: float) -> CoordinateSystem
        
            Scale non-uniformly around the origin
        """
        pass

    def Scale1D(self, basePoint, from, to):
        """
        Scale1D(self: CoordinateSystem, basePoint: Point, from: Point, to: Point) -> CoordinateSystem
        
            Scale in one dimension by base and 2 pick points.  The scaling axis is defined by the line 
             between base and pick0.
        """
        pass

    def Scale2D(self, basePlane, from, to):
        """
        Scale2D(self: CoordinateSystem, basePlane: Plane, from: Point, to: Point) -> CoordinateSystem
        
            Scale in two dimension by base and 2 pick points  The two pick points are projected onto the 
             base plane in order to determine the 2d scale factors
        """
        pass

    def ScaleFactor(self):
        """
        ScaleFactor(self: CoordinateSystem) -> Vector
        
            Returns a Vector containing the X, Y, and Z scale factors
        """
        pass

    def ToString(self):
        """ ToString(self: CoordinateSystem) -> str """
        pass

    def Transform(self, *__args):
        """
        Transform(self: CoordinateSystem, fromCoordinateSystem: CoordinateSystem, contextCoordinateSystem: CoordinateSystem) -> CoordinateSystem
        
            Transforms this CoordinateSystem from source CoordinateSystem to a new 
                    context 
             CoordinateSystem.
        
            Returns: Transformed CoordinateSystem.
        Transform(self: CoordinateSystem, cs: CoordinateSystem) -> CoordinateSystem
        
            Transform the object by the input CoordinateSystem matrix.
        """
        pass

    def Translate(self, *__args):
        """
        Translate(self: CoordinateSystem, direction: Vector, distance: float) -> CoordinateSystem
        
            Translates any CoordinateSystem type by the given distance in the given 
                    direction.
        
            direction: Displacement direction.
            distance: Displacement distance along given direction.
            Returns: Transformed CoordinateSystem.
        Translate(self: CoordinateSystem, direction: Vector) -> CoordinateSystem
        
            Translate the object in the direction and magnitude of input Vector.
        Translate(self: CoordinateSystem, xTranslation: float, yTranslation: float, zTranslation: float) -> CoordinateSystem
        
            Translates any given CoordinateSystem by the given displacements in the x, y,
                    and z 
             directions defined in WCS respectively.
        
        
            xTranslation: Displacement along X-axis.
            yTranslation: Displacement along Y-axis.
            zTranslation: Displacement along Z-axis.
            Returns: Transformed CoordinateSystem.
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Determinant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Obtain the Determinant of this CoordinateSystem

Get: Determinant(self: CoordinateSystem) -> float

"""

    IsScaledOrtho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests if the scaling orthogonal, i.e. does it have a shear component.

Get: IsScaledOrtho(self: CoordinateSystem) -> bool

"""

    IsSingular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determine whether it is possible to get the Inverse of this CoordinateSystem

Get: IsSingular(self: CoordinateSystem) -> bool

"""

    IsUniscaledOrtho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tests if the scaling orthogonal and are all the vectors normalized.

Get: IsUniscaledOrtho(self: CoordinateSystem) -> bool

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Creates a Point representing the CoordinateSystem origin.

Get: Origin(self: CoordinateSystem) -> Point

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns X Axis of CoordinateSystem.

Get: XAxis(self: CoordinateSystem) -> Vector

"""

    XScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the X Axis scaling of the CoordinateSystem: the length of the X Axis vector.

Get: XScaleFactor(self: CoordinateSystem) -> float

"""

    XYPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Plane the X and Y axes lie in, with root at the origin.

Get: XYPlane(self: CoordinateSystem) -> Plane

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns Y Axis of CoordinateSystem.

Get: YAxis(self: CoordinateSystem) -> Vector

"""

    YScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Y Axis scaling of the CoordinateSystem: the length of the Y Axis vector.

Get: YScaleFactor(self: CoordinateSystem) -> float

"""

    YZPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Plane the Y and Z axes lie in, with root at the origin.

Get: YZPlane(self: CoordinateSystem) -> Plane

"""

    ZAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns Z Axis of CoordinateSystem.

Get: ZAxis(self: CoordinateSystem) -> Vector

"""

    ZScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Z Axis scaling of the CoordinateSystem: the length of the Z Axis vector.

Get: ZScaleFactor(self: CoordinateSystem) -> float

"""

    ZXPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Plane the Z and X axes lie in, with root at the origin.

Get: ZXPlane(self: CoordinateSystem) -> Plane

"""


    mConstructor = None


class Cuboid(Solid, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCorners(lowPoint, highPoint):
        """
        ByCorners(lowPoint: Point, highPoint: Point) -> Cuboid
        
            Create an Cuboid spanning from low Point to high Point.
        """
        pass

    @staticmethod
    def ByLengths(*__args):
        """
        ByLengths(cs: CoordinateSystem, width: float, length: float, height: float) -> Cuboid
        
            Create a Cuboid centered and oriented to input CoordinateSystem, with  specified width, length, 
             and height.
        
        ByLengths(origin: Point, width: float, length: float, height: float) -> Cuboid
        
            Create a Cuboid centered at input Point, with specified width, length,  and height.
        ByLengths(width: float, length: float, height: float) -> Cuboid
        
            Create a Cuboid centered at WCS origin, with width, length, and height.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cuboid) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns height distance.                         Note: This return the input dimensions of the Cuboid, NOT the                   actual world space dimensions. In other words, if you create a Cuboid                   width (X-axis) length 10, and transform it to a CoordinateSystem with                   2 times scaling in X, the width will still be 10. ASM does not allow you                   to extract the Vertices of a body in any predictable order, so it                    impossible to determine the dimensions after a transform.

Get: Height(self: Cuboid) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns length distance.                         Note: This return the input dimensions of the Cuboid, NOT the                   actual world space dimensions. In other words, if you create a Cuboid                   width (X-axis) length 10, and transform it to a CoordinateSystem with                   2 times scaling in X, the width will still be 10. ASM does not allow you                   to extract the Vertices of a body in any predictable order, so it                    impossible to determine the dimensions after a transform.

Get: Length(self: Cuboid) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns width distance.                         Note: This return the input dimensions of the Cuboid, NOT the                   actual world space dimensions. In other words, if you create a Cuboid                   width (X-axis) length 10, and transform it to a CoordinateSystem with                   2 times scaling in X, the width will still be 10. ASM does not allow you                   to extract the Vertices of a body in any predictable order, so it                    impossible to determine the dimensions after a transform.

Get: Width(self: Cuboid) -> float

"""


    mConstructor = None


class Cylinder(Cone, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByPointsRadius(startPoint, endPoint, radius):
        """
        ByPointsRadius(startPoint: Point, endPoint: Point, radius: float) -> Cylinder
        
            Construct a Solid Cylinder given the bottom and top center point of the Cylinder.
        """
        pass

    @staticmethod
    def ByRadiusHeight(cs, radius, height):
        """
        ByRadiusHeight(cs: CoordinateSystem, radius: float, height: float) -> Cylinder
        
            Construct a Solid Cylinder defined by a parent CoordinateSystem, the radius, and the height of 
             the cylinder
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Cylinder) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the Cylinder

Get: Radius(self: Cylinder) -> float

"""


    mConstructor = None


class Edge(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Edge) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Faces adjacent to this Edge

Get: AdjacentFaces(self: Edge) -> Array[Face]

"""

    CoEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoEdges(self: Edge) -> Array[CoEdge]

"""

    CurveGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underlying Curve making up the Edge

Get: CurveGeometry(self: Edge) -> Curve

"""

    EndVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Vertex at which this Edge ends

Get: EndVertex(self: Edge) -> Vertex

"""

    StartVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Vertex at which this Edge starts

Get: StartVertex(self: Edge) -> Vertex

"""


    mConstructor = None


class Ellipse(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCoordinateSystemRadii(origin, xAxisRadius, yAxisRadius):
        """
        ByCoordinateSystemRadii(origin: CoordinateSystem, xAxisRadius: float, yAxisRadius: float) -> Ellipse
        
            Create an Ellipse centered and aligned with input CoordinateSystem,  with a x_radius radius in 
             the CS X direction, and y_radius radius in the  CS Y direction.
        """
        pass

    @staticmethod
    def ByOriginRadii(origin, xAxisRadius, yAxisRadius):
        """
        ByOriginRadii(origin: Point, xAxisRadius: float, yAxisRadius: float) -> Ellipse
        
            Create an Ellipse centered at input Point, aligned with WCS XY Plane, with specified X and Y 
             axis radii.
        """
        pass

    @staticmethod
    def ByOriginVectors(origin, xAxisRadius, yAxisRadius):
        """
        ByOriginVectors(origin: Point, xAxisRadius: Vector, yAxisRadius: Vector) -> Ellipse
        
            Create an Ellipse centered at input Point, with two specified axes.  Axes should be be at 90 
             degrees to each other.
        """
        pass

    @staticmethod
    def ByPlaneRadii(plane, xAxisRadius, yAxisRadius):
        """
        ByPlaneRadii(plane: Plane, xAxisRadius: float, yAxisRadius: float) -> Ellipse
        
            Create an Ellipse centered and aligned with input Plane, with a x_radius  radius in the Plane X 
             axis direction, and y_radius radius in the  Plane Y axis direction.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Ellipse) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The center of the Ellipse

Get: CenterPoint(self: Ellipse) -> Point

"""

    MajorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major axis of the Ellipse.  This is the longer axis.  The length of the Vector is the Major radius.

Get: MajorAxis(self: Ellipse) -> Vector

"""

    MinorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor axis of the Ellipse.  This is the shorter axis.  The length of the Vector is the Minor radius.

Get: MinorAxis(self: Ellipse) -> Vector

"""


    mConstructor = None


class EllipseArc(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByPlaneRadiiAngles(plane, xRadius, yRadius, startAngle, sweepAngle):
        """
        ByPlaneRadiiAngles(plane: Plane, xRadius: float, yRadius: float, startAngle: float, sweepAngle: float) -> EllipseArc
        
            Create an EllipseArc in a plane with the given the radii along the X and Y axes and the angles 
             to sweep through
        
        
            plane: The plane the EllipseArc is contained in
            xRadius: The radius of the EllipseArc in the X direction of the Plane
            yRadius: The radius of the EllipseArc in the Y direction of the Plane
            startAngle: The start angle of the arc as measured from the positive x-axis of the input plane
            sweepAngle: The angle to sweep from the start angle in degrees
        """
        pass

    @staticmethod
    def ByPlaneRadiiStartAngleSweepAngle(plane, xRadius, yRadius, startAngle, sweepAngle):
        """ ByPlaneRadiiStartAngleSweepAngle(plane: Plane, xRadius: float, yRadius: float, startAngle: float, sweepAngle: float) -> EllipseArc """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: EllipseArc) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The center of the Ellipse

Get: CenterPoint(self: EllipseArc) -> Point

"""

    MajorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major axis of the Ellipse.  This is the longer axis.  The length of the Vector is the Major radius.

Get: MajorAxis(self: EllipseArc) -> Vector

"""

    MinorAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor axis of the Ellipse.  This is the shorter axis.  The length of the Vector is the Minor radius.

Get: MinorAxis(self: EllipseArc) -> Vector

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The plane in which the ellipse lies

Get: Plane(self: EllipseArc) -> Plane

"""

    StartAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The start angle in degrees

Get: StartAngle(self: EllipseArc) -> float

"""

    SweepAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total sweep angle in degrees

Get: SweepAngle(self: EllipseArc) -> float

"""


    mConstructor = None


class Face(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def SurfaceGeometry(self):
        """
        SurfaceGeometry(self: Face) -> Surface
        
            The underlying Surface making up the Face
        """
        pass

    def ToString(self):
        """ ToString(self: Face) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All of the Edges around this Face in counterclockwise order

Get: Edges(self: Face) -> Array[Edge]

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Face) -> Array[Loop]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All of the Vertices around this Face in counterclockwise order

Get: Vertices(self: Face) -> Array[Vertex]

"""


    mConstructor = None


class GeometryExtension(object):
    # no doc
    @staticmethod
    def AreCoincident(pts):
        """ AreCoincident(pts: Array[IPointEntity]) -> bool """
        pass

    @staticmethod
    def ConvertAll(array, converter):
        """ ConvertAll[(TInput, TOutput)](array: Array[TInput], converter: Converter[TInput, TOutput]) -> Array[TOutput] """
        pass

    @staticmethod
    def DegreesToRadians(deg):
        """ DegreesToRadians(deg: float) -> float """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(x: float, y: float, tolerance: float) -> bool """
        pass

    @staticmethod
    def EqualsTo(thisValue, value):
        """ EqualsTo(thisValue: float, value: float) -> bool """
        pass

    @staticmethod
    def ForEach(array, action):
        """ ForEach[T](array: Array[Array[T]], action: Action[T])ForEach[T](array: Array[T], action: Action[T]) """
        pass

    @staticmethod
    def GetCurveEntity(curve, checkClosed):
        """ GetCurveEntity(curve: Curve, checkClosed: bool) -> ICurveEntity """
        pass

    @staticmethod
    def LessThanOrEquals(x, y, tolerance):
        """ LessThanOrEquals(x: float, y: float, tolerance: float) -> bool """
        pass

    @staticmethod
    def LessThanOrEqualTo(thisValue, value):
        """ LessThanOrEqualTo(thisValue: float, value: float) -> bool """
        pass

    @staticmethod
    def LocateFile(fileName):
        """ LocateFile(fileName: str) -> str """
        pass

    @staticmethod
    def RadiansToDegrees(rad):
        """ RadiansToDegrees(rad: float) -> float """
        pass

    @staticmethod
    def ToEntity(data):
        """ ToEntity(data: DesignScriptEntity) -> IDesignScriptEntity """
        pass

    @staticmethod
    def ToPointArray(points, checkRectangular):
        """ ToPointArray(points: Array[Array[IPointEntity]], checkRectangular: bool) -> Array[Array[Point]] """
        pass

    @staticmethod
    def ToPointEntityArray(points, checkRectangular):
        """ ToPointEntityArray(points: Array[Array[Point]], checkRectangular: bool) -> Array[Array[IPointEntity]] """
        pass

    PI = 3.1415926535897931
    __all__ = [
        'AreCoincident',
        'ConvertAll',
        'DegreesToRadians',
        'Equals',
        'EqualsTo',
        'ForEach',
        'GetCurveEntity',
        'LessThanOrEquals',
        'LessThanOrEqualTo',
        'LocateFile',
        'PI',
        'RadiansToDegrees',
        'ToEntity',
        'ToPointArray',
        'ToPointEntityArray',
    ]


class Helix(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByAxis(axisPoint, axisDirection, startPoint, pitch, angleTurns):
        """
        ByAxis(axisPoint: Point, axisDirection: Vector, startPoint: Point, pitch: float, angleTurns: float) -> Helix
        
            Create a Helix. The helix always rotates clockwise about the supplied  axis direction. If 
             viewing along the axis direction, the viewer will see  the point turning clockwise around the 
             axis as it moves along the curve  in the direction of increasing parameter. Pitch is Distance 
             the helix  moves in the axis direction per turn. This can be positive or negative.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Helix) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The angle in degrees through which the Helix turns over its length

Get: Angle(self: Helix) -> float

"""

    AxisDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the axis of the Helix

Get: AxisDirection(self: Helix) -> Vector

"""

    AxisPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base point of the Helix axis

Get: AxisPoint(self: Helix) -> Point

"""

    Pitch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The pitch of the helix in Degrees

Get: Pitch(self: Helix) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The radius of the arc

Get: Radius(self: Helix) -> float

"""


    mConstructor = None


class HostFactory(object):
    # no doc
    def PreloadAsmLibraries(self, baseDirectory):
        """ PreloadAsmLibraries(self: HostFactory, baseDirectory: str) """
        pass

    def ShutDown(self):
        """ ShutDown(self: HostFactory) """
        pass

    def StartUp(self):
        """ StartUp(self: HostFactory) """
        pass

    Factory = None
    Instance = None
    PersistenceManager = None


class IndexGroup(object):
    # no doc
    @staticmethod
    def ByIndices(a, b, c, d=None):
        """
        ByIndices(a: UInt32, b: UInt32, c: UInt32) -> IndexGroup
        
            Create an IndexGroup storing three indices
        ByIndices(a: UInt32, b: UInt32, c: UInt32, d: UInt32) -> IndexGroup
        
            Create an IndexGroup storing four indices
        """
        pass

    def Equals(self, other):
        """ Equals(self: IndexGroup, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: IndexGroup) -> int """
        pass

    def ToString(self):
        """ ToString(self: IndexGroup) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The first index

Get: A(self: IndexGroup) -> UInt32

"""

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The second index

Get: B(self: IndexGroup) -> UInt32

"""

    C = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The third index

Get: C(self: IndexGroup) -> UInt32

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Either 3 or 4, depending if it represents a triangle or a quad

Get: Count(self: IndexGroup) -> UInt32

"""

    D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fourth index

Get: D(self: IndexGroup) -> UInt32

"""



class IProtoGeometryConfiguration:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GeometryFactoryFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryFactoryFileName(self: IProtoGeometryConfiguration) -> str

Set: GeometryFactoryFileName(self: IProtoGeometryConfiguration) = value
"""

    PersistentManagerFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PersistentManagerFileName(self: IProtoGeometryConfiguration) -> str

Set: PersistentManagerFileName(self: IProtoGeometryConfiguration) = value
"""



class Line(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(bestFitPoints):
        """ ByBestFitThroughPoints(bestFitPoints: IEnumerable[Point]) -> Line """
        pass

    @staticmethod
    def ByStartPointDirectionLength(startPoint, direction, length):
        """
        ByStartPointDirectionLength(startPoint: Point, direction: Vector, length: float) -> Line
        
            Create a straight Line starting at start Point, extending in Vector direction by specified 
             length.
        """
        pass

    @staticmethod
    def ByStartPointEndPoint(startPoint, endPoint):
        """
        ByStartPointEndPoint(startPoint: Point, endPoint: Point) -> Line
        
            Creates a straight Line between two input Points.
        """
        pass

    @staticmethod
    def ByTangency(curve, parameter):
        """
        ByTangency(curve: Curve, parameter: float) -> Line
        
            Create a Line tangent to the input Curve, positioned at the parameter Point of the input Curve.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Line) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The direction of the Curve

Get: Direction(self: Line) -> Vector

"""


    mConstructor = None


class Loop(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Loop) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CoEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoEdges(self: Loop) -> Array[CoEdge]

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: Loop) -> Face

"""


    mConstructor = None


class Mesh(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByPointsFaceIndices(vertexPositions, indices):
        """ ByPointsFaceIndices(vertexPositions: IEnumerable[Point], indices: IEnumerable[IndexGroup]) -> Mesh """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Mesh) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FaceIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex indices that make up each face in a counterclockwise fashion

Get: FaceIndices(self: Mesh) -> Array[IndexGroup]

"""

    VertexNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The normal vector at this vertex

Get: VertexNormals(self: Mesh) -> Array[Vector]

"""

    VertexPositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The positions of the vertices

Get: VertexPositions(self: Mesh) -> Array[Point]

"""


    mConstructor = None


class NurbsCurve(Curve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByControlPoints(points, degree=None, closeCurve=None):
        """
        ByControlPoints(points: IEnumerable[Point], degree: int, closeCurve: bool) -> NurbsCurve
        ByControlPoints(points: IEnumerable[Point], degree: int) -> NurbsCurve
        ByControlPoints(points: IEnumerable[Point]) -> NurbsCurve
        """
        pass

    @staticmethod
    def ByControlPointsWeightsKnots(points, weights, knots, degree):
        """ ByControlPointsWeightsKnots(points: IEnumerable[Point], weights: Array[float], knots: Array[float], degree: int) -> NurbsCurve """
        pass

    @staticmethod
    def ByPoints(points, *__args):
        """
        ByPoints(points: IEnumerable[Point], degree: int) -> NurbsCurve
        ByPoints(points: IEnumerable[Point], closeCurve: bool) -> NurbsCurve
        ByPoints(points: IEnumerable[Point]) -> NurbsCurve
        """
        pass

    @staticmethod
    def ByPointsTangents(points, startTangent, endTangent):
        """ ByPointsTangents(points: IEnumerable[Point], startTangent: Vector, endTangent: Vector) -> NurbsCurve """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def ControlPoints(self):
        """
        ControlPoints(self: NurbsCurve) -> Array[Point]
        
            Get the control points of the NurbsCurve.  These are the points that the curve interpolates.
            Returns: An Array of Points
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Knots(self):
        """
        Knots(self: NurbsCurve) -> Array[float]
        
            The knots of the Curve.  These, along with the Degree, define the domain of the Curve where a 
             particular control vertex acts.
        """
        pass

    def ToString(self):
        """ ToString(self: NurbsCurve) -> str """
        pass

    def Weights(self):
        """
        Weights(self: NurbsCurve) -> Array[float]
        
            The weights of the control vertices of the curve.  These define the magnitude of influence of 
             the control vertices.
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Degree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The degree of the curve

Get: Degree(self: NurbsCurve) -> int

"""

    IsPeriodic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the NurbsCurve is periodic or not

Get: IsPeriodic(self: NurbsCurve) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether the NurbsCurve is rational or not.  This defines whether any of the weights are not 1.0.

Get: IsRational(self: NurbsCurve) -> bool

"""


    mConstructor = None


class Surface(Topology, IDisposable, IGraphicItem):
    # no doc
    def ApproximateWithTolerance(self, tolerance):
        """
        ApproximateWithTolerance(self: Surface, tolerance: float) -> NurbsSurface
        
            Gets a Nurbs representation of the Surface within a specified tolerance. This method may 
             approximate Surface in certain circumstances.
        """
        pass

    @staticmethod
    def ByLoft(crossSections, *__args):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> Surface
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> Surface
        ByLoft(crossSections: IEnumerable[Curve]) -> Surface
        """
        pass

    @staticmethod
    def ByPatch(closedCurve):
        """
        ByPatch(closedCurve: Curve) -> Surface
        
            Create a Surface by filling in the interior of a closed boundary defined by input Curves.
        """
        pass

    @staticmethod
    def ByPerimeterPoints(points):
        """ ByPerimeterPoints(points: IEnumerable[Point]) -> Surface """
        pass

    @staticmethod
    def ByRevolve(profile, axisOrigin, axisDirection, startAngle, sweepAngle):
        """
        ByRevolve(profile: Curve, axisOrigin: Point, axisDirection: Vector, startAngle: float, sweepAngle: float) -> Surface
        
            Create a Surface by sweeping the profile Curve around the axis ray formed  by origin Point in 
             the direction of the axis Vector, starting at start_angle in degrees, sweeping sweep_angle in 
             degrees.
        """
        pass

    @staticmethod
    def ByRuledLoft(crossSections):
        """ ByRuledLoft(crossSections: IEnumerable[Line]) -> Surface """
        pass

    @staticmethod
    def BySweep(profile, path):
        """
        BySweep(profile: Curve, path: Curve) -> Surface
        
            Create a Surface by sweeping a cross section Curve along a path.
        """
        pass

    @staticmethod
    def BySweep2Rails(path, guideRail, profile):
        """
        BySweep2Rails(path: Curve, guideRail: Curve, profile: Curve) -> Surface
        
            Sweep the cross section curve along a path guided by a two rails
        
            path: The input path to sweep along.
            guideRail: A rail to guide the orientation of the sweep.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def CoordinateSystemAtParameter(self, u, v):
        """
        CoordinateSystemAtParameter(self: Surface, u: float, v: float) -> CoordinateSystem
        
            Return a CoordinateSystem aligned with principal curvature directions.
        """
        pass

    def CurvatureAtParameter(self, u, v):
        """
        CurvatureAtParameter(self: Surface, u: float, v: float) -> CoordinateSystem
        
            The returned coordination system use xAxis, yAxis and zAxis to represent the uDir, vDir and 
             normal. The length of xAxis, yAxis represents the curvatures.
        """
        pass

    def DerivativesAtParameter(self, u, v):
        """
        DerivativesAtParameter(self: Surface, u: float, v: float) -> Array[Vector]
        
            Return the derivatives at input U and V coordinates.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def FlipNormalDirection(self):
        """
        FlipNormalDirection(self: Surface) -> Surface
        
            Returns a new Surface with the Normal flipped. Leaves this surface unchanged.
        """
        pass

    def GaussianCurvatureAtParameter(self, u, v):
        """
        GaussianCurvatureAtParameter(self: Surface, u: float, v: float) -> float
        
            Returns the Gaussian curvature at U and V parameters.
        """
        pass

    def GetIsoline(self, isoDirection, parameter):
        """
        GetIsoline(self: Surface, isoDirection: int, parameter: float) -> Curve
        
            Create a parameter line curve on the given surface. Create a Curve that represents a u or v 
             parameter line on the Surface. A  parameter line runs in the direction of increasing u or v 
             parameter at a  constant opposite u or v parameter. The resulting Curve will match the  Surface 
             parameterisation and its range will be bounded by the Surface  parameter range. The type of 
             Curve returned will depend on the Surface  type.
        
        
            isoDirection: If direction == 0, creates a U parameter line, if direction == 1, creates a V parameter line.
        """
        pass

    def Join(self, *__args):
        """
        Join(self: Surface, otherSurfaces: IEnumerable[Surface]) -> PolySurface
        Join(self: Surface, otherSurface: Surface) -> PolySurface
        
            Combines this Surface and input Surface into a PolySurface
        """
        pass

    def NormalAtParameter(self, u, v):
        """
        NormalAtParameter(self: Surface, u: float, v: float) -> Vector
        
            Return the normal Vector at specified U and V parameters.
        """
        pass

    def NormalAtPoint(self, point):
        """
        NormalAtPoint(self: Surface, point: Point) -> Vector
        
            Return the surface normal at the input Point on the Surface.
        """
        pass

    def Offset(self, distance):
        """
        Offset(self: Surface, distance: float) -> Surface
        
            Offset Surface in direction of Surface normal by specified distance.
        """
        pass

    def PerimeterCurves(self):
        """
        PerimeterCurves(self: Surface) -> Array[Curve]
        
            Return all the boundary Curves of the Surface.
        """
        pass

    def PointAtParameter(self, u, v):
        """
        PointAtParameter(self: Surface, u: float, v: float) -> Point
        
            Return the Point at specified U and V parameters.
        """
        pass

    def PrincipalCurvaturesAtParameter(self, u, v):
        """
        PrincipalCurvaturesAtParameter(self: Surface, u: float, v: float) -> Array[float]
        
            Returns the principal curvatures at the U and V parameters.
        """
        pass

    def PrincipalDirectionsAtParameter(self, u, v):
        """
        PrincipalDirectionsAtParameter(self: Surface, u: float, v: float) -> Array[Vector]
        
            Returns principal direction vectors at U and V parameters.
        """
        pass

    def ProjectInputOnto(self, geometryToProject, projectionDirection):
        """
        ProjectInputOnto(self: Surface, geometryToProject: Geometry, projectionDirection: Vector) -> Array[Geometry]
        
            Projects the input Geometry onto this Surface in the input Vector direction
        """
        pass

    def SubtractFrom(self, trimmingEntity):
        """
        SubtractFrom(self: Surface, trimmingEntity: Solid) -> Array[Geometry]
        
            Subtract the input tools from this Surface.
        """
        pass

    def TangentAtUParameter(self, u, v):
        """
        TangentAtUParameter(self: Surface, u: float, v: float) -> Vector
        
            Return the U tangent Vector at specified U and V parameters.
        """
        pass

    def TangentAtVParameter(self, u, v):
        """
        TangentAtVParameter(self: Surface, u: float, v: float) -> Vector
        
            Return the V tangent Vector at specified U and V parameters.
        """
        pass

    def Thicken(self, thickness, both_sides=None):
        """
        Thicken(self: Surface, thickness: float, both_sides: bool) -> Solid
        
            Thicken Surface into a Solid, extruding in the direction of Surface  normals. If both_sides 
             parameter is true, surface is thickened  on both sides.
        
        Thicken(self: Surface, thickness: float) -> Solid
        
            Thicken Surface into a Solid, extruding in the direction of Surface  normals on both sides of 
             the Surface.
        """
        pass

    def ToNurbsSurface(self):
        """
        ToNurbsSurface(self: Surface) -> NurbsSurface
        
            Gets a Nurbs representation of the Surface. This method may approximate Surface in certain 
             circumstances.
        """
        pass

    def ToString(self):
        """ ToString(self: Surface) -> str """
        pass

    def TrimWithEdgeLoops(self, loops):
        """ TrimWithEdgeLoops(self: Surface, loops: IEnumerable[PolyCurve]) -> Surface """
        pass

    def UVParameterAtPoint(self, point):
        """
        UVParameterAtPoint(self: Surface, point: Point) -> UV
        
            Return the UV parameter pair at the input Point. This is the inverse of Point at parameter.
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the total surface area.

Get: Area(self: Surface) -> float

"""

    Closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is closed in U or V directions

Get: Closed(self: Surface) -> bool

"""

    ClosedInU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is closed in U direction.

Get: ClosedInU(self: Surface) -> bool

"""

    ClosedInV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is closed in V direction

Get: ClosedInV(self: Surface) -> bool

"""

    Perimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the sum of all edges of the Surface.

Get: Perimeter(self: Surface) -> float

"""


    mConstructor = None


class NurbsSurface(Surface, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByControlPoints(controlVertices, uDegree, vDegree):
        """
        ByControlPoints(controlVertices: Array[Array[Point]], uDegree: int, vDegree: int) -> NurbsSurface
        
            Create a NurbsSurface by using explicit control Points, with specified U and V degrees.
        """
        pass

    @staticmethod
    def ByControlPointsWeightsKnots(controlVertices, weights, knotsU, knotsV, uDegree, vDegree):
        """
        ByControlPointsWeightsKnots(controlVertices: Array[Array[Point]], weights: Array[Array[float]], knotsU: Array[float], knotsV: Array[float], uDegree: int, vDegree: int) -> NurbsSurface
        
            Creates a NurbsSurface with specified control vertices, knots, weights,  and U V degrees.  There 
             are several restrictions on the data which, if broken, will cause the function to fail and will 
             throw an exception. Degree: Both u- and v- degree should be >= 1 (piecewise-linear spline)  and  
             less than 26 (the maximum B-spline basis degree supported by ASM). Weights: All weight values 
             (if supplied) should be strictly positive.  Weights smaller than 1e-11 will be rejected and the 
             function will fail.  Knots: Both knot vectors should be non-decreasing sequences. Interior knot 
             multiplicity should be no larger than degree + 1 at the start/end knot and  degree at an 
             internal knot (this allows surfaces with G1 discontinuities to  be represented). Note that 
             non-clamped knot vectors are supported, but will  be converted to clamped ones, with the 
             corresponding changes applied to the  control point/weight data.
        """
        pass

    @staticmethod
    def ByPoints(points, uDegree, vDegree):
        """
        ByPoints(points: Array[Array[Point]], uDegree: int, vDegree: int) -> NurbsSurface
        
            Creates a NurbsSurface with specified interpolated points and  U and V degrees.  The resultant 
             surface will pass through all of the points.
        """
        pass

    @staticmethod
    def ByPointsTangents(points, startUTangents, endUTangents, startVTangents, endVTangents):
        """ ByPointsTangents(points: Array[Array[Point]], startUTangents: IEnumerable[Vector], endUTangents: IEnumerable[Vector], startVTangents: IEnumerable[Vector], endVTangents: IEnumerable[Vector]) -> NurbsSurface """
        pass

    @staticmethod
    def ByPointsTangentsKnotsDerivatives(points, startUTangents, endUTangents, startVTangents, endVTangents, uKnots, vKnots, cornerTwistDerivatives):
        """ ByPointsTangentsKnotsDerivatives(points: Array[Array[Point]], startUTangents: IEnumerable[Vector], endUTangents: IEnumerable[Vector], startVTangents: IEnumerable[Vector], endVTangents: IEnumerable[Vector], uKnots: Array[float], vKnots: Array[float], cornerTwistDerivatives: IEnumerable[Vector]) -> NurbsSurface """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def ControlPoints(self):
        """
        ControlPoints(self: NurbsSurface) -> Array[Array[Point]]
        
            Returns NurbsSurface control points (poles).
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: NurbsSurface) -> str """
        pass

    def UKnots(self):
        """
        UKnots(self: NurbsSurface) -> Array[float]
        
            Surface knots in U direction.
        """
        pass

    def VKnots(self):
        """
        VKnots(self: NurbsSurface) -> Array[float]
        
            Surface knots in V direction.
        """
        pass

    def Weights(self):
        """
        Weights(self: NurbsSurface) -> Array[Array[float]]
        
            Returns NurbsSurface control point weights.
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DegreeU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Surface degree in the U direction.

Get: DegreeU(self: NurbsSurface) -> int

"""

    DegreeV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Surface degree in the V direction.

Get: DegreeV(self: NurbsSurface) -> int

"""

    IsPeriodicInU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is periodic in the U direction.

Get: IsPeriodicInU(self: NurbsSurface) -> bool

"""

    IsPeriodicInV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is periodic in the V direction.

Get: IsPeriodicInV(self: NurbsSurface) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns true if the Surface is rational.

Get: IsRational(self: NurbsSurface) -> bool

"""

    NumControlPointsU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of control Points in the U direction.

Get: NumControlPointsU(self: NurbsSurface) -> int

"""

    NumControlPointsV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of control Points in the V direction.

Get: NumControlPointsV(self: NurbsSurface) -> int

"""


    mConstructor = None


class Plane(Geometry, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByBestFitThroughPoints(points):
        """ ByBestFitThroughPoints(points: IEnumerable[Point]) -> Plane """
        pass

    @staticmethod
    def ByLineAndPoint(line, point):
        """
        ByLineAndPoint(line: Line, point: Point) -> Plane
        
            Create the Plane containing the input Line and external Point. Point cannot lie on the Line or 
             in the Line axis.
        """
        pass

    @staticmethod
    def ByOriginNormal(origin, normal):
        """
        ByOriginNormal(origin: Point, normal: Vector) -> Plane
        
            Create a Plane centered at root Point, with input normal Vector.
        """
        pass

    @staticmethod
    def ByOriginNormalXAxis(origin, normal, xAxis):
        """
        ByOriginNormalXAxis(origin: Point, normal: Vector, xAxis: Vector) -> Plane
        
            Create an "oriented" Plane, positioned at Point origin with Vector  normal, but with a specific 
             X axis orientation. This has no impact to splitting, intersect, project, etc oporations, it only 
             specifies the orientation of the input CoordinateSystem.
        """
        pass

    @staticmethod
    def ByOriginXAxisYAxis(origin, xAxis, yAxis):
        """
        ByOriginXAxisYAxis(origin: Point, xAxis: Vector, yAxis: Vector) -> Plane
        
            The X and Y axis lie in the plane. The Z axis is the cross product of the two Vectors.
        """
        pass

    @staticmethod
    def ByThreePoints(origin, planePoint, xAxisPoint):
        """
        ByThreePoints(origin: Point, planePoint: Point, xAxisPoint: Point) -> Plane
        
            Create a the Plane containing the three input Points.
        
            origin: The plane origin
            planePoint: Any point lying on the plane
            xAxisPoint: The point lying on the X-axis of the plane wrt to the plane origin
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def Offset(self, dist):
        """
        Offset(self: Plane, dist: float) -> Plane
        
            Create a new Plane offset by this Plane in the normal direction by the specified distance.
        """
        pass

    def ToCoordinateSystem(self):
        """
        ToCoordinateSystem(self: Plane) -> CoordinateSystem
        
            Produces a new CoordinateSystem representing this plane. It is based on  the origin, and X and Y 
             axis basis.
        """
        pass

    def ToString(self):
        """ ToString(self: Plane) -> str """
        pass

    @staticmethod
    def XY():
        """
        XY() -> Plane
        
            Creates a plane in the world XY
        """
        pass

    @staticmethod
    def XZ():
        """
        XZ() -> Plane
        
            Creates a plane in the world XZ plane
        """
        pass

    @staticmethod
    def YZ():
        """
        YZ() -> Plane
        
            Creates a plane in the world YZ
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the normal direction of the Plane.

Get: Normal(self: Plane) -> Vector

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the origin of the Plane.

Get: Origin(self: Plane) -> Point

"""

    XAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The X basis of the Plane

Get: XAxis(self: Plane) -> Vector

"""

    YAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Y basis of the Plane

Get: YAxis(self: Plane) -> Vector

"""


    mConstructor = None


class Point(Geometry, IDisposable, IGraphicItem):
    # no doc
    def Add(self, vectorToAdd):
        """
        Add(self: Point, vectorToAdd: Vector) -> Point
        
            Add a vector to a point.  The same as Translate(Vector).
        """
        pass

    def AsVector(self):
        """
        AsVector(self: Point) -> Vector
        
            Get the Vector with the same X, Y, and Z component
        """
        pass

    @staticmethod
    def ByCartesianCoordinates(cs, x, y, z):
        """
        ByCartesianCoordinates(cs: CoordinateSystem, x: float, y: float, z: float) -> Point
        
            Form a Point in the given coordinate system with 3 cartesian coordinates
        """
        pass

    @staticmethod
    def ByCoordinates(x, y, z=None):
        """
        ByCoordinates(x: float, y: float, z: float) -> Point
        
            Form a Point given 3 cartesian coordinates
        ByCoordinates(x: float, y: float) -> Point
        
            Form a Point in the XY plane given two 2 cartesian coordinates.  The Z component is 0.
        """
        pass

    @staticmethod
    def ByCylindricalCoordinates(cs, angle, elevation, radius):
        """
        ByCylindricalCoordinates(cs: CoordinateSystem, angle: float, elevation: float, radius: float) -> Point
        
            Form a Point in the given coordinate system given its position in cylindrical coordinates.
        
            cs: The coordinate system to build the point in
            angle: The angle is the rotation from the X axis in the coordinate system around the Z axis in degrees
            elevation: The elevation of the point above the XY plane
            radius: The distance from the origin of the coordinate system
            Returns: A new Point
        """
        pass

    @staticmethod
    def BySphericalCoordinates(cs, phi, theta, radius):
        """
        BySphericalCoordinates(cs: CoordinateSystem, phi: float, theta: float, radius: float) -> Point
        
            Form a Point in the given coordinate system given its position in spherical coordinates.
        
            cs: The coordinate system to build the point in
            phi: The angle down from the Z axis in degrees
            theta: The rotation around the sphere from the X axis in degrees
            radius: The offset from the origin
            Returns: A new Point
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Point) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: Point, other: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def Origin():
        """
        Origin() -> Point
        
            Get the Origin point (0,0,0)
        """
        pass

    def Project(self, baseGeometry, projectionDirection):
        """
        Project(self: Point, baseGeometry: Geometry, projectionDirection: Vector) -> Array[Geometry]
        
            Project another piece of Geometry onto this along a given direction Vector
        """
        pass

    @staticmethod
    def PruneDuplicates(points, tolerance):
        """ PruneDuplicates(points: IEnumerable[Point], tolerance: float) -> Array[Point] """
        pass

    def Subtract(self, vectorToSubtract):
        """
        Subtract(self: Point, vectorToSubtract: Vector) -> Point
        
            Subtract a vector from a point.  The same as Translate(-Vector).
        """
        pass

    def ToString(self):
        """ ToString(self: Point) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the X component of a Point

Get: X(self: Point) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Y component of a Point

Get: Y(self: Point) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Z component of a Point

Get: Z(self: Point) -> float

"""


    mConstructor = None


class PolyCurve(Curve, IDisposable, IGraphicItem):
    # no doc
    def BasePlane(self):
        """
        BasePlane(self: PolyCurve) -> Plane
        
            Returns plane of planar polycurve
        """
        pass

    @staticmethod
    def ByJoinedCurves(curves):
        """ ByJoinedCurves(curves: IEnumerable[Curve]) -> PolyCurve """
        pass

    @staticmethod
    def ByPoints(points, connectLastToFirst):
        """ ByPoints(points: IEnumerable[Point], connectLastToFirst: bool) -> PolyCurve """
        pass

    @staticmethod
    def ByThickeningCurve(curve, thickness, nor):
        """
        ByThickeningCurve(curve: Curve, thickness: float, nor: Vector) -> PolyCurve
        
            Make PolyCurve by thickening a curve.
        
            curve: the curve to thicken
            thickness: the thickness
            nor: the normal perpendicular to the thickening direction
        """
        pass

    def CloseWithLine(self):
        """
        CloseWithLine(self: PolyCurve) -> PolyCurve
        
            Close polycurve by line connecting start and end points
        """
        pass

    def CloseWithLineAndTangentArcs(self, radiusAtStart, radiusAtEnd):
        """
        CloseWithLineAndTangentArcs(self: PolyCurve, radiusAtStart: float, radiusAtEnd: float) -> PolyCurve
        
            Close polycurve by tangent chain of arc, line, and arc
        
            radiusAtStart: Radius of arc at start of polycurve
            radiusAtEnd: Radius of arc at end of polycurve
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def CurveAtIndex(self, index, endOrStart):
        """
        CurveAtIndex(self: PolyCurve, index: int, endOrStart: bool) -> Curve
        
            Returns curve of the polycurve by index
        
            index: Length to locate point
            endOrStart: counting from end or start of the polycurve
        """
        pass

    def Curves(self):
        """
        Curves(self: PolyCurve) -> Array[Curve]
        
            Returns curves of the polycurve
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ExtendWithArc(self, length, radius, endOrStart):
        """
        ExtendWithArc(self: PolyCurve, length: float, radius: float, endOrStart: bool) -> PolyCurve
        
            Extends polycurve by tangent arc
        
            length: Length of extension arc
            radius: Radius of arc
            endOrStart: extending end or start of the polycurve
        """
        pass

    def ExtendWithEllipse(self, length, radius1, radius2, endEllipseParameter, endOrStart):
        """
        ExtendWithEllipse(self: PolyCurve, length: float, radius1: float, radius2: float, endEllipseParameter: float, endOrStart: bool) -> PolyCurve
        
            Extends polycurve by tangent ellipse
        
            length: Length of extension ellipse
            radius1: Parameter of ellipse
            radius2: Parameter of ellipse
            endEllipseParameter: Parameter of ellipse
            endOrStart: extending end or start of the polycurve
        """
        pass

    def Fillet(self, radius, rightSide):
        """
        Fillet(self: PolyCurve, radius: float, rightSide: bool) -> PolyCurve
        
            Fillet polycurve in its plane.
        
            radius: Radius of fillet
            rightSide: If right side which to fillet
        """
        pass

    def Offset(self, distance, extendCircular=None):
        """
        Offset(self: PolyCurve, distance: float, extendCircular: bool) -> Curve
        
            Offset polycurve in its plane.
        
            extendCircular: If true, corners will be made circular
        """
        pass

    def ToString(self):
        """ ToString(self: PolyCurve) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    NumberOfCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of curves of the polycurve

Get: NumberOfCurves(self: PolyCurve) -> int

"""


    mConstructor = None


class Polygon(PolyCurve, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByPoints(points):
        """ ByPoints(points: IEnumerable[Point]) -> Polygon """
        pass

    def Center(self):
        """
        Center(self: Polygon) -> Point
        
            Returns average point of corners of polygon
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def ContainmentTest(self, point):
        """
        ContainmentTest(self: Polygon, point: Point) -> bool
        
            Checks if point is inside planar polygon without self intersections.
        """
        pass

    def Corners(self):
        """
        Corners(self: Polygon) -> Array[Point]
        
            Returns corners of polygon
        """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    @staticmethod
    def RegularPolygon(circle, numberSides):
        """
        RegularPolygon(circle: Circle, numberSides: int) -> Polygon
        
            Construct an inscribed Polygon Curve within a circle.
        """
        pass

    def SelfIntersections(self):
        """
        SelfIntersections(self: Polygon) -> Array[Point]
        
            Returns self intersections between sides of the polygon.
        """
        pass

    def ToString(self):
        """ ToString(self: Polygon) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PlaneDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns maximum deviation from average plane of polygon.

Get: PlaneDeviation(self: Polygon) -> float

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns all the segment start / end points.

Get: Points(self: Polygon) -> Array[Point]

"""


    mConstructor = None


class PolySurface(Surface, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByJoinedSurfaces(surfaces):
        """ ByJoinedSurfaces(surfaces: IEnumerable[Surface]) -> PolySurface """
        pass

    @staticmethod
    def ByLoft(crossSections, guideCurve=None):
        """
        ByLoft(crossSections: IEnumerable[Curve], guideCurve: Curve) -> PolySurface
        ByLoft(crossSections: IEnumerable[Curve]) -> PolySurface
        """
        pass

    @staticmethod
    def ByLoftGuides(crossSections, guideCurves):
        """ ByLoftGuides(crossSections: IEnumerable[Curve], guideCurves: IEnumerable[Curve]) -> PolySurface """
        pass

    @staticmethod
    def BySolid(solid):
        """
        BySolid(solid: Solid) -> PolySurface
        
            Make Polysurface by surfaces of Solid.
        
            solid: Solid which surfaces to use
        """
        pass

    @staticmethod
    def BySweep(rail, *__args):
        """
        BySweep(rail: Curve, profile: Curve) -> PolySurface
        
            Make Polysurface by sweeping a curve along rail.
        
            rail: Curve to sweep along
            profile: Sweep profile
        BySweep(rail: Curve, crossSection: IEnumerable[Curve]) -> PolySurface
        """
        pass

    def Chamfer(self, edges, offset):
        """ Chamfer(self: PolySurface, edges: IEnumerable[Edge], offset: float) -> PolySurface """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def EdgeCount(self):
        """
        EdgeCount(self: PolySurface) -> int
        
            number of edges of Polysurface
        """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ExtractSolids(self):
        """
        ExtractSolids(self: PolySurface) -> Array[Solid]
        
            Extract Solids from Polysurface defined by subset of surfaces
        """
        pass

    def Fillet(self, edges, radius):
        """ Fillet(self: PolySurface, edges: IEnumerable[Edge], radius: float) -> PolySurface """
        pass

    def LocateSurfacesByLine(self, line):
        """
        LocateSurfacesByLine(self: PolySurface, line: Line) -> Array[Surface]
        
            Locate Surfaces by Line. Takes all surfaces hit by line.
        """
        pass

    def LocateSurfacesByPoint(self, point, direction):
        """
        LocateSurfacesByPoint(self: PolySurface, point: Point, direction: Vector) -> Array[Surface]
        
            Locate Surfaces by point. Takes first intersection in forward direction.  Returns one surface if 
             hit  surface interior, two if hit edge interior, and many if hit vertex
        """
        pass

    def SurfaceCount(self):
        """
        SurfaceCount(self: PolySurface) -> int
        
            number of surfaces of Polysurface
        """
        pass

    def Surfaces(self):
        """
        Surfaces(self: PolySurface) -> Array[Surface]
        
            Return new Surfaces representing the underlying Surfaces.
        """
        pass

    def ToString(self):
        """ ToString(self: PolySurface) -> str """
        pass

    def UnconnectedBoundaries(self):
        """
        UnconnectedBoundaries(self: PolySurface) -> Array[PolyCurve]
        
            Compute 2d cell boundaries which are not connected to other Surfaces
        """
        pass

    def VertexCount(self):
        """
        VertexCount(self: PolySurface) -> int
        
            number of vertices of Polysurface
        """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    mConstructor = None


class ProtoGeometryConfiguration(object, IProtoGeometryConfiguration):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    GeometryFactoryFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryFactoryFileName(self: ProtoGeometryConfiguration) -> str

Set: GeometryFactoryFileName(self: ProtoGeometryConfiguration) = value
"""

    PersistentManagerFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PersistentManagerFileName(self: ProtoGeometryConfiguration) -> str

Set: PersistentManagerFileName(self: ProtoGeometryConfiguration) = value
"""



class Rectangle(Polygon, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByCornerPoints(*__args):
        """
        ByCornerPoints(p1: Point, p2: Point, p3: Point, p4: Point) -> Rectangle
        
            Create a Rectangle by four corner Points.
        ByCornerPoints(points: IEnumerable[Point]) -> Rectangle
        """
        pass

    @staticmethod
    def ByWidthLength(*__args):
        """
        ByWidthLength(cs: CoordinateSystem, width: float, length: float) -> Rectangle
        
            Create a Rectangle centered at the input origin in the CoordinateSystem  XY Plane, with 
             specified width (X Axis length), and length  (Y Axis length).
        
        ByWidthLength(plane: Plane, width: float, length: float) -> Rectangle
        
            Create a Rectangle centered at input Plane root, with input width  (Plane X axis length), and 
             length (Plane Y axis length).
        
        ByWidthLength(width: float, length: float) -> Rectangle
        
            Create a Rectangle centered at the WCS origin in the WCS XY Plane, with specified width (X Axis 
             length), and length (Y Axis length).
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Rectangle) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the Rectangle

Get: Height(self: Rectangle) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the Rectangle

Get: Width(self: Rectangle) -> float

"""


    mConstructor = None


class Sphere(Solid, IDisposable, IGraphicItem):
    # no doc
    @staticmethod
    def ByBestFit(points):
        """ ByBestFit(points: IEnumerable[Point]) -> Sphere """
        pass

    @staticmethod
    def ByCenterPointRadius(centerPoint, radius):
        """
        ByCenterPointRadius(centerPoint: Point, radius: float) -> Sphere
        
            Create a Solid Sphere cetered at the input Point, with given radius.
        """
        pass

    @staticmethod
    def ByFourPoints(points):
        """ ByFourPoints(points: IEnumerable[Point]) -> Sphere """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Geometry) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: Geometry, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: Geometry) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Sphere) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the center Point of the Sphere.

Get: CenterPoint(self: Sphere) -> Point

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the radius of the Sphere.

Get: Radius(self: Sphere) -> float

"""


    mConstructor = None


class UV(object):
    # no doc
    @staticmethod
    def ByCoordinates(u, v):
        """
        ByCoordinates(u: float, v: float) -> UV
        
            Create a UV from two doubles.
        """
        pass

    def Equals(self, other):
        """ Equals(self: UV, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UV) -> int """
        pass

    def ToString(self):
        """ ToString(self: UV) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    U = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the U component of a UV

Get: U(self: UV) -> float

"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the V component of a V

Get: V(self: UV) -> float

"""



class Vector(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def Add(self, vectorToAdd):
        """
        Add(self: Vector, vectorToAdd: Vector) -> Vector
        
            Add a vector
        """
        pass

    def AngleAboutAxis(self, otherVector, rotationAxis):
        """
        AngleAboutAxis(self: Vector, otherVector: Vector, rotationAxis: Vector) -> float
        
            Returns the angle between the two Vectors, in the range [0, 360] degrees. It uses axis of 
             rotation to determine the direction of the angle.
        """
        pass

    def AngleBetween(self, otherVector, rotationAxis=None):
        """
        AngleBetween(self: Vector, otherVector: Vector, rotationAxis: Vector) -> float
        AngleBetween(self: Vector, otherVector: Vector) -> float
        """
        pass

    def AngleWithVector(self, otherVector):
        """
        AngleWithVector(self: Vector, otherVector: Vector) -> float
        
            Returns the angle between the two Vectors, in the range [0, 180] degrees.
        """
        pass

    def AsPoint(self):
        """
        AsPoint(self: Vector) -> Point
        
            Get the Point with the same X, Y, and Z component
        """
        pass

    @staticmethod
    def ByCoordinates(x, y, z, normalized=None):
        """
        ByCoordinates(x: float, y: float, z: float, normalized: bool) -> Vector
        
            Form a Vector by 3 Euclidean coordinates and normalize the Vector
        
            x: X coordinate
            y: Y coordinate
            z: Z coordinate
            normalized: Whether to normalize the result Vector or not
        ByCoordinates(x: float, y: float, z: float) -> Vector
        
            Form a Vector by 3 Euclidean coordinates
        
            x: X coordinate
            y: Y coordinate
            z: Z coordinate
        """
        pass

    @staticmethod
    def ByTwoPoints(start, end):
        """
        ByTwoPoints(start: Point, end: Point) -> Vector
        
            Form a Vector by two end points.  The result is a vector from the start to the end point.
        """
        pass

    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: Vector) -> int """
        pass

    def Cross(self, cross):
        """
        Cross(self: Vector, cross: Vector) -> Vector
        
            Form the cross product of two vectors
        """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Dot(self, vec):
        """
        Dot(self: Vector, vec: Vector) -> float
        
            Form the dot product of two vectors
        """
        pass

    def Equals(self, obj):
        """ Equals(self: Vector, other: DesignScriptEntity) -> bool """
        pass

    def IsAlmostEqualTo(self, other):
        """
        IsAlmostEqualTo(self: Vector, other: Vector) -> bool
        
            Determine whether two vectors ae almost equal
        """
        pass

    def IsParallel(self, other):
        """
        IsParallel(self: Vector, other: Vector) -> bool
        
            Determine whether two vectors are parallel or not
        """
        pass

    def Normalized(self):
        """
        Normalized(self: Vector) -> Vector
        
            Get the normalized version of a vector
        """
        pass

    def Reverse(self):
        """
        Reverse(self: Vector) -> Vector
        
            Get the reverse of the vector.  Essentially this negates the X, Y, and Z components of the 
             Vector.
        """
        pass

    def Rotate(self, *__args):
        """
        Rotate(self: Vector, plane: Plane, degrees: float) -> Vector
        
            Rotates a vector around the Plane origin and normal by a specified  degree
        Rotate(self: Vector, axis: Vector, degrees: float) -> Vector
        
            Rotates a Vector around an axis by a specified number of degrees
        """
        pass

    def Scale(self, *__args):
        """
        Scale(self: Vector, xScaleFactor: float, yScaleFactor: float, zScaleFactor: float) -> Vector
        
            Scale Vector non-uniformly around the origin
        Scale(self: Vector, scale_factor: float) -> Vector
        
            Scale Vector uniformly around the origin
        """
        pass

    def Subtract(self, vectorToSubtract):
        """
        Subtract(self: Vector, vectorToSubtract: Vector) -> Vector
        
            Subtract a vector
        """
        pass

    def ToString(self):
        """ ToString(self: Vector) -> str """
        pass

    def Transform(self, cs):
        """
        Transform(self: Vector, cs: CoordinateSystem) -> Vector
        
            Transform this Vector by input CoordinateSystem matrix.
        """
        pass

    @staticmethod
    def XAxis():
        """
        XAxis() -> Vector
        
            Get the canonical X axis Vector (1,0,0)
        """
        pass

    @staticmethod
    def YAxis():
        """
        YAxis() -> Vector
        
            Get the canonical Y axis Vector (0,1,0)
        """
        pass

    @staticmethod
    def ZAxis():
        """
        ZAxis() -> Vector
        
            Get the canonical Z axis Vector (0,0,1)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the length of the vector - otherwise known as the Euclidean norm

Get: Length(self: Vector) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the X component of a Vector

Get: X(self: Vector) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Y component of a Vector

Get: Y(self: Vector) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the Z component of a Vector

Get: Z(self: Vector) -> float

"""


    mConstructor = None


class Vertex(DesignScriptEntity, IDisposable, IGraphicItem):
    # no doc
    def ComputeHashCode(self, *args): #cannot find CLR method
        """ ComputeHashCode(self: DesignScriptEntity) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: DesignScriptEntity, disposing: bool) """
        pass

    def DisposeDisplayable(self, *args): #cannot find CLR method
        """ DisposeDisplayable(self: DesignScriptEntity) """
        pass

    def Equals(self, obj):
        """ Equals(self: DesignScriptEntity, dsentity: DesignScriptEntity) -> bool """
        pass

    def ToString(self):
        """ ToString(self: Vertex) -> str """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AdjacentEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Edges emanating from this Vertex

Get: AdjacentEdges(self: Vertex) -> Array[Edge]

"""

    AdjacentFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Faces adjacent to this Vertex

Get: AdjacentFaces(self: Vertex) -> Array[Face]

"""

    PointGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Point where this Vertex is located

Get: PointGeometry(self: Vertex) -> Point

"""


    mConstructor = None


# variables with complex values

